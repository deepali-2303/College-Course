import numpy as np
import soundfile as sf

def calculate_fft(x):
    N = len(x)
    X = np.fft.fft(x)
    return X

def correlation(x, y):
    coeff = 0
    if len(x) == len(y):
        sumXY = sum((x - x.mean()) * (y - y.mean()))
        sumXSquared = sum((x - x.mean()) ** 2)
        sumYSquared = sum((y - y.mean()) ** 2)
        coeff = sumXY / np.sqrt(sumXSquared * sumYSquared)
    return coeff

x, sample_rate_x = sf.read('Recording_101.wav')
y, sample_rate_y = sf.read('Recording_102.wav')

X = calculate_fft(x)
Y = calculate_fft(y)

X_magnitude_squared = np.abs(X)**2
Y_magnitude_squared = np.abs(Y)**2

r = correlation(X_magnitude_squared, Y_magnitude_squared)

threshold = 0.9

if r > threshold:
    print("User Authenticated")
else:
    print("Authentication Failed")
print(r)