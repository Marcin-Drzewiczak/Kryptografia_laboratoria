import random


# non-optimal approach to generation of random number
# it presents the beauty of oneliner, but consumes memory thousandfold.
def generate_random_oneliner(k: int):
    return sum([random.randint(0, 1) * 2 ** i for i in range(k)])


def generate_random(k: int):
    result = 0
    for i in range(k):
        if random.randint(0, 1) == 1:
            result += 2 ** i
    return result


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


def pow_mod(x, y, z):
    # Calculate (x ** y) % z efficiently."
    result = 1
    while y:
        if y & 1:
            result = result * x % z
        y >>= 1
        x = x * x % z
    return result


def power_optimal(n: int, k: int, b: int):
    while k > 1:
        # b = (b ** 2) % n
        b = pow_mod(b, 2, n)
        k = k / 2
    return b


def power_naive(n: int, k: int, b: int):
    while k > 1:
        b = (b ** 2) % n
        k = k / 2
    return b


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


if __name__ == "__main__":


    print(generate_random(5))
    print(generate_random(5))
    print(generate_random(5))
    print(generate_random(5))
    print(generate_random(5))
    print(generate_random(33))

    print(modinv(5, 2))
    print(modinv(120, 23))
    print(modinv(13, 5))
    print(modinv(
        669892632907423142807554789493111392205078053287806839068279555560804717506144656966710732064770697246939871016079002974444833961,
        66989263290742314280755478949311139220507805328780683906827955556080495183693955538717506144656966710732064770697246939871016079002974444833961))

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

    print(modular_sqrt(31, 83))  # 23, 60
    print(modular_sqrt(23, 59))  # not a modular sqrt
    print(modular_sqrt(60, 103))  # 36, 67

    print(prime_little_fermat_theorem(4))
    print(prime_little_fermat_theorem(5))
    print(prime_little_fermat_theorem(6))
    print(prime_little_fermat_theorem(2313132131231))
    print(prime_little_fermat_theorem(23450069))
    print(prime_little_fermat_theorem(23451569))
    print(prime_little_fermat_theorem(23460641))
    print(prime_little_fermat_theorem(23459981))
    print(prime_little_fermat_theorem(23459651))
