# """
# Convert given integer to corresponding roman numerals
# """

# iterating downwards through list
# added 9 and 4 value: symbol pairs
check_list = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def int_to_roman(num):

    num = int(num)
    
    roman = ""

    while num > 0:
        for n, r in check_list:
            while num >= n:
                roman += r
                num -= n

    return roman


while True:
    num = input("Let's convert integers to Roman Numerals! \nGive me a number between 1 and 1999: ") 

    final_roman = int_to_roman(num)

    print (f"Your number {num} in Roman Numerals is {final_roman}")
