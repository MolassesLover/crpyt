# region Modules

from colorama import Fore
import os
import subprocess
import shutil

# endregion

# region Variables

decryptionCount: int = 0
encryptionCount: int = 0
encryptedFileExtensions: str = [".asc", ".gpg"]

# endregion

# region Functions


def decrypt(file, deleteOriginal: bool):
    global encryptedFileExtensions

    def decrypt_subprocess(file, extension: str):
        global decryptionCount

        print(f":: {Fore.BLUE}Decrypting {Fore.YELLOW}{file}{Fore.RESET}")
        subprocess.run(
            f"gpg --decrypt {file} > {file.removesuffix(extension)}", shell=True
        )

        decryptionCount += int(1)

    def decrypt_delete(file):
        global decryptionCount

        print(f":: {Fore.RED}Deleting {Fore.YELLOW}{file}{Fore.RESET}")
        os.remove(file)

    for encryptedFileExtension in encryptedFileExtensions:
        if file.endswith(encryptedFileExtension):
            if os.path.isfile(file):
                decrypt_subprocess(file, encryptedFileExtension)
                if deleteOriginal is True:
                    decrypt_delete(file)


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


# endregion
