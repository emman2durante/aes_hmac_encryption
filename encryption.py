import hashlib
import hmac

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate your own strong password here
# https://passwordsgenerator.net/
SHARED_KEY = 'K3QgSHgHcs7hetbdGsuEBqtsGdNpt8pP7dAWSXnuZ9L6TSWYzQKWmMmzgK4ApKggHEDXYhazs9gLLXUQk4wy2m57kpdNLrs4AqZWYv96De55kqCUwAc4ZgBWbyVY5uqQ'

# We will use file name of the file we want to encrypt
# as the `message` part for creating the hash key
FILENAME = 'ENCRYPT_ME'


def encrypt_content():
    # Read the file we want to encrypt
    file = open(f'{FILENAME}.txt', 'r')
    file_contents = file.read()

    # iv = initialization vector for semantic security
    iv = get_random_bytes(16)

    # Generating our hash key using filename and shared key
    hmac_token = hmac.new(
        SHARED_KEY.encode(),
        FILENAME.encode(),
        hashlib.md5
    ).hexdigest()

    # Create our cipher instance using the 'initialization vector' and 'hash key'
    cipher = AES.new(hmac_token.encode(), AES.MODE_CFB, iv)

    # Encrypt our message using the cipher instance
    # NOTE: we prepend 'iv' so we can recreate our cipher instance when we will decrypt it (see decryption part)
    return iv + cipher.encrypt(str.encode(file_contents))