#!/usr/bin/env python3

def checkio(array):
    if not array:
        return 0
    else:
        sum = 0
        for index in range (0, len(array)):
            if index%2 == 0:
                sum = sum + array[index]
        return sum*array[-1]


if __name__ == '__main__':
    print(checkio([0,1,2,3,4,5]))
