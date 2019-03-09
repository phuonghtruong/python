#!/usr/bin/env python3


import sys
import re

def checkio(*args):
    #max_num = 0
    #min_num = args[0]
    if len(sys.argv) == 0:
        return 0
    else:
        max_num = args[0]
        min_num = args[0]

        for x in args:
            if x > max_num: max_num = x
            if x < min_num: min_num = x

        #print(x)
        return max_num - min_num


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    print('Example:')
    print(checkio(1, 2, 3))

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
