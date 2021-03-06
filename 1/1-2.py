'''
Zaimplementuj algorytm (funkcję) obliczania odwrotności B grupie Φ(n).
Wykorzystaj Rozszerzony Algorytm Euklidesa.
Dane:n∈N,b∈Φ(n)
Wynik:b−1∈Φ(n)
'''


def xgcd(a: int, b: int) -> tuple:
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
        raise Exception('modular inverse does not exist')
    else:
        if y < 0:
            return y + a
        return y


if __name__ == "__main__":
    print(modinv(5, 2))
    print(modinv(120, 23))
    print(modinv(13, 5))
    print(modinv(669892632907423142807554789493111392205078053287806839068279555560804717506144656966710732064770697246939871016079002974444833961, 66989263290742314280755478949311139220507805328780683906827955556080495183693955538717506144656966710732064770697246939871016079002974444833961))
