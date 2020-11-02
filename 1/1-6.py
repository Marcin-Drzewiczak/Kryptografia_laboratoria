"""
Zaimplementuj test (funkcję), który sprawdza liczba naturalna n
jest liczbą pierwszą. Wykorzystaj test Fermata
Dane:n∈N
Wynik:True jeśli n jest liczbą pierwszą, False w przeciwnym wypadku.
"""


def power_alg(n: int, k: int, b: int):
    while k > 1:
        b = (b ** 2) % n
        k = k / 2
    return b


def prime_little_fermat_theorem(x):
    # check if 2 ^ x-1 in x-modulo is equal to 1
    return power_alg(2, x-1, x) == 1


if __name__ == "__main__":
    print(prime_little_fermat_theorem(4))
    print(prime_little_fermat_theorem(5))
    print(prime_little_fermat_theorem(23450069))
    print(prime_little_fermat_theorem(23451569))
    print(prime_little_fermat_theorem(23460641))
    print(prime_little_fermat_theorem(23459981))
    print(prime_little_fermat_theorem(23459651))
