#!/usr/bin/env python3

def checkio(number: int)-> int:
    mul = 1
    for item in [int(digits) for digits in str(number)]:
        if item != 0:
            mul = mul*item
    return mul



if __name__ == '__main__':
    print(checkio(123405))
