# Vigenere cipher
import math

alphabet = "abcdefghijklmnopqrstuvwxyz"
length = len(alphabet)
table = [[0 for x in range(length)] for x in range(length)]

for i in range(0, length * 2 - 1):
    if i < length:
        size = i + 1
        char = alphabet[i]
        for j in range(size):
            table[j][i - j] = char
    else:
        dif = i - length + 1
        size = length - dif
        char = alphabet[i - length]
        for j in range(size):
            table[j + dif][i - j - dif] = char

# print(*table, sep='\r\n')

key = "LEMON"
msg = "ATTACKATDAWN"
cipher = []

key = key.lower()
msg = msg.lower()
times = math.ceil(len(msg)/len(key))
key = (key * times)[:len(msg)]

for i in range(len(msg)):
    row = alphabet.index(key[i])
    col = alphabet.index(msg[i])
    # cipher.append(table[row][col])
    cipher.append(alphabet[(row + col) % length])

encode = ''.join(cipher).upper()

print(encode)

decipher = []
msg = encode.lower()

for i in range(len(msg)):
    row = alphabet.index(key[i])
    col = table[row].index(msg[i])
    # decipher.append(alphabet[col])
    c = alphabet.index(msg[i])
    decipher.append(alphabet[(c - row + length) % length])

decode = ''.join(decipher).upper()

print(decode)