"""
Author: Basem Hamza <basem.hamza@datacivica.org>

"""

# TODO:  Make semaphores to handle more files at the same time

import asyncio
import os
import time
from urllib.parse import urlparse

import aiofiles
import aiohttp
from cryptography.fernet import Fernet


class DecryptFile:
    """

    Parse the URL to extract the filename
    Make an asynchronous HTTP request
    Write the content to a file asynchronously
    Load the key
    Read the data from the encrypted file
    Write the decrypted data

    """

    def __init__(self, ipfs_url, key_path, input_path, output_path):

        self.key_path = key_path
        self.input_path = input_path
        self.output_path = output_path
        self.ipfs_url = ipfs_url
        self.filename = ""

    async def decrypt_file(self):
        """
        Load the key
        Read the data from the encrypted file
        Write the decrypted data
        """
        start_time = time.time()
        async with aiofiles.open(self.key_path, "rb") as key_file:
            key = await key_file.read()

        cipher_suite = Fernet(key)

        async with aiofiles.open(self.input_path, "rb") as file:
            file_data = await file.read()

        decrypt_data = cipher_suite.decrypt(file_data)
        output_path_file = (
            f"{self.output_path}/{self.filename.replace('.encrypted', "")}"
        )
        async with aiofiles.open(output_path_file, "wb") as file:
            await file.write(decrypt_data)
        elapsed_time = time.time() - start_time
        return print(f"Decrypt from ipfs took {elapsed_time:.2f} seconds")

    async def fetch_from_ipfs(self):
        """
        Parse the URL to extract the filename
        Make an asynchronous HTTP request
        Write the content to a file asynchronously
        """

        start_time = time.time()
        parsed_url = urlparse(self.ipfs_url)
        self.filename = os.path.basename(parsed_url.path)
        path_file = os.path.join(self.input_path, self.filename)
        async with aiohttp.ClientSession() as session:
            async with session.get(self.ipfs_url) as response:
                if response.status == 200:
                    with open(path_file, "wb") as file:
                        file.write(await response.read())
                    print(f"Data saved to {path_file}")
                    self.input_path = path_file
                    await self.decrypt_file()
                    elapsed_time = time.time() - start_time
                    print(f"Fetch from ipfs took {elapsed_time:.2f} seconds")
                else:
                    print(
                        f"""Failed to retrieve data.
                    Status code: {response.status}"""
                    )

    def main(self):
        """
        Run async functions
        """
        asyncio.run(self.fetch_from_ipfs())
