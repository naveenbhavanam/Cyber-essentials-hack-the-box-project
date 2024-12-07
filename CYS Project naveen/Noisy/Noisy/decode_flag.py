import numpy as np

# Dominant frequencies extracted from the FFT
dominant_frequencies = [1.99750e+07, 2.50000e+04, 1.99736e+07, 2.64000e+04, 
                        6.60000e+03, 1.45920e+06, 1.85408e+07, 1.38000e+04, 
                        1.99862e+07]

# Encryption parameters from encrypt.py
rate = 20_000_000  # Sampling rate
N = 1_000_000      # Total number of samples

# Decode frequencies to characters
decoded_flag = []
for freq in dominant_frequencies:
    # Reverse frequency calculation to get index (i + 1)
    index = int(freq / (rate / N)) - 1  # Adjust index scaling
    if 32 <= index <= 126:  # Valid ASCII printable range
        decoded_flag.append(chr(index))
    else:
        decoded_flag.append("?")  # Placeholder for invalid characters

# Join characters to form the flag
flag = "".join(decoded_flag)
print("Decoded Flag:", flag)
