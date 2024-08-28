from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("usb.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as usb_key.key")

if __name__ == "__main__":
    generate_key()
