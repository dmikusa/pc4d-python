# Practical Cryptography for Developers (in Python)

This repository contains examples of how to use various Python libraries to perform cryptographic operations safely and with purpose. 

The primary purposes of cryptography are:

- Confidentiality
- Integrity
- Non-repudiation
- Authentication

The examples in this repository depend on the [PyNaCl: Python binding to the libsodium library](https://pynacl.readthedocs.io/en/stable/) packages.

This is inspired by [aeden/pc4d-go](https://github.com/aeden/pc4d-go).

## Examples

To run the examples...

- Install Python 3, preferrably Python 3.7+.
- Install libsodium. Your package manager can likely do this for you. For example, `brew install libsodium` or `apt install libsodium23`.
- Run `pip install -r requirements.txt` from the project directory to install dependencies.

You should now be able to run the examples, for example `python src/encrypt.py`.

### Confidentiality

Symmetric examples: `encrypt` & `decrypt`

Asymmetric examples: `pkencrypt` & `pkdecrypt`

Run either `encrypt` or `pkencrypt` with the appropriate arguments and the final output should show the command required to decrypt.

### Integrity

Hash example: `hash`

Run `hash` with the same input argument and you should get the same output argument every time.

Asymmetric example: `pksign` & `pkverify`

Run `pksign` with the appropriate arguments and the final output should show the command required to verify.

### Non-repudiation

Asymmetric examples: `pksign` & `pkverify`

Run `pksign` with the appropriate arguments and the final output should show the command required to verify.

### Authentication

Symmetric example: `auth` & `verify`

Run `auth` with the appropriate arguments and the final output should show the command required to verify.

