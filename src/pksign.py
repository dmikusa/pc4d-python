#!/usr/bin/env python3
#
# Use public key crypto to sign a message
#
import sys
import libnacl.sign
from base64 import b64encode

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} message".format(sys.argv[0]))
        print("    message: message to sign")
        sys.exit(1)

    # message must be of type bytes, not str, so we convert
    message = sys.argv[1].encode()

    # generate signer's keys
    signer = libnacl.sign.Signer()

    # sign the message
    signed = signer.sign(message)

    print("Public Key: {}".format(signer.hex_vk().decode('utf-8')))
    print("Private Key: {}".format(signer.hex_sk().decode('utf-8')))
    print("Signature: {}".format(b64encode(signed).decode('utf-8')))
    print()
    print("Verify with: python src/pkverify.py {} {}".format(
        signer.hex_vk().decode('utf-8'),
        b64encode(signed).decode('utf-8')))
    print()
