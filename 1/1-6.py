"""
Zaimplementuj test (funkcję), który sprawdza liczba naturalna n
jest liczbą pierwszą. Wykorzystaj test Fermata
Dane:n∈N
Wynik:True jeśli n jest liczbą pierwszą, False w przeciwnym wypadku.
"""
# import time
import random


def prime_little_fermat_theorem(n: int, k: int = 100):
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


if __name__ == "__main__":
    print(prime_little_fermat_theorem(4))
    print(prime_little_fermat_theorem(5))
    print(prime_little_fermat_theorem(6))
    print(prime_little_fermat_theorem(2313132131231))
    print(prime_little_fermat_theorem(23450069))
    print(prime_little_fermat_theorem(23451569))
    print(prime_little_fermat_theorem(23460641))
    print(prime_little_fermat_theorem(23459981))
    print(prime_little_fermat_theorem(23459651))
