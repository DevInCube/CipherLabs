# Caesar cipher

shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz".lower()
length = len(alphabet)

msg = "Hello, world!".lower()
encoded_alphabet = ""

for i in range(len(alphabet)):
    index = (i + shift) % len(alphabet)
    encoded_alphabet += alphabet[index]

print(encoded_alphabet)

cipher = ""
for i in range(len(msg)):
    char = msg[i]
    if char in alphabet:
        index = (alphabet.index(char) + shift) % 26
        cipher += alphabet[index]
    else:
        cipher += char

print(cipher)

message = ""
for i in range(len(cipher)):
    char = cipher[i]
    if char in alphabet:
        index = alphabet.index(char)
        index = (index - shift + length) % length
        message += alphabet[index]
    else:
        message += char

print(message)