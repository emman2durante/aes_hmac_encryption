import hashlib
import hmac

from Crypto.Cipher import AES

# Generate your own strong password here
# https://passwordsgenerator.net/
SHARED_KEY = 'K3QgSHgHcs7hetbdGsuEBqtsGdNpt8pP7dAWSXnuZ9L6TSWYzQKWmMmzgK4ApKggHEDXYhazs9gLLXUQk4wy2m57kpdNLrs4AqZWYv96De55kqCUwAc4ZgBWbyVY5uqQ'

# We will use file name of the file we want to encrypt
# as the `message` part for creating the hash key
FILENAME = 'ENCRYPT_ME'

def decrypt_content(encrypted_content):

    # Get the first 16 bytes (this will be used for recreating our cipher instance)
    iv = encrypted_content[:16]

    # This is the raw encrypted data
    encrypted_data = encrypted_content[16:]

    # Generating our hash key using filename and shared key
    hmac_token = hmac.new(
        SHARED_KEY.encode(),
        FILENAME.encode(),
        hashlib.md5
    ).hexdigest()

    # Create our cipher instance using the 'initialization vector' and 'hash key'
    cipher = AES.new(hmac_token.encode(), AES.MODE_CFB, iv)

    return cipher.decrypt(encrypted_data)