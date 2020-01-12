#!/usr/bin/env python3
#
# Hash a message
#
import sys
import nacl.hash


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} message".format(sys.argv[0]))
        print("    message: message to hash")
        sys.exit(1)

    message = sys.argv[1].encode("utf-8")

    # also supported:
    #  - nacl.hash.sha512
    #  - nacl.hash.blake2b
    digest = nacl.hash.sha256(message)

    print("Hash: {}".format(digest.decode()))
