from twofish import Twofish

key = b"ThisIsA32ByteKey_____1234567890"
T = Twofish(key)

plaintext = b"16BytePlaintext!"
ciphertext = T.encrypt(plaintext)
decrypted = T.decrypt(ciphertext)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted.decode())