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

# Step 1: Record Audio Password and filter the noise x[n]

# Step 2: Record Test Audio Password and filter the noise y[n]

# Step 3: Load Audio Files
x, sample_rate_x = sf.read('input_audio1.wav')
y, sample_rate_y = sf.read('input_audio.wav')

# Step 4: Calculate X[k] and Y[k] using FFT
X = calculate_fft(x)
Y = calculate_fft(y)

# Step 5: Calculate |X[k]|^2 and |Y[k]|^2
X_magnitude_squared = np.abs(X)**2
Y_magnitude_squared = np.abs(Y)**2

# Step 6: Calculate Coefficient of Correlation of |X[k]|^2 and |Y[k]|^2 ==> r
r = correlation(X_magnitude_squared, Y_magnitude_squared)

# Step 7: Authenticate the user by selecting appropriate Threshold value (Anything > 0.9).
threshold = 0.9
if r > threshold:
    print("User Authenticated")
else:
    print("Authentication Failed")
