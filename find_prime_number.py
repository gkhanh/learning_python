def find_prime_number(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
            else:
                return True


def main():
    print(find_prime_number(10001))


if __name__ == "__main__":
    main()
