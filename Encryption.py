import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"Chars : {chars}")
#print(f"key : {key}")

# ENCRYPT

plain_text = input("Enter a message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original Message : {plain_text}")
print(f"Encrypted Message : {cipher_text}")