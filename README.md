# PRODIGY_CS_02
# PixCrypt

PixCrypt is a simple image encryption tool using pixel manipulation developed for Kali Linux. The tool allows users to encrypt and decrypt images by performing basic mathematical operations on each pixel value.

## Features
- Encrypt images by manipulating pixel values.
- Decrypt images using the same key to restore the original image.
- Supports various image formats including .jpg, .png, .bmp, .gif, and others.
- Supports different mathematical operations: addition, subtraction, multiplication, division, and XOR.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Requirements
- Python 3
- Pillow library

## Installation
1. **Install Python 3**: Ensure you have Python 3 installed. You can check this by running:
   ```bash
   python3 --version
   ```
2. **Install Pillow**: Install the Pillow library using pip:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install pillow
   ```

## Usage
PixCrypt uses a command-line interface to encrypt and decrypt images.
```plaintext
 python3 pixcrypt.py -h
usage: pixcrypt.py [-h] {encrypt,decrypt} ...

PixCrypt: A simple image encryption tool using pixel manipulation.

positional arguments:
  {encrypt,decrypt}  Sub-commands:
    encrypt          Encrypt an image
    decrypt          Decrypt an image

options:
  -h, --help         show this help message and exit

Example usage:
  python3 pixcrypt.py encrypt input.jpg encrypted.png 100 add
  python3 pixcrypt.py encrypt <input_path> <output_path> <key> <operation>
  python3 pixcrypt.py decrypt <input_path> <output_path> <key> <operation>
```
### Example
```bash
python3 pixcrypt.py encrypt input.jpg encrypted.png 100 add
python3 pixcrypt.py decrypt encrypted.png decrypted.jpg 100 add
```
