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


if __name__ == "__main__":
    print(generate_random(5))
    print(generate_random(5))
    print(generate_random(5))
    print(generate_random(5))
    print(generate_random(5))
    print(generate_random(33))
