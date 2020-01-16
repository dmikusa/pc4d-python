#!/usr/bin/env python3
#
# Use symetric encryption to validate a digest for a value
#
import sys
import libnacl
import libnacl.utils


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} key digest message".format(sys.argv[0]))
        print("    key: the key in hex format")
        print("    digest: the digest in hex format")
        print("    message: unencrypted data")
        sys.exit(1)

    # load the key
    key = bytes.fromhex(sys.argv[1])

    # load the digest
    digest = bytes.fromhex(sys.argv[2])

    # message must be of type bytes, not str, so we convert
    message = sys.argv[3].encode()

    # no convenience methods for this, so we use the raw wrapper methods
    try:
        libnacl.crypto_auth_verify(digest, message, key)
        print("Verified")
    except ValueError:
        print("NOT verified")
