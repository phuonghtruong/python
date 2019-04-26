#!/usr/bin/env python3

FIRST_TEN = ["one" , "two", "three", "four", "five", "six",
             "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirdteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    speech = ''
    hundred_digit = int(number / 100)
    second_digit = int((number % 100) / 10)
    last_digit = int(str(number)[-1])

    if hundred_digit > 0:
        speech += FIRST_TEN[hundred_digit - 1] + ' ' + HUNDRED
    if second_digit > 1:
        speech += ' ' + OTHER_TENS[second_digit - 2]
        if last_digit > 0:
            speech += ' ' + FIRST_TEN[last_digit - 1]
    elif second_digit == 1:
        speech += ' ' + SECOND_TEN[int(str(number)[-2:]) - 10]
    else:
        if last_digit > 0:
            speech += ' ' + FIRST_TEN[last_digit - 1]
    return speech.lstrip().rstrip()

if __name__ == '__main__':
    print(checkio(4))
    print(checkio(133))
    print(checkio(12))
    print(checkio(101))
    print(checkio(212))
    print(checkio(40))


