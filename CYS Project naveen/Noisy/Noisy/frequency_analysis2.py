import numpy as np
from scipy.fftpack import fft
from scipy.io.wavfile import read

# Step 1: Load the encrypted WAV file
rate, data = read("encrypted.wav")

# Step 2: Perform FFT on the data
frequencies = np.abs(fft(data))

# Step 3: Extract dominant frequencies
# Find the indices of the 10 most significant frequencies
dominant_indices = np.argsort(-frequencies)[:10]  # Top 10 frequencies
dominant_amplitudes = frequencies[dominant_indices]  # Get their amplitudes

# Convert indices to frequencies
dominant_frequencies = dominant_indices * rate / len(data)  # Frequency in Hz

# Print results
print("Dominant Frequencies (Hz):", dominant_frequencies)
print("Corresponding Amplitudes:", dominant_amplitudes)
