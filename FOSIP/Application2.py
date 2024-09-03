import numpy as np
import soundfile as sf


def correlation(x, y):
    coeff = 0
    if len(x) == len(y):
        sumXY = sum((x - x.mean()) * (y - y.mean()))
        sumXSquared = sum((x - x.mean()) ** 2)
        sumYSquared = sum((y - y.mean()) ** 2)
        coeff = sumXY / np.sqrt(sumXSquared * sumYSquared)
        
    return coeff


def authenticate_voice(input_audio, stored_audio, threshold):
    correlation_coefficient = correlation(input_audio, stored_audio)

    if correlation_coefficient > threshold:
        return True
    else:
        return False


# Load stored audio file
stored_audio, sample_rate_stored = sf.read('input_audio1.wav')

# Capture real-time audio (You'll need a library like PyAudio for this)
# Replace the following line with the code to capture real-time audio
input_audio, sample_rate_input = sf.read('denoised_audio.wav')

# Define a threshold for correlation coefficient
threshold = 0.9

# Authenticate the voice
if authenticate_voice(input_audio, stored_audio, threshold):
    print("Voice authenticated. Access granted.")
else:
    print("Voice not authenticated. Access denied.")
