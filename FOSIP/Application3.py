import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def convolve(signal, kernel):
    signal_len = len(signal)
    kernel_len = len(kernel)
    output = np.zeros(signal_len)
    for i in range(signal_len):
        for j in range(kernel_len):
            if i - j >= 0:
                output[i] += signal[i - j] * kernel[j]

    return output

def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X


kernel = np.array([-0.0003, 0.0000, 0.0003, 0.0005, 0.0006, 0.0005, 0.0002, -0.0003, -0.0008, -0.0011, -0.0012, -0.0008, 0.0000, 0.0010, 0.0019, 0.0024, 0.0020, 0.0008, -0.0009, -0.0028, -0.0040, -0.0041, -0.0027, 0.0000, 0.0033, 0.0060, 0.0072, 0.0060, 0.0025, -0.0027, -0.0079, -0.0113, -0.0114, -0.0074, 0.0000, 0.0089, 0.0165, 0.0197, 0.0167, 0.0069, -0.0077, -0.0233, -0.0347, -0.0367, -0.0255, 0.0000, 0.0375, 0.0817, 0.1252, 0.1599, 0.1791, 0.1791, 0.1599, 0.1252, 0.0817, 0.0375, 0.0000, -0.0255, -0.0367, -0.0347, -0.0233, -0.0077, 0.0069, 0.0167, 0.0197, 0.0165, 0.0089, 0.0000, -0.0074, -0.0114, -0.0113, -0.0079, -0.0027, 0.0025, 0.0060, 0.0072, 0.0060, 0.0033, 0.0000, -0.0027, -0.0041, -0.0040, -0.0028, -0.0009, 0.0008, 0.0020, 0.0024, 0.0019, 0.0010, 0.0000, -0.0008, -0.0012, -0.0011, -0.0008, -0.0003, 0.0002, 0.0005, 0.0006, 0.0005, 0.0003, 0.0000, -0.0003])

input_audio, sample_rate = sf.read('input_audio.wav')

denoised_audio = convolve(input_audio, kernel)

denoised_audio = denoised_audio / np.max(np.abs(denoised_audio))


plt.plot(denoised_audio)
plt.title("Audio Signal x[n]")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.show()

X = np.fft.fft(denoised_audio)

magnitude_spectrum = np.abs(X)
plt.plot(magnitude_spectrum)
plt.title("Magnitude Spectrum of X[k]")
plt.xlabel("Frequency Bin")
plt.ylabel("Magnitude")
plt.show()
