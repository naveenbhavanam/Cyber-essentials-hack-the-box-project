import numpy as np
from scipy.fftpack import fft
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# Step 1: Load the encrypted WAV file
rate, data = read("encrypted.wav")

# Step 2: Perform FFT on the data
frequencies = np.abs(fft(data))  # Compute the magnitude of the FFT

# Step 3: Plot the frequency spectrum
plt.figure(figsize=(10, 6))
plt.plot(frequencies[:5000])  # Plot the first 5000 frequency components
plt.title("Frequency Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Amplitude")
plt.show()

# Step 4: Identify dominant frequencies
# Find the indices of the 10 most significant frequencies
dominant_indices = np.argsort(-frequencies)[:10]  # Top 10 frequencies
dominant_amplitudes = frequencies[dominant_indices]  # Get their amplitudes

# Print the results
print("Dominant Frequencies (Indices):", dominant_indices)
print("Corresponding Amplitudes:", dominant_amplitudes)
