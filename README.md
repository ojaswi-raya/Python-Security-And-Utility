# Python Security Utility

## Description

The **Python Security Utility** is a collection of Python tools designed to enhance your security and provide various utilities. This project includes the following features:
- **Password Generator**: Create strong, random passwords.
- **Password Manager**: Securely store and manage passwords with encryption.
- **Port Scanner**: Scan a given IP address for open ports.
- **Cryptography Cipher**: Encrypt and decrypt messages using a Caesar Cipher.
- **WHOIS Lookup**: Retrieve WHOIS information for a domain.

## Features

- **Password Generator**: Generate random passwords with customizable length and character types.
- **Password Manager**: Encrypt and store passwords, and decrypt them when needed.
- **Port Scanner**: Check which ports are open on a specified IP address.
- **Cryptography Cipher**: Use Caesar Cipher for simple encryption and decryption.
- **WHOIS Lookup**: Get domain registration details.

## Installation

To get started with the **Python Security Utility**, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone 
    ```

2. **Navigate to the project directory:**

    ```bash
    cd python-security-utility
    ```

3. **Install the required packages:**

    ```bash
    pip install cryptography whois
    ```

4. **Run the main script:**

    ```bash
    python appp.py
    ```

## Usage

1. **Password Generator**: Select the option to generate a password. Customize the length and character types according to your needs.

2. **Password Manager**: Choose the option to store or retrieve passwords. Passwords are encrypted for security.

3. **Port Scanner**: Enter the IP address you wish to scan and the range of ports. The scanner will display open ports.

4. **Cryptography Cipher**: Encrypt or decrypt a message using Caesar Cipher. Provide the message and shift value as required.

5. **WHOIS Lookup**: Enter the domain you want to look up to get registration information.

## Example

Here's a quick example of how to use each tool:

- **Password Generator**: Generate a 12-character password including letters, numbers, and symbols.
- **Password Manager**: Store a password with a label and retrieve it later.
- **Port Scanner**: Scan IP `192.168.1.1` for ports in the range `1-1024`.
- **Cryptography Cipher**: Encrypt "hello" with a shift of 3.
- **WHOIS Lookup**: Get WHOIS information for `example.com`.
