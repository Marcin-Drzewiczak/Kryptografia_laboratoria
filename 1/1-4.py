"""
4. Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję),
który sprawdza czy element zbioru Z∗p jest resztą kwadratową w Z∗p.
Wykorzystaj twierdzenie Eulera.
Dane:b∈Z∗p
Wynik:True jeśli b jest resztą kwadratową, False w przeciwnym wypadku.
"""


def power_binary_list(x, k, n):
    temp_list = list(reversed([int(i) for i in list('{0:0b}'.format(k))]))
    y = 1
    i = len(temp_list) - 1
    while i >= 0:
        y = ( y ** 2 ) % n
        if temp_list[i] == 1:
            y = (y * x) % n
        i = i -1
    return y


def quadratic_residue_power(x: int, p: int):
    if p < 2:
        return False
    if x == 0:
        return False
    if power_binary_list(x, int((p-1)/2), p) == 1:
        return True
    else:
        return False


def quadratic_residue(q, n):
    return q in [i * i % n for i in range(1, n)]


if __name__ == "__main__":
    # print(quadratic_residue(15, 22))  # true
    # print(quadratic_residue(1, 5))  # true
    # print(quadratic_residue(3, 8))  # false
    # print(quadratic_residue(31, 83))  # true
    # print(quadratic_residue(17, 23))  # false

    print(quadratic_residue_power(15, 22))  # true
    print(quadratic_residue_power(1, 5))  # true
    print(quadratic_residue_power(3, 8))  # false
    print(quadratic_residue_power(31, 83))  # true
    print(quadratic_residue_power(17, 23))  # false
