import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import compute_fft

# Inputs
folder_path = "/home/vitomurgida/Downloads/"
file_name = "2 lug, 22.09_ - moto + uccelli.wav"
start_time = 0.5 # initial time for time range of analysis
end_time = 2.3 # end time for time range of analysis
freq_min_plot = 50
freq_max_plot = 400
thr = 0.5 # threshold for peak picking, as a percentage of maximum peak
y_axis = "amplitude digital"
units = "-"

# data and sample rate
sample_rate, data = wavfile.read(folder_path+file_name)
print ("channels = ", len(data.shape))
print ("data type = ", data.dtype)
print ("sample rate = ", sample_rate)

# time vector
time = np.linspace(0, len(data)/ sample_rate, num=len(data))
print ("duration = ", time[-1], "s")

# check input
if end_time >= time[-1] or end_time > time[-1]:
    raise Exception("ERROR: Data not available at this time range, reduce it")

if end_time <= start_time:
    raise Exception("ERROR: end_time must be greater than start_time")

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

# reduce measurement range for quicker analysis
time = time[(int(start_time)*sample_rate):(int(end_time)*sample_rate)]
data = data[(int(start_time)*sample_rate):(int(end_time)*sample_rate)]

# FFT
compute_fft.compute_fft(time, data, thr, freq_min_plot, freq_max_plot, y_axis , "["+units+"]", file_name)

