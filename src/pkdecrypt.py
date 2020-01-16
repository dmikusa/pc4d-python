#!/usr/bin/env python3
#
# Use public key encryption to encrypt a file
#
import sys
import libnacl
import libnacl.utils
from base64 import b64decode

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} senderPublicKey recipientPrivateKey box")
        print("    senderPublicKey: base-64 encoded public key")
        print("    recipientPrivateKey: base64-encoded private key")
        print("    box: base64 encoded encrypted data")
        sys.exit(1)

    # load the sender public key
    sender_pub_key = libnacl.public.PublicKey(b64decode(sys.argv[1]))

    # load the receiver private key
    receiver_private_key = libnacl.public.SecretKey(b64decode(sys.argv[2]))

    # load the encrypted bytes
    encrypted = b64decode(sys.argv[3])

    # create a box with sender's secret key & receiver's public key
    receiver_box = libnacl.public.Box(receiver_private_key, sender_pub_key)

    # pull out the nonce, just to print it, this happens automatically when
    #  we decrypt
    print("Nonce: {}".format(encrypted[:libnacl.crypto_box_NONCEBYTES].hex()))

    # decrypt & print or catch the error and log failure
    try:
        decrypted = receiver_box.decrypt(encrypted)
        print("Message: {}".format(decrypted.decode('utf-8')))
    except (libnacl.CryptError, ValueError) as e:
        print("Decryption failed: {}".format(e))
