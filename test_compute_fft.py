import compute_fft
import numpy as np

freq_max_plot = 50
y_axis = "signal amplitude"
units = "-"
title = "my multiharmonic signal"
fs = 100            # Sampling frequency [Hz]
T = 10.0              # Signal duration [s]
f1 = 1           # Signal frequency [Hz]
f2 = 3
f3 = 2400
f4 = 6
f5 = 8
f6 = 10
f7 = 12
A1 = 3.0              # Signal amplitude
A2 = 1.0
A3 = 0
A4 = 0.00
A5 = 0.000
A6 = 0.0000
A7 = 0.00000
thr = 1e-5
law = 2 #power law applied to signal

t = np.arange(0, T, 1 / fs)
x = (A1 * np.sin(2*np.pi*f1*t) + A2 * np.sin(2*np.pi*f2*t) + A3 * np.sin(2*np.pi*f3*t) + A4 * np.sin(2*np.pi*f4*t) + A5 * np.sin(2*np.pi*f5*t) + A6 * np.sin(2*np.pi*f6*t) + A7 * np.sin(2*np.pi*f7*t))  # <-- define ANY signal here
x_nl = x**law

compute_fft.compute_fft(t, x, thr, freq_max_plot, y_axis, units, "x")
compute_fft.compute_fft(t, x_nl, thr, freq_max_plot, y_axis, units, "x^"+str(law))