def print_starts(length):
    k = (2 * length) - 2
    for p in range(0, length):
        for n in range(0, k):
            print(end=" ")
        k = k - 1
        for n in range(0, p + 1):
            print("*", end=' ')
        print()


if __name__ == '__main__':
    length = 7
    print_starts(length)

