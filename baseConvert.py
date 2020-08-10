def base_converter(decimalNum, base):

    if decimalNum is None or base is None:
        raise Exception("The input decimal or base is invalidate.")

    if decimalNum < 0 or base <= 0:
        raise Exception("The input decimal or base is less than 0")

    DIGITS = "0123456789ABCDEF"
    result = []
    digit = ''

    while decimalNum > 0:
        reminder = decimalNum % base
        decimalNum = decimalNum // base
        result.append(DIGITS[reminder])

    result.reverse()

    for v in result:
        digit = digit + v

    return digit


if __name__ == '__main__':

    BIN = 2
    OCT = 8
    HEX = 16

    # decimal to hex
    a = base_converter(17, BIN)
    print(a)
    print(bin(17))

    # convert binary to decimal
    b = '0b1010'
    print(int(b, 2))

