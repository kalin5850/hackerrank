
def smallest_integer(A):
    set_A = set(A)
    tarket_value = set_A.pop()

    for value in set_A:
        if value < 0:
            return 1

    for value in set_A:
        tarket_value += 1
        if tarket_value == value:
            continue

    if tarket_value == max(set_A):
        tarket_value += 1

    return tarket_value


if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    # A = [-1, -2]
    # A = [1, 2, 3]
    print(smallest_integer(A))

