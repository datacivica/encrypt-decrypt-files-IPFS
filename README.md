# Encrypt Decrypt files IPFS

Python CLI repository for encrypting and decrypting files for IPFS

python version 3.13

## Setup

```bash
python3 -m venv env \
source env/bin/activate
pip3 install -r requirements.txt

```
## change chmod to run the cli 

```bash
chmod +x main.py \
./main.py -h
```

## Example:

```bash
./main.py -u https://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi.ipfs.dweb.link -s secret.key
```

## Usage

```
usage: main.py [-h] [-e] -u IPFS_URL -s SECRET [-i INPUT] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -e                    Flag for encryption default decryption
  -u, --ipfs_url IPFS_URL
                        URL to encrypted file in IPFS
  -s, --secret SECRET   PATH of secret key file ex: secret.key
  -i, --input INPUT     PATH where you want to save the encrypted file default input
  -o, --output OUTPUT   PATH where you want to save the decrypted file default output

```
