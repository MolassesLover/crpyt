import subprocess
import os
from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as readme:
    long_desc = readme.read()

if os.path.exists("src"):
    subprocess.run("mv src crpyt", shell=True)

setup(
    name="crpyt",
    version="0.0.2",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    description="Encrypt files within a tree using GPG",
    author="MolassesLover",
    author_email="60114762+MolassesLover@users.noreply.github.com",
    url="https://github.com/MolassesLover/Crpyt",
    install_requires=["black", "colorama", "SCons"],
    license="MIT",
    entry_points={
        "console_scripts": [
            "crpyt = crpyt.cli:main",
        ]
    },
)

if os.path.exists("crpyt"):
    subprocess.run("mv crpyt src", shell=True)
