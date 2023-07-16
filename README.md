# RSA Python Module

## Description
This Python module includes an implementation of the RSA (Rivest-Shamir-Adleman) algorithm. The RSA algorithm is a widely used public key cryptosystem that allows for secure data transmission.

## Features
- Implements RSA (Rivest-Shamir-Adleman) encryption and decryption
- Checks if two numbers are coprime
- Computes Euler's Totient function (phi)
- Validates if e and phi are coprime
- Computes the modular inverse (private key)
- User-friendly interface to run different functions

## Dependencies
- Python 3.6 or above
- Sympy library

## Installation
1. Make sure Python 3.6 or higher is installed.
2. Install Sympy library if you haven't installed it yet.
```
pip install sympy
```
3. Download the RSA.py file and you're ready to use the module.

## Usage

After running the script, you will be presented with a menu and prompted to make a selection. The options are:
```
Choose a number between 1 and 8:

1. Check if two numbers are coprime
2. Compute phi(n)
3. Validate e given phi(n)
4. Compute d given e and phi(n)
5. Compute (phi, d) given n and e
6. Compute (phi, e) given n and d
7. Encrypt
8. Decrypt
9. Build signature
10. Check signature
```


- If you choose '1', you will be asked to enter two numbers, and the module will check if they are coprime.
- If you choose '2', you will be asked to enter a number n, and the module will compute the Euler's Totient function (phi) of the number.
- If you choose '3', you will be asked to enter the numbers e and n, and the module will validate if e and phi(n) are coprime.
- If you choose '4', you will be asked to enter the numbers e and phi(n), and the module will compute the modular inverse (private key).
- If you choose '5', you will be asked to enter the numbers n and e, and the module will compute both phi(n) and the modular inverse (private key).
- If you choose '6', you will be asked to enter the numbers n and d, and the module will compute both phi(n) and e.
- If you choose '7', you will be asked to enter the numbers m (message), n, and e, and the module will return the encrypted message.
- If you choose '8', you will be asked to enter the numbers c (cyphertext), n, and d, and the module will return the decrypted message.
- If you choose '9', you will be asked to enter the numbers m (message), n, and d, and the module will return the RSA signature for the message.
- If you choose '10', you will be asked to enter the numbers s (signature), n, and e, and the module will check and return the original message if the signature is valid.

## Disclaimer
This module is a simple implementation of the RSA algorithm and should not be used for any kind of secure communication as it does not include any security measures or optimizations typically found in professional-grade cryptographic software.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions, feel free to contact us.
