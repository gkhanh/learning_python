def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


def main():
    print(factorial(10))


if __name__ == "__main__":
    main()
