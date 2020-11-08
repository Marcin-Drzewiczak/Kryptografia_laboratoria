"""
Zaimplementuj algorytm (funkcję), który oblicza pierwiastek kwadratowy w ciele F∗p,
gdzie p ≡ 3 (mod 4) jest liczbą pierwszą.
Wykorzystaj twierdzenie Eulera.
Dane:b∈F∗p,b jest resztą kwadratową F∗p
Wynik:a∈F∗p taki, że a2=b.
"""


# https://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python
def modular_sqrt(a: int, p: int):

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, int((s + 1) / 2), p)
    b = pow(a, int(s), p)
    g = pow(n, int(s), p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a: int, p: int):
    ls = pow(a, int((p - 1) / 2), p)
    return -1 if ls == p - 1 else ls


if __name__ == "__main__":
    print(modular_sqrt(223, 17))  # 6
    print(modular_sqrt(58, 101))  # 19
    print(modular_sqrt(111, 113))  # 26 lub 87
