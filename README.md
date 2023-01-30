# Cr**py**t
> Pronounced 'crypt.'

[![Ko-Fi](https://img.shields.io/badge/donate-kofi-blue?style=for-the-badge&logo=ko-fi&color=e57578&logoColor=FFFFFF&labelColor=262a35)](https://ko-fi.com/molasses)
[![Patreon](https://img.shields.io/badge/donate-patreon-blue?style=for-the-badge&logo=patreon&color=e57578&logoColor=FFFFFF&labelColor=262a35)](https://www.patreon.com/molasseslover)
[![PyPi](https://img.shields.io/badge/install-pypi-blue?style=for-the-badge&logo=python&color=e57578&logoColor=FFFFFF&labelColor=262a35)](https://pypi.org/project/crpyt)

A very simple Python script that calls Shell, allowing you
to encrypt files within a tree using GPG. The script is
hardcoded to encrypt files with 256 bit [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).

## Usage

In this example, the [`test/`](https://github.com/MolassesLover/Crpyt/tree/master/test) directory is **encrypted**, leaving only the `.gpg` files:
```sh
➜ python3 src/cli.py --path test --encrypt --delete_original --key #$MY_GPG_KEY
# Encrypting pets/dogs/inu.txt
# Encrypting pets/cats/neko.txt
# Encrypted 2 files.
```

Then the tree is **decrypted**, removing the `.gpg` files:
```sh
➜ python3 src/cli.py --path test --decrypt --delete_original --key #$MY_GPG_KEY
# Decrypting pets/dogs/inu.txt.gpg
# Deleting pets/dogs/inu.txt.gpg
# Decrypting pets/cats/neko.txt.gpg
# Deleting pets/cats/neko.txt.gpg
# Decrypted 2 files.
```

## Installation

The [`src/cli.py`](https://github.com/MolassesLover/Crpyt/blob/master/src/cli.py) file can be installed as the
`crpyt` command using `pip`.

You can install it from [GitHub](https://github.com/MolassesLover/Crpyt):
```sh
➜ pip install git+https://github.com/MolassesLover/Crpyt.git
```
Alternatively, from [PyPi](https://pypi.org/project/crpyt):
```sh
➜ pip install crpyt
```

## License
All files within this repository are licensed under the 
[Apache v2.0 license](https://github.com/MolassesLover/Crpyt/blob/master/LICENSE-APACHE.md) or 
[MIT license](https://github.com/MolassesLover/Crpyt/blob/master/LICENSE-MIT.md) at your choice. 

## Contributing
Contributions are open, just make sure to sign your
commits, otherwise, your changes will not be merged.
