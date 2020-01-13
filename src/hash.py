#!/usr/bin/env python3
#
# Hash a message
#
import sys
import hashlib


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} message".format(sys.argv[0]))
        print("    message: message to hash")
        sys.exit(1)

    message = sys.argv[1].encode("utf-8")

    # also supported (Python 3.7+):
    #
    # - sha224
    # - md5
    # - sha1
    # - sha3_256
    # - sha256
    # - blake2b
    # - sha3_384
    # - blake2s
    # - sha3_224
    # - sha512
    # - shake_128
    # - sha3_512
    # - sha384
    # - shake_256
    #
    # or look at `hashlib.algorithms_available` to see exactly what
    #  is supported by your version of Python
    digest = hashlib.shake_256(message)

    # `hexdigest` only requires a parameter for `shake_128` and `shake_256`
    hexdigest = digest.hexdigest(64)

    print("Hash: {}".format(hexdigest))
