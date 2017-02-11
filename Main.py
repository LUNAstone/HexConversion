import sys


hexa = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F')


def hex_to_dec(hex):
    pass


def dec_to_hex(dec):
    pass


if __name__ == "__main__":
    print("Hexadecimal and Decimal Converter")
    print("Type 'H' for Hexadecimal to Decimal Conversion")
    print("Type 'D' for Decimal to Hexadecimal Conversion")
    print("Type anything else to quit.")
    while True:
        menu_answer = str(input()).lower()
        if menu_answer == "h":
            try:
                number = int(input("What is the number you would like to convert? ", 16))
            except (ValueError, TypeError):
                print("Please type a number.", end="\n\n")
                continue
            else:
                hex_to_dec(number)
        elif menu_answer == "d":
            try:
                number = int(input("What is the number you would like to convert? "))
            except (ValueError, TypeError):
                print("Please type a number.", end="\n\n")
                continue
            else:
                dec_to_hex(number)
        else:
            sys.exit()
