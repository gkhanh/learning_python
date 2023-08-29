def fibonacci_sequence(i):
    z = []
    z.append(0)
    z.append(1)
    z.append(z[0] + z[1])
    for j in range(2, i):
        z[j] = z[j - 2] + z[j - 1]
        z.append(z[j] + z[j - 1])
    print(z)


def main():
    print(fibonacci_sequence(20))


if __name__ == "__main__":
    main()
