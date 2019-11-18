#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: November 2019
# This is a program which finds the area of the triangle.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# This is what runs the program.
print("This program converts a temperature from degrees Celcius"
      " to degrees Fahrenheit.")


def calculations(base_copy, height_copy):
    # This does the calculations
    area = ((base_copy * height_copy)/2)
    print(color.GREEN + "The area is {0}".format(area) + color.END)


def main():
    # This is what gets the dimensions of the triangle
    while True:
        base_as_string = input(color.YELLOW + 'Input the base of the' +
                               ' triangle: ' + color.END)
        height_as_string = input(color.YELLOW + "Input the height " +
                                 "of the triangle: " + color.END)

        try:
            base = int(base_as_string)
            height = int(height_as_string)

            calculations(base, height)
            break

        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
                  ' number...' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
