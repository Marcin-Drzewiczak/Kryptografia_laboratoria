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

