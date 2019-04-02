#!/usr/bin/env python3.6

import re

def checkio(data: str) -> bool:
    isSafe = True
    if len(data) < 10 or data.isalpha() \
            or data.islower() or data.isupper() or data.isdigit():
                isSafe = False
    return isSafe


if __name__ == '__main__':
    print(checkio('A1213pok1'))
    print(checkio('bAse730onE4'))
    print(checkio('asasasasasasasaas'))# "3rd example"
    print(checkio('QWERTYqwerty') ) #"4th example"
    print(checkio('123456123456'))# "5th example"
    print(checkio('QwErTy911poqqqq'))# "6th example"
