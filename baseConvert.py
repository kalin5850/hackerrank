if __name__ == '__main__':

    DIGITS = "0123456789ABCDEF"
    BIN = 2
    OCT = 8
    HEX = 16

    def baseConverter(decimalNum, base):
        result = []

        while decimalNum > 0:
            reminder = decimalNum % base
            decimalNum = decimalNum // base
            result.append(DIGITS[reminder])
            result.reverse()

        return result

    # decimal to hex
    a = baseConverter(10, BIN)
    print(a)

    # convert binary to decimal
    b = '0b1010'
    print(int(b, 2))

