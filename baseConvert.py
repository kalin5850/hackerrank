if __name__ == '__main__':

    def decToBin(decimal):
        binary = []

        while decimal > 0:
            reminder = decimal % 2
            binary.append(reminder)
            decimal = decimal // 2

        return binary

    def baseConverter(decimalNum, base):

        result = []

        while decimalNum > 0:
            reminder = decimal % base
            result.append(reminder)
            decimal = decimal // base

        return result

    a = bin(10)
    print(a)

    # convert binary to decimal
    b = '0b1010'
    print(int(b, 2))

    pass
