import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evmopcodes",
    version="0.0.1",
    author="Tyler Bair",
    author_email="tyler.bair@protonmail.com",
    description="Python EVM opcode programming library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeaBear5/PyEvmOpcodes.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
    ]
)
