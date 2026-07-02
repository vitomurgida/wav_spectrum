# wav_spectrum
Use wav_fft.py to compute the spectrum of your .wav file.

wav_fft.py is a simple Python code which reads an audio recording in .wav format and computes the frequency spectrum of the signal.
To compute the fft, it makes use of the function in compute_fft.py
test_compute_fft.py contains a code used to validate compute_fft.py, using an analytical signal for which harmonics amplitudes and frequencies can be calculated by hand.

It outputs:
- original signal time history
- slice of the time history to be analyzed, arbitrarily chosen by the user, and frequency spectrum based on its
peaks frequencies, amplitudes and rms
- sampling frequency
- measurement duration

The user can choose:
- .wav file location
- time range in which performing the FFT analysis (start and end time)
- maximum frequency to visualize in the spectrum (which, as theory teaches, is limited by the sampling frequency of the microphone used for the measurement)
- threshold for which a peak is peaked or not for frequency peak recognizition, as a percentage of the largest peak
- figure title and y-axis title and units

Files:
- compute_fft = computes the fft of signal
- fft_from_wav = reads a .wav file and computes its spectrum using compute_fft
