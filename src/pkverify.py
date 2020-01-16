#!/usr/bin/env python3
#
# Use public key crypto to verify a message
#
import sys
import libnacl
import libnacl.utils
from base64 import b64decode

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: {} publicKey signedMessage".format(sys.argv[0]))
        print("    publicKey: hex-encoded public key")
        print("    signedMessage: base64-encoded signed message")
        sys.exit(1)

    # load the verifier/public key, `libnacl.sign.Verifier` expects this
    #  to be a public key in hex format
    sender_pub_key = sys.argv[1]

    # signed message
    signed_message = b64decode(sys.argv[2].encode())

    # generate a verifier from the public key
    verifier = libnacl.sign.Verifier(sender_pub_key)

    # sign the message
    try:
        verifier.verify(signed_message)
        print("Verified")
    except ValueError:
        print("NOT verified")
