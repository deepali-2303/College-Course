import numpy as np
import soundfile as sf
import sounddevice as sd

def convolve(signal, kernel):
    signal_len = len(signal)
    kernel_len = len(kernel)
    output = np.zeros(signal_len)
    for i in range(signal_len):
        for j in range(kernel_len):
            if i - j >= 0:
                output[i] += signal[i - j] * kernel[j]
    return output

kernel = np.array([-0.0003, 0.0000, 0.0003, 0.0005, 0.0006, 0.0005, 0.0002, -0.0003, -0.0008, -0.0011, -0.0012, -0.0008, 0.0000, 0.0010, 0.0019, 0.0024, 0.0020, 0.0008, -0.0009, -0.0028, -0.0040, -0.0041, -0.0027, 0.0000, 0.0033, 0.0060, 0.0072, 0.0060, 0.0025, -0.0027, -0.0079, -0.0113, -0.0114, -0.0074, 0.0000, 0.0089, 0.0165, 0.0197, 0.0167, 0.0069, -0.0077, -0.0233, -0.0347, -0.0367, -0.0255, 0.0000, 0.0375, 0.0817, 0.1252, 0.1599, 0.1791, 0.1791, 0.1599, 0.1252, 0.0817, 0.0375, 0.0000, -0.0255, -0.0367, -0.0347, -0.0233, -0.0077, 0.0069, 0.0167, 0.0197, 0.0165, 0.0089, 0.0000, -0.0074, -0.0114, -0.0113, -0.0079, -0.0027, 0.0025, 0.0060, 0.0072, 0.0060, 0.0033, 0.0000, -0.0027, -0.0041, -0.0040, -0.0028, -0.0009, 0.0008, 0.0020, 0.0024, 0.0019, 0.0010, 0.0000, -0.0008, -0.0012, -0.0011, -0.0008, -0.0003, 0.0002, 0.0005, 0.0006, 0.0005, 0.0003, 0.0000, -0.0003])


duration = 5
sample_rate = 44100  

print("Please start speaking...")
input_audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
sd.wait()

denoised_audio = convolve(input_audio[:, 0], kernel)
denoised_audio = denoised_audio / np.max(np.abs(denoised_audio))

sf.write('input_audio1.wav', input_audio, sample_rate)

print("Denoising completed and saved to 'input_audio.wav' and 'denoised_audio.wav'")
