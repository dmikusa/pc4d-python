#!/usr/bin/env python3
#
# Use symetric encryption to encrypt a value
#
import sys
import nacl.secret
import nacl.utils
from base64 import b64encode


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} plaintext\n\tplaintext: unencrypted data\n"
              .format(sys.argv[0]))
        sys.exit(1)

    # generate a key to use
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

    # message must be of type bytes, not str, so we convert
    message = sys.argv[1].encode()

    # we are making a nonce here, but if we just omit this,
    #  a random nonce will be created
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)

    # create a box from our key & encrypt the message
    box = nacl.secret.SecretBox(key)
    encrypted = box.encrypt(message, nonce)

    print("Nonce: {}".format(nonce.hex()))
    print("Key: {}".format(key.hex()))
    print("Box: {}".format(b64encode(encrypted).decode("utf-8")))
    print()
    print("Decrypt with: python src/decrypt.py {} {}".format(key.hex(),
          b64encode(encrypted).decode("utf-8")))
    print()
