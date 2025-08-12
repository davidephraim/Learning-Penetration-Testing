def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003
n = p * q
phi = (p - 1) * (q - 1)

e = 65537
d = modinv(e, phi)
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423

# Ensure all variables are integers
c, d, n = int(c), int(d), int(n)

# Perform modular exponentiation
plain = pow(c, d, n)
print(plain)

# Convert the numeric result to ASCII
plaintext_ascii = hex(plain)[2:]
plaintext_bytes = bytes.fromhex(plaintext_ascii)
decoded_text = plaintext_bytes.decode('ascii')

print(decoded_text)

