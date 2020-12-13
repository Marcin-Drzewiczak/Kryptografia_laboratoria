import random
import time
import math


#1
def generate_random_with_bits(bits):
    number = 0
    for i in range(bits):
        if random.randint(0, 1) == 1:
            number += 2**i
    return number


#2
'''
Zaimplementuj algorytm (funkcję) obliczania odwrotności B grupie Φ(n).
Wykorzystaj Rozszerzony Algorytm Euklidesa.
Dane:n∈N,b∈Φ(n)
Wynik:b−1∈Φ(n)
'''
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        print('Odwrotnosc nie istnieje')
        return

    if y < 0:
        return y + a

    return y


#3
'''
Zaimplementuj algorytm (funkcję) efektywnego potęgowania w zbiorzeZ∗n.
Wykorzystaj algorytm iterowanego podnoszenia do kwadratu.
Dane:n, k∈N,b∈Z∗n
Wynik:bk∈Z∗n
'''
# (a^n)%p
def get_power_optimal(a, n, p):
    res = 1

    a = a % p

    while n > 0:
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2

    return res % p


#4
'''
Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję), który sprawdza czy elementzbioruZ∗pjest resztą kwadratową wZ∗p.
Wykorzystaj twierdzenie Eulera.
Dane:b∈Z∗p
Wynik:Truejeśli b jest resztą kwadratową,False w przeciwnym wypadku.
'''


def is_rest_squared(a, p):
    tmp = get_power_optimal(a, int((p-1) // 2), p)
    if tmp == 1:
        return True
    elif tmp == p - 1:
        return False


#5
"""
Zaimplementuj algorytm (funkcję), który oblicza pierwiastek kwadratowy w ciele F∗p,
gdzie p ≡ 3 (mod 4) jest liczbą pierwszą.
Wykorzystaj twierdzenie Eulera.
Dane:b∈F∗p,b jest resztą kwadratową F∗p
Wynik:a∈F∗p taki, że a2=b.
"""
def find_b(a, p):
    if p % 4 == 3:
        b = 0
        if is_rest_squared(a, p):
            b = get_power_optimal(a, int((p + 1) / 4), p)
            return b, p - b


#6
'''
Zaimplementuj test (funkcję), który sprawdza liczba naturalna n
jest liczbą pierwszą. Wykorzystaj test Fermata
Dane:n∈N
Wynik:True jeśli n jest liczbą pierwszą, False w przeciwnym wypadku.
'''
def is_prime(n, k = 100):

    if n == 1 or n == 4:
        return False
    if n == 2 or n ==3:
        return True

    else:
        for i in range(k):
            a = random.randint(2, n - 2)

            if get_power_optimal(a, n - 1, n) != 1:
                return False
    return True


# ElGamal
def find_prime(bits, k=7):

    while True:
        x = generate_random_with_bits(bits)

        if is_prime(x, k):
            return x


def find_generator(p, q):
    print("Finding generator\nUsed number\np: {0}\nq: {1}".format(p, q))
    checked = []
    while True:
        g = random.randint(2, p-1)
        if g in checked:
            print("G already checked: {0} now is {1}".format(g, time.time()))
            continue
        checked.append(g)
        print("Checking for: {0} now is {1}".format(g, time.time()))

        g = get_power_optimal(g, q, p)

        if g % p != 1:
            return g


def elgamal():
    while True:
        q = find_prime(1024, 3)
        p = 2 * q + 1
        if is_prime(p):
            return p, q


# --- MODUŁ 2 ---

# http://stackoverflow.com/a/14793082/562769
def factorize(n):
    factors = []

    p = 2
    while True:
        while n % p == 0 and n > 0:  # while we can divide by smaller number, do so
            factors.append(p)
            n = n / p
        p += 1  # p is not necessary prime, but n%p == 0 only for prime numbers
        if p > n / p:
            break
    if n > 1:
        factors.append(n)
    return factors


def calculate_legendre(a, p):
    if a >= p or a < 0:
        return calculate_legendre(a % p, p)
    elif a == 0 or a == 1:
        return a
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p - 1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    elif not is_prime(a):
        factors = factorize(a)
        product = 1
        for pi in factors:
            product *= calculate_legendre(pi, p)
        return product
    else:
        if ((p - 1) / 2) % 2 == 0 or ((a - 1) / 2) % 2 == 0:
            return calculate_legendre(p, a)
        else:
            return (-1) * calculate_legendre(p, a)


def generate_random_elliptic_curve(prime_bites):
    p = find_prime(prime_bites, 3)

    while True:
        A = random.randint(0, p-1)
        B = random.randint(0, p-1)

        delta_e = (4 * A ** 3 + 27 * B ** 2) % p

        if delta_e % p != 0:
            break

    return A, B, p


def generate_random_point_on_elliptic_curve(A, B, p):
    while True:
        x = random.randint(0, p-1)
        f_x = (x ** 3 + A * x + B) % p

        if calculate_legendre(f_x, p) != -1:
            break

    y = math.sqrt(f_x) % p
    return x, y


def generate_random_point_on_elliptic_curve_test():
    A = 158710583
    B = 330114178
    p = 374055203
    x = 157667137
    y = math.sqrt((x ** 3 + A * x + B)) % p

    return y


if __name__ == "__main__":
    # print(generate_random_point_on_elliptic_curve(*generate_random_elliptic_curve(30)))

    A = 158710583
    B = 330114178
    p = 374055203

    print(generate_random_point_on_elliptic_curve(A, B, p))
