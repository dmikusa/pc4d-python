#!/usr/bin/env python3
#
# Use symetric encryption to encrypt a value
#
import sys
import libnacl.secret
from base64 import b64encode


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} plaintext\n\tplaintext: unencrypted data\n"
              .format(sys.argv[0]))
        sys.exit(1)

    # message must be of type bytes, not str, so we convert
    message = sys.argv[1].encode()

    # create a secret box, which automatically creates a nonce & key
    box = libnacl.secret.SecretBox()
    enc_bytes = box.encrypt(message)

    # nonce is the first part of the encrypted data, so we strip it out
    #  this is purely just to print it below
    nonce = enc_bytes[0:libnacl.crypto_secretbox_NONCEBYTES]

    print("Nonce: {}".format(nonce.hex()))
    print("Key: {}".format(box.hex_sk().decode('utf-8')))
    print("Box: {}".format(b64encode(enc_bytes).decode('utf-8')))
    print()
    print("Decrypt with: python src/decrypt.py {} {}".format(
          box.hex_sk().decode('utf-8'),
          b64encode(enc_bytes).decode("utf-8")))
    print()
