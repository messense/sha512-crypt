# sha512-crypt

![CI](https://github.com/messense/sha512-crypt/workflows/CI/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/sha512-crypt.svg)](https://pypi.org/project/sha512-crypt)

Python binding to Rust [sha-crypt](https://github.com/RustCrypto/password-hashes/tree/master/sha-crypt) password hashing crate.


## Installation

```bash
pip install sha512-crypt
```

## Usage

```python
import sha512_crypt

password = 'abc'
hashed = sha512_crypt.encrypt(password)
assert sha512_crypt.verify(password, hashed), 'wrong password'
```

## License

This work is released under the MIT license. A copy of the license is provided in the [LICENSE](./LICENSE) file.
