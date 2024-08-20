import random
import string
import json
import os
import socket
from concurrent.futures import ThreadPoolExecutor
from cryptography.fernet import Fernet
import whois

# Password Generator
def generate_password(length=12, use_digits=True, use_symbols=True, use_uppercase=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("\nPassword Generator")
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_digits, use_symbols, use_uppercase)
    print(f"Generated password: {password}")

# Password Manager
def load_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    else:
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    return key

def load_passwords(filename, cipher):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    data = cipher.decrypt(encrypted_data).decode('utf-8')
    return json.loads(data)

def save_passwords(filename, passwords, cipher):
    data = json.dumps(passwords).encode('utf-8')
    encrypted_data = cipher.encrypt(data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def password_manager():
    print("\nPassword Manager")
    key = load_key()
    cipher = Fernet(key)
    filename = 'passwords.dat'
    passwords = load_passwords(filename, cipher)

    while True:
        print("\n1. Add new password")
        print("2. View passwords")
        print("3. Back to main menu")
        choice = input("Choose an option: ")

        if choice == '1':
            service = input("Enter the service (e.g., Gmail): ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            passwords[service] = {'username': username, 'password': password}
            save_passwords(filename, passwords, cipher)
            print("Password saved successfully!")
        elif choice == '2':
            for service, creds in passwords.items():
                print(f"Service: {service}\nUsername: {creds['username']}\nPassword: {creds['password']}\n")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Port Scanner
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        return port, result == 0
    except:
        return port, False

def port_scanner():
    print("\nPort Scanner")
    ip = input("Enter the IP address to scan: ")
    port_range = input("Enter port range (e.g., 20-80): ")
    start_port, end_port = map(int, port_range.split('-'))

    print(f"Scanning {ip} from port {start_port} to {end_port}...")

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(ip, p), range(start_port, end_port + 1))

    open_ports = [port for port, is_open in results if is_open]
    
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

# Cryptography Cipher
def caesar_cipher(text, shift, encrypt=True):
    result = []
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    return ''.join(result)

def cryptography_cipher():
    print("\nCryptography Cipher (Caesar Cipher)")
    action = input("Would you like to (E)ncrypt or (D)ecrypt? ").lower()
    text = input("Enter your text: ")
    shift = int(input("Enter the shift value: "))
    encrypt = action == 'e'

    result = caesar_cipher(text, shift, encrypt)
    print(f"Result: {result}")

# WHOIS Lookup
def perform_whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Error: {e}"

def whois_lookup():
    print("\nWHOIS Lookup")
    domain = input("Enter the domain (e.g., example.com): ")
    
    whois_info = perform_whois_lookup(domain)
    print("\nWHOIS Information:")
    for key, value in whois_info.items():
        print(f"{key}: {value}")

# Main Menu
def main():
    while True:
        print("\nMain Menu")
        print("1. Password Generator")
        print("2. Password Manager")
        print("3. Port Scanner")
        print("4. Cryptography Cipher")
        print("5. WHOIS Lookup")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            password_generator()
        elif choice == '2':
            password_manager()
        elif choice == '3':
            port_scanner()
        elif choice == '4':
            cryptography_cipher()
        elif choice == '5':
            whois_lookup()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
