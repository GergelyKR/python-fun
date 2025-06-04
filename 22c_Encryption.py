import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter) # get the index of the letter
    cipher_text += key[index] # use the index of the letter to get the encrypted letter

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter) # get the index of the letter
    plain_text += chars[index] # use the index of the letter to get the decrypted letter

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
