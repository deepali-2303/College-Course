import numpy as np
import matplotlib.pyplot as plt
import librosa

def oam_filter(signal):

    coefficients = np.array([-0.0004, 0.0004, 0.0004, -0.0004, -0.0005, 0.0005, 0.0006, -0.0006, -0.0007, 0.0008, 0.0009, -0.0010, -0.0012, 0.0013, 0.0015, -0.0017, -0.0019, 0.0021, 0.0024, -0.0026, -0.0029, 0.0032, 0.0035, -0.0039, -0.0043, 0.0047, 0.0052, -0.0057, -0.0062, 0.0068, 0.0074, -0.0081, -0.0089, 0.0097, 0.0106, -0.0116, -0.0128, 0.0141, 0.0156, -0.0174, -0.0194, 0.0218, 0.0248, -0.0285, -0.0333, 0.0398, 0.0491, -0.0636, -0.0895, 0.1498, 0.4501, 0.4501, 0.1498, -0.0895, -0.0636, 0.0491, 0.0398, -0.0333, -0.0285, 0.0248, 0.0218, -0.0194, -0.0174, 0.0156, 0.0141, -0.0128, -0.0116, 0.0106, 0.0097, -0.0089, -0.0081, 0.0074, 0.0068, -0.0062, -0.0057, 0.0052, 0.0047, -0.0043, -0.0039, 0.0035, 0.0032, -0.0029, -0.0026, 0.0024, 0.0021, -0.0019, -0.0017, 0.0015, 0.0013, -0.0012, -0.0010, 0.0009, 0.0008, -0.0007, -0.0006, 0.0006, 0.0005, -0.0005, -0.0004, 0.0004, 0.0004, -0.0004])
    filtered_signal = np.zeros_like(signal)
    print(len(filtered_signal))
    # Apply the OAM filter
    for i in range(len(signal)):
        for j in range(len(coefficients)):
            if i - j >= 0:
                filtered_signal[i] += coefficients[j] * signal[i - j]
    
    return filtered_signal
    


def dft(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, signal)

def plot_spectrum(signal, sr, title):
    # Discrete Fourier Transform (DFT)
    Sxx = np.abs(dft(signal))
    f = np.fft.fftfreq(len(Sxx), d=1/sr)
    
    # Plot magnitude spectrum
    plt.plot(f[:len(f)//2], 10 * np.log10(Sxx[:len(Sxx)//2]))
    plt.ylabel('Magnitude [dB]')
    plt.xlabel('Frequency [Hz]')
    plt.title(title)
    plt.grid(True)

def apply_oam_filter(audio_file, block_size=2048):
    # Load audio file
    y, sr = librosa.load(audio_file)
    
    # Apply the OAM filter
    y_filtered = oam_filter(y)

    # Plot magnitude spectrum before and after OAM filter
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plot_spectrum(y[:block_size], sr, 'Magnitude Spectrum Before OAM Filter')

    plt.subplot(1, 2, 2)
    plot_spectrum(y_filtered[:block_size], sr, 'Magnitude Spectrum After OAM Filter')

    plt.tight_layout()
    plt.show()


apply_oam_filter('rec.wav')
