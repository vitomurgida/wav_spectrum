# wav_spectrum

What:
wav_spectrum is a simple Python project that reads an audio recording in .wav format and computes the frequency spectrum of the signal using an fft.

Why:
wav_spectrum can help identifying and characterize noise sources with a simple measurement performed with a mobile. 

Files:
- wav_fft.py = the main file. Inputs are defined here. You need to modify only this file.
- compute_fft.py = computes the fft of the signal. It uses an Hanning windowing.
- test_compute_fft.py = validation test of compute_fft.py, using an analytical (multi-)harmonic signal, whose harmonics amplitudes and frequencies can be     calculated by hand using basic trigonometry.

Outputs:
- spectrum and time history of an arbitrary slice of the orginal signal, peaks frequencies, amplitudes and rms
- original digital signal time history, its sampling frequency, duration, and quantization (for example float32)    

Inputs:
- .wav location
- observation window on the measurement. The FFT is performed only on this window.
- min and max frequency at which visualizing the spectrum, to zoom into specific frequency ranges
- threshold for peak picking, as percentage of max peak amplitude

