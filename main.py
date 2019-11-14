def main(a, b):
    """ a is our lower bound and b is upper"""
    for x in range(a, b+1):
        print(fizz_buzz(x))


def test_main(a, b):
    """ a is our lower bound and b is upper"""
    for x in range(a, b+1):
        print(fizz_buzz(x), x)


def fizz_buzz(x):
    if x % 3 == 0:
        if x % 5 == 0:
            return "FizzBuzz"
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    return x


if __name__ == '__main__':
    main(1, 100)
    # test_main(1, 15)
