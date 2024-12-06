import pyaes, pbkdf2, binascii, os, secrets

# Derive a 256-bit AES encryption key from the password

def aesctr():
    password = "ewo hgoerhgeh th erohoeq3nh493n9hng34q9haergnv9q42n9gwbenr9beiufndxnv"
    print('password:', password)
    passwordSalt = os.urandom(16)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(32) #pdfkbf2 is considered secure !! https://security.stackexchange.com/questions/47183/is-it-safe-to-use-pbkdf2-for-hashing
    print('AES encryption key:', binascii.hexlify(key))

    # Encrypt the plaintext with the given key:
    #   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
    iv = secrets.randbits(256)
    plaintext = "Let's encrypt a message"
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    print('Encrypted:', binascii.hexlify(ciphertext))

    # Decrypt the ciphertext with the given key:
    #   plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(ciphertext)
    print('Decrypted:', decrypted)


