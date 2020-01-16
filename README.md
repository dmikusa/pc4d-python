# Practical Cryptography for Developers (in Python)

This repository contains examples of how to use various Python libraries to perform cryptographic operations safely and with purpose.

The primary purposes of cryptography are:

- Confidentiality
- Integrity
- Non-repudiation
- Authentication

The examples in this repository depend on the [libnacl: Python bindings to NaCl](https://libnacl.readthedocs.io/en/latest/) packages.

This is inspired by [aeden/pc4d-go](https://github.com/aeden/pc4d-go) & [aeden/pc4d-ruby](https://github.com/aeden/pc4d-ruby).

## Examples

To run the examples...

- Install Python 3, preferrably Python 3.7+.
- Install libsodium. Your package manager can likely do this for you. For example, `brew install libsodium` or `apt install libsodium23`.
- Optional: run `python -m venv ./env`. This will create a virtual env. Then run `./env/bin/activate` to activate the virtual env. This prevents polluting your global Python library.
- Run `pip install -r requirements.txt` from the project directory to install dependencies.

You should now be able to run the examples, for example `python src/encrypt.py`, or try running `./test.sh` which runs all four examples and validates they are working correctly.

### Confidentiality

Symmetric examples: `encrypt.py` & `decrypt.py`

Asymmetric examples: `pkencrypt.py` & `pkdecrypt.py`

Run either `encrypt.py` or `pkencrypt.py` with the appropriate arguments and the final output should show the command required to decrypt.

### Integrity

Hash example: `hash.py`

Run `hash.py` with the same input argument and you should get the same output argument every time.

Asymmetric example: `pksign.py` & `pkverify.py`

Run `pksign.py` with the appropriate arguments and the final output should show the command required to verify.

### Non-repudiation

Asymmetric examples: `pksign.py` & `pkverify.py`

Run `pksign.py` with the appropriate arguments and the final output should show the command required to verify.

### Authentication

Symmetric example: `auth.py` & `verify.py`

Run `auth.py` with the appropriate arguments and the final output should show the command required to verify.
