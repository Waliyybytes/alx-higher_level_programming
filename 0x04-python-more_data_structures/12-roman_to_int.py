#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if type(roman_string) != str or roman_string == "":
        return 0
    i = 0
    num = 0
    while i < len(roman_string) - 1:
        if roman[roman_string[i + 1]] <= roman[roman_string[i]]:
            num += roman[roman_string[i]]
        if roman[roman_string[i + 1]] > roman[roman_string[i]]:
            num -= roman[roman_string[i]]
        i += 1
    num += roman[roman_string[i]]
    return num
