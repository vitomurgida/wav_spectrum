import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import compute_fft
import os

# Inputs
file_name = "HVAC-iPhone-mic.wav"
start_time = 0.5
end_time = 2.3
freq_min_plot = 50
freq_max_plot = 400
thr = 0.5 # threshold for peak picking, as a percentage of maximum peak

# data and sample rate
folder_path = os.getcwd()
sample_rate, data = wavfile.read(folder_path + "/measurements/" + file_name)
print ("channels = ", len(data.shape))
print ("data type = ", data.dtype)
print ("sample rate = ", sample_rate)

# time vector
time = np.linspace(0, len(data)/ sample_rate, num=len(data))
print ("duration = ", time[-1], "s")

# check input
if end_time >= time[-1] or end_time > time[-1]:
    raise Exception("ERROR: Data not available at end_time, reduce it")

if end_time <= start_time:
    raise Exception("ERROR: end_time must be greater than start_time")

if freq_min_plot < 0:
    raise Exception("ERROR: Frequency must be greater than 0")

if freq_max_plot > sample_rate/2:
    raise Exception("ERROR: Max frequency must be less than half-sample rate")

# isolate only first channel in case measurement has two channels
if len(data.shape) > 1:
    data = data[:, 0]

# plot measured signal
plt.figure(figsize=(10,6))
plt.plot(time, data)
plt.title(file_name)
plt.xlabel("time (s)")
plt.ylabel("amplitude digital [-]")
plt.grid(True)
plt.show()

# observation window
time = time[(int(start_time)*sample_rate):(int(end_time)*sample_rate)]
data = data[(int(start_time)*sample_rate):(int(end_time)*sample_rate)]

# FFT
compute_fft.compute_fft(time, data, thr, freq_min_plot, freq_max_plot, "digital signal amplitude" , "-", file_name)

