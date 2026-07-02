def compute_fft(t, x, thr, name, units, title, freq_max_plot):

    import numpy as np
    from scipy.signal import find_peaks
    import matplotlib
    #matplotlib.use("TkAgg")  # or "TkAgg" if Qt not installed
    import matplotlib.pyplot as plt

# INPUTS DESCRIPTION
# fs = sampling frequency
# t = time vector
# x = signal
# thr = threshold for peak detection as scaling factor of max amplitude harmonic

    # Sampling frequency
    fs = 1/(t[1] - t[0])

    # WINDOWING (HANN)
    window = np.hanning(len(x))
    x_win = x * window

    # Window correction factor (coherent gain)
    U = np.sum(window) / len(window)

    # FFT COMPUTATION
    N = len(x)
    X = np.fft.rfft(x_win) # numpy FFT gives unnormalized real FFT, so need to rescale by N
    freqs = np.fft.rfftfreq(N, 1/fs)

    # AMPLITUDE SCALING
    amp = (2 / (N * U)) * np.abs(X) # N needed to normalize FFT, U to correct for windowing reduction of signal power, 2 needed to recover negative side neglected by np.ff.rfft
    amp[0] = amp[0] / 2
    rms = amp / np.sqrt(2)

    # PEAK DETECTION
    threshold = np.max(amp) * thr
    peaks, _ = find_peaks(amp, height=threshold)

    print("\nDetected FFT Peaks:")
    print("----------------------------------------")
    print("Freq [Hz]    Amplitude    RMS")
    print("----------------------------------------")

    for p in peaks:
        print(f"{freqs[p]:8.2f}    {amp[p]:10.4f}    {rms[p]:10.4f}")

    # PLOTTING
    plt.figure(figsize=(10,6))

    plt.subplot(2,1,1)
    plt.plot(freqs, amp)
    plt.plot(freqs[peaks], amp[peaks], "ro")
    plt.title("FFT Amplitude Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel(name+" "+units)
    plt.grid()
    plt.xlim(0, freq_max_plot)
    plt.title(title)

    plt.subplot(2,1,2)
    plt.plot(t, x)
    plt.title("signal" )
    plt.xlabel("time [s]")
    plt.ylabel(name+" "+units)
    plt.grid()
    plt.title(title)

    plt.tight_layout()
    plt.show()

    return freqs, amp, peaks
