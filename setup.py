from setuptools import find_packages, setup

setup(
    name="crpyt",
    version="0.0.1",
    packages=find_packages(include=["src", "src.*"]),
    description="Encrypt files within a tree using GPG",
    author="MolassesLover",
    author_email="60114762+MolassesLover@users.noreply.github.com",
    url="https://github.com/MolassesLover/Crpyt",
    install_requires=["black", "colorama", "SCons"],
    license="MIT",
)
