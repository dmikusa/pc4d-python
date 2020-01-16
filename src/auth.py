#!/usr/bin/env python3
#
# Use symetric encryption to create a digest for a value
#
import sys
import libnacl.utils


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} plaintext".format(sys.argv[0]))
        print("    plaintext: unencrypted data")
        sys.exit(1)

    # message must be of type bytes, not str, so we convert
    message = sys.argv[1].encode()

    # create a key
    key = libnacl.utils.salsa_key()

    # no convenience methods for this, so we use the raw wrapper methods
    digest = libnacl.crypto_auth(message, key)

    print("Key: {}".format(key.hex()))
    print("Digest: {}".format(digest.hex()))
    print()
    print("Verify with: python src/verify.py {} {} {!r}".format(
          key.hex(), digest.hex(), message.decode('utf-8')))
    print()
