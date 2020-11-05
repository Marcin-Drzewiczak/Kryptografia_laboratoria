import time


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


if __name__ == "__main__":

    t0 = time.perf_counter()
    for i in range(1, 10000000):
        # print(power_optimal(13, 2, i))
        power_optimal(13, 2, i)
    t1 = time.perf_counter()
    print("power optimal: %s" % (t1 - t0))

    t0 = time.perf_counter()
    for i in range(1, 10000000):
        # print(power_naive(13, 2, i))
        power_naive(13, 2, i)
    t1 = time.perf_counter()
    print("power naive: %s" % (t1 - t0))

    t0 = time.perf_counter()
    for i in range(1, 10000000):
        power_binary_list(i, 2, 13)
    t1 = time.perf_counter()
    print("power binary list: %s" % (t1 - t0))
