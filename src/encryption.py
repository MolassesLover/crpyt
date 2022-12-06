#!/bin/python3

# region Modules

import argparse
import colorama
from colorama import Fore, Style
import glob
import os
import subprocess
from pathlib import Path
import shutil
import sys

# endregion

# region Variables

decryptionCount: int = 0
encryptionCount: int = 0

# endregion

# region Functions


def decrypt(file, deleteOriginal: bool):
    global decryptionCount

    if file.endswith(".gpg"):
        if os.path.isfile(file):
            print(f":: {Fore.BLUE}Decrypting {Fore.YELLOW}{file}{Fore.RESET}")
            subprocess.run(
                f"gpg --decrypt {file} > {file.removesuffix('.gpg')}", shell=True
            )

            decryptionCount += int(1)

    elif file.endswith(".asc"):
        if os.path.isfile(file):
            print(f":: {Fore.BLUE}Decrypting {Fore.YELLOW}{file}{Fore.RESET}")
            subprocess.run(
                f"gpg --decrypt {file} > {file.removesuffix('.asc')}", shell=True
            )

            decryptionCount += int(1)

    if deleteOriginal is True:
        if file.endswith(".asc"):
            if os.path.isfile(file):
                print(f":: {Fore.RED}Deleting {Fore.YELLOW}{file}{Fore.RESET}")
                os.remove(file)
        elif file.endswith(".gpg"):
            if os.path.isfile(file):
                print(f":: {Fore.RED}Deleting {Fore.YELLOW}{file}{Fore.RESET}")
                os.remove(file)


def encrypt(file, deleteOriginal: bool, key: str, deleteDuplicates: bool = True):
    # Clean directories
    if os.path.isdir("__pycache__"):
        shutil.rmtree("__pycache__")

    if file.endswith(".asc"):
        return
    elif file.endswith(".gpg"):
        return

    global encryptionCount

    print(f":: {Fore.GREEN}Encrypting {Fore.YELLOW}{file}{Fore.RESET}")

    if os.path.isfile(file):
        subprocess.run(
            f"gpg --encrypt --sign --cipher-algo AES256 --compress-algo zlib -r {key} {file}",
            shell=True,
        )
        encryptionCount += int(1)

    if deleteOriginal is True:
        if os.path.isfile(file):
            os.remove(file)


def main():
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("--encrypt", action="store_true")
    argumentParser.add_argument("--decrypt", action="store_true")
    argumentParser.add_argument("--delete_original", action="store_true")
    argumentParser.add_argument("--force", action="store_true")
    argumentParser.add_argument("--key", type=str)
    argumentParser.add_argument("--path", type=str)
    arguments = argumentParser.parse_args()

    workingDirectory = os.getcwd()

    if not arguments.path:
        targetDirectory: str = workingDirectory
    else:
        targetDirectory: str = arguments.path

    print(
        f":: Using the path '{Fore.YELLOW}{os.path.abspath(targetDirectory)}{Fore.RESET}'"
    )

    if not arguments.key:
        print(f":: {Fore.RED}Error{Fore.RESET}: No GPG key provided.")
        sys.exit(1)

    if arguments.force is not True:
        if os.path.abspath(targetDirectory) == os.environ["HOME"]:
            print(
                f":: {Fore.RED}Error{Fore.RESET}: Encrypting the home directory is disabled."
            )
            print(
                f":: {Fore.BLUE}Help{Fore.RESET}: Use the {Fore.YELLOW}--force{Fore.RESET} flag to enable it."
            )
            sys.exit(1)

    if arguments.encrypt:
        for filepath in glob.iglob(f"{targetDirectory}/**/**", recursive=True):
            if os.path.isfile(filepath):
                encrypt(
                    filepath,
                    deleteOriginal=arguments.delete_original,
                    key=arguments.key,
                )
        if encryptionCount == 1:
            print(f":: {Style.DIM}Encrypted {encryptionCount} file.{Style.RESET_ALL}")
        else:
            print(f":: {Style.DIM}Encrypted {encryptionCount} files.{Style.RESET_ALL}")

    elif arguments.decrypt:
        for filepath in glob.iglob("*/**", recursive=True):
            if os.path.isfile(filepath):
                decrypt(filepath, deleteOriginal=arguments.delete_original)
        if decryptionCount == 1:
            print(f":: {Style.DIM}Decrypted {decryptionCount} file.{Style.RESET_ALL}")
        else:
            print(f":: {Style.DIM}Decrypted {decryptionCount} files.{Style.RESET_ALL}")


# endregion

if __name__ == "__main__":
    main()
