from baseConvert import base_converter

if __name__ == '__main__':

    input = input()
    BIN = 2
    OCT = 8
    HEX = 16
    width = 2

    i = 1
    while i <= 17:
        String1 = "{}\t{}\t{}\t{}".format(i, base_converter(i, OCT), base_converter(i, HEX), base_converter(i, BIN), width)
        print(String1)
        i += 1


