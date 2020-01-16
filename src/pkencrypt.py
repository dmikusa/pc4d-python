#!/usr/bin/env python3
#
# Use public key encryption to encrypt a file
#
import sys
import libnacl
import libnacl.utils
from base64 import b64encode

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} plaintext")
        print("    plaintext: unencrypted data")
        sys.exit(1)

    # message must be of type bytes, not str, so we convert
    message = sys.argv[1].encode()

    # generate sender key
    sender = libnacl.public.SecretKey()

    # generate receiver key
    receiver = libnacl.public.SecretKey()

    # create a box with sender's secret key & receiver's public key
    sender_box = libnacl.public.Box(sender.sk, receiver.pk)

    # encrypt
    context = sender_box.encrypt(message)

    print("Sender public key: {}".format(
        b64encode(sender.pk).decode('utf-8')))
    print("Sender private key: {}".format(
        b64encode(sender.sk).decode('utf-8')))
    print("Recipient public key: {}".format(
        b64encode(receiver.pk).decode('utf-8')))
    print("Recipient private key: {}".format(
        b64encode(receiver.sk).decode('utf-8')))
    print("Nonce: {}".format(context[0:libnacl.crypto_box_NONCEBYTES].hex()))
    print("Box: {}".format(b64encode(context).decode('utf-8')))
    print()
    print("Decrypt with: python src/pkdecrypt.py {!r} {!r} {!r}".format(
        b64encode(sender.pk).decode('utf-8'),
        b64encode(receiver.sk).decode('utf-8'),
        b64encode(context).decode('utf-8')))
    print()
