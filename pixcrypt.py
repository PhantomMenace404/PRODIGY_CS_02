import argparse
from PIL import Image
import numpy as np

def apply_operation(array, key, operation):
    if operation == 'add':
        return (array + key) % 256
    elif operation == 'subtract':
        return (array - key) % 256
    elif operation == 'multiply':
        return (array * key) % 256
    elif operation == 'divide':
        # Avoid division by zero
        if key == 0:
            raise ValueError("Key for division cannot be zero.")
        return (array // key) % 256
    elif operation == 'xor':
        return array ^ key
    else:
        raise ValueError(f"Unsupported operation: {operation}")

def encrypt_image(input_path, output_path, key, operation):
    try:
        img = Image.open(input_path)
        img_array = np.array(img)
        encrypted_array = apply_operation(img_array, key, operation)
        encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_img.save(output_path)
        print(f"\033[92m[Success]\033[0m Image encrypted and saved to {output_path}")
    except Exception as e:
        print(f"\033[91m[Error]\033[0m Could not encrypt the image. {e}")

def decrypt_image(input_path, output_path, key, operation):
    try:
        img = Image.open(input_path)
        img_array = np.array(img)
        # For decryption, reverse the operation
        if operation == 'add':
            decrypted_array = apply_operation(img_array, -key, 'add')
        elif operation == 'subtract':
            decrypted_array = apply_operation(img_array, -key, 'subtract')
        elif operation == 'multiply':
            # For multiplication, assuming key is an integer and non-zero
            if key == 0:
                raise ValueError("Key for division cannot be zero.")
            decrypted_array = (img_array * pow(key, -1, 256)) % 256
        elif operation == 'divide':
            if key == 0:
                raise ValueError("Key for division cannot be zero.")
            decrypted_array = (img_array * key) % 256
        elif operation == 'xor':
            decrypted_array = apply_operation(img_array, key, 'xor')
        else:
            raise ValueError(f"Unsupported operation: {operation}")
        decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_img.save(output_path)
        print(f"\033[92m[Success]\033[0m Image decrypted and saved to {output_path}")
    except Exception as e:
        print(f"\033[91m[Error]\033[0m Could not decrypt the image. {e}")

def main():
    parser = argparse.ArgumentParser(
        description="\033[1mPixCrypt\033[0m: A simple image encryption tool using pixel manipulation.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Example usage:
  python3 pixcrypt.py encrypt <input_path> <output_path> <key> <operation>
  python3 pixcrypt.py decrypt <input_path> <output_path> <key> <operation>
"""
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands:")
    
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt an image")
    encrypt_parser.add_argument("input", type=str, help="Path to the input image")
    encrypt_parser.add_argument("output", type=str, help="Path to save the encrypted image")
    encrypt_parser.add_argument("key", type=int, help="Encryption key (integer)")
    encrypt_parser.add_argument("operation", type=str, choices=['add', 'subtract', 'multiply', 'divide', 'xor'], help="Mathematical operation to apply")

    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt an image")
    decrypt_parser.add_argument("input", type=str, help="Path to the encrypted image")
    decrypt_parser.add_argument("output", type=str, help="Path to save the decrypted image")
    decrypt_parser.add_argument("key", type=int, help="Decryption key (same as the encryption key)")
    decrypt_parser.add_argument("operation", type=str, choices=['add', 'subtract', 'multiply', 'divide', 'xor'], help="Mathematical operation to reverse")

    args = parser.parse_args()

    if args.command == "encrypt":
        encrypt_image(args.input, args.output, args.key, args.operation)
    elif args.command == "decrypt":
        decrypt_image(args.input, args.output, args.key, args.operation)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
