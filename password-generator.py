import base64
from hashlib import pbkdf2_hmac
from sys import argv
from os import urandom


def generate(password):
    salt = urandom(16)
    password = base64.b64decode(password)
    key = pbkdf2_hmac('sha512', password, salt, 100000, 64)
    return base64.b64encode(salt).decode() + ":" + base64.b64encode(key).decode()


if __name__ == "__main__":
    print(generate(argv[1]))
