from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# Step 1: Load the encrypted WAV file
rate, data = read("encrypted.wav")

# Step 2: Print details about the audio
print(f"Sample Rate: {rate}")
print(f"Number of Samples: {len(data)}")
print(f"First 10 Samples: {data[:10]}")  # Check a few samples

# Step 3: Plot the waveform
plt.figure(figsize=(10, 6))
plt.plot(data[:10000])  # Plot the first 10,000 samples for visualization
plt.title("Encrypted Waveform")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.show()
