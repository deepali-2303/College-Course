import sounddevice as sd
import numpy as np
import wavio


duration = 10
fs = 8000  


audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()


filename = 'rec.wav'

wavio.write(filename, audio_data, fs, sampwidth=2)
print(len(audio_data))
print(f'Audio recorded and saved as {filename}')
