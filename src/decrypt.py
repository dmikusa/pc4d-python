#!/usr/bin/env python3
#
# Use symetric encryption to decrypt a value
#
import sys
import nacl.secret
import nacl.utils
from base64 import b64decode


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} key box".format(sys.argv[0]))
        print("    key: hex-encoded 32 byte key")
        print("    box: base64 encoded encrypted data")
        sys.exit(1)

    # load the key
    key = bytes.fromhex(sys.argv[1])

    # load the encrypted bytes
    encrypted = b64decode(sys.argv[2].encode())

    # pull the nonce out, it's the first chunk of the encrypted bytes
    nonce = encrypted[:nacl.secret.SecretBox.NONCE_SIZE]

    # create a box from our key & decrypt the message
    box = nacl.secret.SecretBox(key)
    decrypted = box.decrypt(
        encrypted[nacl.secret.SecretBox.NONCE_SIZE:], nonce)

    print("Nonce: {}".format(nonce.hex()))
    print("Message: {}".format(decrypted.decode()))
