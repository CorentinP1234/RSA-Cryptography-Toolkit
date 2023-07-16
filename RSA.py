from sympy.ntheory import totient
class RSA:
    """Class for RSA operations."""

    def __init__(self):
        """Initialize with the necessary attributes."""
        self.n = None
        self.e = None
        self.d = None

    @staticmethod
    def extended_gcd(a, b):
        """Return the greatest common divisor of a and b using the Extended Euclidean algorithm."""
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = RSA.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    @staticmethod
    def is_coprime(a, b):
        """Check if two numbers are coprime."""
        g, _, _ = RSA.extended_gcd(a, b)
        return g == 1

    def compute_totient(self, n):
        """Calculate the Euler's Totient function (phi) of a number."""
        self.n = n
        totient_val = totient(self.n)
        return totient_val

    def validate_e(self, e, n):
        """Validate if e and phi are coprime."""
        self.e = e
        self.n = n
        totient_val = self.compute_totient(self.n)
        return self.is_coprime(totient_val, self.e)

    def mod_inverse(self, e, phi):
        """Calculate the modular inverse."""
        d_old, r_old = 0, phi
        d_new, r_new = 1, e
        while r_new > 0:
            a = r_old // r_new
            d_old, d_new = d_new, d_old - a * d_new
            r_old, r_new = r_new, r_old - a * r_new
        return d_old % phi if r_old == 1 else None

    def encrypt(self, m, n, e):
        """Encrypt using RSA."""
        self.n = n
        self.e = e
        cyphertext = pow(m, self.e, self.n)
        return cyphertext

    def decrypt(self, c, n, d):
        """Decrypt using RSA."""
        self.n = n
        self.d = int(d)
        plaintext = pow(c, self.d, self.n)
        return plaintext

def main():
    """Main function to handle user interface."""
    rsa = RSA()
    print("Choose a number between 1 and 8:")
    print("1. Check if two numbers are coprime")
    print("2. Compute phi(n)")
    print("3. Validate e given phi(n)")
    print("4. Compute d given e and phi(n)")
    print("5. Compute (phi, d) given n and e")
    print("6. Compute (phi, e) given n and d")
    print("7. Encrypt")
    print("8. Decrypt")
    selection = input()
    if selection == '1':
        rsa.check_coprime_ui()
    elif selection == '2':
        rsa.compute_totient_ui()
    elif selection == '3':
        rsa.validate_e_ui()
    elif selection == '4':
        rsa.find_d()
    elif selection == '5':
        rsa.compute_phi_d()
    elif selection == '6':
        rsa.compute_phi_e()
    elif selection == '7':
        rsa.encrypt()
    elif selection == '8':
        rsa.decrypt()

if __name__ == "__main__":
    main()
