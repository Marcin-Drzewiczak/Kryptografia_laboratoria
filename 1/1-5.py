"""
Zaimplementuj algorytm (funkcję), który oblicza pierwiastek kwadratowy w ciele F∗p,
gdzie p ≡ 3 (mod 4) jest liczbą pierwszą.
Wykorzystaj twierdzenie Eulera.
Dane:b∈F∗p,b jest resztą kwadratową F∗p
Wynik:a∈F∗p taki, że a2=b.
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


def modular_sqrt(a, p):
    if p % 4 == 3:
        if quadratic_residue_power(a, p):
            result1 = power_binary_list(a, int((p+1) / 4), p)
            result2 = p - result1
        else:
            return "not a modular sqrt"
    else:
        return "not a p % 4 == 3"
    return result1, result2


if __name__ == "__main__":
    print(modular_sqrt(31, 83))  # 23, 60
    print(modular_sqrt(23, 59))  # not a modular sqrt
    print(modular_sqrt(60, 103))  # 36, 67
