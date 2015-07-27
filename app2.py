# Hronsfeld cipher

import math

alphabet = "abcdefghijklmnopqrstuvwxyz"

msg = "EXALTATION"
key = "31415"

msg = msg.lower()
times = math.ceil(len(msg)/len(key))
key = (key * times)[:len(msg)]

cipher = []

for i in range(len(msg)):
    char = msg[i]
    shift = int(key[i])
    char_index = alphabet.index(char)
    index = (char_index + shift) % len(alphabet)
    cipher.append(alphabet[index])

encode = ''.join(cipher).upper()

print(encode.upper())

msg = encode.lower()
decipher = []

for i in range(len(msg)):
    char = msg[i]
    shift = int(key[i])
    char_index = alphabet.index(char)
    index = (char_index - shift)
    if index < 0:
        index = len(alphabet) + index
    decipher.append(alphabet[index])

decode = ''.join(decipher).upper()

print(decode.upper())