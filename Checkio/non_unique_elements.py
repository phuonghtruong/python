#!/usr/bin/env python3

import collections

def checkio(data: list) -> list:
    d = {}
    for item in data:
        if item not in d:
            d[item] = 0
        d[item] += 1

    for number, count in d.items():
        if count == 1 : data.pop(data.index(number))
    return data

if __name__ == '__main__':
    print(list(checkio([1,2,3,1,2])))
    print(list(checkio([1,2,3,4,5])))
    print(list(checkio([5,5,5,5,5])))
    print(list(checkio([10,9,10,10,9,8])))
