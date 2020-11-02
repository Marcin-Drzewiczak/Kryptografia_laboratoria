"""
4. Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję),
który sprawdza czy element zbioru Z∗p jest resztą kwadratową w Z∗p.
Wykorzystaj twierdzenie Eulera.
Dane:b∈Z∗p
Wynik:True jeśli b jest resztą kwadratową, False w przeciwnym wypadku.
"""


def quadratic_residue(q, n):
    return q in [i * i % n for i in range(1, n)]


if __name__ == "__main__":
    print(quadratic_residue(15, 22))  # true
    print(quadratic_residue(1, 5))  # true
    print(quadratic_residue(3, 8))  # false
