import random
from math import pow


def prime_little_fermat_theorem(n, k: int = 100):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    if k > n - 3:
        k = n - 3

    for _ in random.sample(range(2, n-1), k):
        a = power_binary_list(_, n - 1, n)
        if a != 1:
            return False
    return True


def power_binary_list(x, k, n):
    temp_list = list(reversed([int(i) for i in list('{0:0b}'.format(k))]))
    y = 1
    i = len(temp_list) - 1
    while i >= 0:
        y = ( y ** 2 ) % n
        if temp_list[i] == 1:
            y = (y * x) % n
        i = i - 1
    return y


def generate_random_odd(k: int):
    result = 0
    for i in range(k):
        if random.randint(0, 1) == 1:
            result += 2 ** i
    return result + 1 if result % 2 == 0 else result


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while not prime_little_fermat_theorem(key):
        key = random.randint(pow(10, 20), q)
    return key


# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c


# Asymmetric encryption
def encrypt(message, q, h, g):
    message_encoded = []

    k = gen_key(q)  # Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(message)):
        message_encoded.append(message[i])

    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(message_encoded)):
        message_encoded[i] = s * ord(message_encoded[i])

    return message_encoded, p


def decrypt(message_encoded, p, key, q):
    message_decoded = []
    h = power(p, key, q)
    for i in range(0, len(message_encoded)):
        message_decoded.append(chr(int(message_encoded[i] / h)))
    return message_decoded


if __name__ == '__main__':
    message = 'encryption'
    print("Original Message :", message)

    # a = random.randint(2, 10)
    q = generate_random_odd(1024)
    g = random.randint(2, q)

    key = gen_key(q)  # Private key for receiver

    print(key)

    h = power(g, key, q)
    print("g used : ", g)
    print("g^a used : ", h)

    message_encoded, p = encrypt(message, q, h, g)
    message_direct = decrypt(message_encoded, p, key, q)
    dmessage = ''.join(message_direct)
    print("Decrypted Message :", dmessage)
