from encryption import encrypt_content
from decryption import decrypt_content

print('> Encrypting...')
encrypted_content = encrypt_content()

print('> Encrypted file content:')
print(encrypted_content)

print('------------------------------------')
print('> Decrypting...')
decrypted_content = decrypt_content(encrypted_content)

print('> Decrypted file content:')
print(decrypted_content)
