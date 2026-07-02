import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
import compute_fft

# Inputs
folder_path = "/home/vitomurgida/5. Upwork/John White - HVAC + Pool Pumps Noise/"
file_name = "HVAC-iPhone-mic.wav" # HVAC-iPhone-mic.wav # Backyard - pool pump.wav
start_time = 50 # initial time for time range of analysis
end_time = 55 # end time for time range of analysis
freq_max_plot = 1500
thr = 0.1 # threshold for peak picking, as a percentage of maximum peak

sample_rate, data = wavfile.read(folder_path+file_name)

# number of measurement samples, sample rate and data format
print ("data.shape = ", data.shape)
print ("data type = ", data.dtype)
print ("sample rate = ", sample_rate)

# time vector
num_samples = len(data)
time = np.linspace(0, num_samples / sample_rate, num=num_samples)
print ("time shape = ", time.shape)
print ("duration = ", time[-1], "s")

if end_time >= time[-1] or end_time > time[-1]:
    raise Exception("ERROR: Data not available at this time range, reduce it!")

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
time = time[(start_time*sample_rate):(end_time*sample_rate)]
data = data[(start_time*sample_rate):(end_time*sample_rate)]
print (time)
# FFT
freqs, amp, peaks = compute_fft.compute_fft(time, data, thr, "amplitude digital", "-", file_name, freq_max_plot)

