from encryption import encrypt_content, decrypt_content

# Read the file we want to encrypt
file = open('ENCRYPT_ME.txt', 'r')
raw_content = file.read()

print('> Encrypting...')
encrypted_content = encrypt_content(raw_content)

print('> Encrypted file content:')
print(encrypted_content)

print('------------------------------------')
print('> Decrypting...')
decrypted_content = decrypt_content(encrypted_content)

print('> Decrypted file content:')
print(decrypted_content)
