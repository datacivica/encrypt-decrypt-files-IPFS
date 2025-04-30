#!/usr/bin/env python
"""
Author: Basem Hamza <basem.hamza@datacivica.org>

"""

# TODO: Add encrytion class to the code
# TODO: Add multi files handler
# TODO: Make a registry option for tow option encrypt decrypt
# TODO: Make doc for the cli script

import argparse
import os

from decrypt_class import DecryptFile

YELLOW = "\033[93m"
NEON_GREEN = "\033[92m"
RESET_COLOR = "\033[0m"


def main(arguments):
    if arguments.e:
        print(
            """encryption not done yet you can remove
        the flag -e to decrypt for now"""
        )
    else:

        if not os.path.exists(arguments.input):
            os.mkdir(arguments.input)

        if not os.path.exists(arguments.output):
            os.mkdir(arguments.output)

        decrypt = DecryptFile(
            ipfs_url=arguments.ipfs_url,
            key_path=arguments.secret,
            input_path=arguments.input,
            output_path=arguments.output,
        )
        decrypt.main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "-e",
        action="store_true",
        help=f"{NEON_GREEN}Flag for encryption default decryption" + RESET_COLOR,
    )
    parser.add_argument(
        "-u",
        "--ipfs_url",
        required=True,
        help=f"{NEON_GREEN}URL to encrypted file in IPFS" + RESET_COLOR,
    )
    parser.add_argument(
        "-s",
        "--secret",
        required=True,
        help=f"{NEON_GREEN}PATH of secret key file ex: secret.key" + RESET_COLOR,
    )
    parser.add_argument(
        "-i",
        "--input",
        required=False,
        help=f"{NEON_GREEN}PATH where you want to save the encrypted file default input"
        + RESET_COLOR,
        default="input",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        help=f"{NEON_GREEN}PATH where you want to save the decrypted file default output"
        + RESET_COLOR,
        default="output",
    )

    args = parser.parse_args()
    main(args)
