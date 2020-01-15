#!/usr/bin/env python3
#
# Use symetric encryption to decrypt a value
#
import sys
import libnacl.secret
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
    #  this is purely to print the nonce below
    nonce = encrypted[:libnacl.crypto_secretbox_NONCEBYTES]

    # create a box from our key & decrypt the message
    box = libnacl.secret.SecretBox(key)

    # the nonce is part of `encrypted`, it's the first
    #   `libnacl.crypto_secretbox_NONCEBYTES bytes`.
    #
    # `box.decrypt` can be passed the nonce, but it's smart enough
    #   to automaticaly pull the nonce out so we don't have to.
    #
    #  We could have done, `box.decrypt(encrypted, nonce)`
    #   it would have the same result.
    decrypted = box.decrypt(encrypted)

    print("Nonce: {}".format(nonce.hex()))
    print("Message: {}".format(decrypted.decode()))
