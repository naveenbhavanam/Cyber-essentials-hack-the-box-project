import numpy as np
from scipy.io.wavfile import read
from scipy.fft import dst

# Step 1: Load the encrypted WAV file
rate, waveform = read("encrypted.wav")

# Step 2: Perform Discrete Sine Transform (DST)
result = dst(waveform)  # Transform to identify significant frequencies

# Step 3: Filter out significant amplitudes (threshold > 10^5)
amplitudes = result[result > 10**5]
amplitudes.sort()  # Sort the amplitudes for processing

# Step 4: Recover characters from amplitudes
recovered = ""
for a in amplitudes:
    # Find the index of the amplitude in the result array
    found = np.where(result == a)[0][0]
    
    # Check if the index is odd (indicates character data)
    if found % 2 == 1:
        c = round(found / 20)  # Approximate ASCII value
        
        # Ensure the value is within ASCII range
        while c > 128:
            c //= 4  # Reduce by dividing by 4
        
        # Append the character to the flag
        recovered += chr(c)

# Step 5: Print the recovered flag
print("Recovered Flag:", recovered)
