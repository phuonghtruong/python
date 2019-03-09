#!/usr/bin/env python3

def checkio(numbers_array: tuple) -> list:
    #list(i) for i in numbers_array
    #map(list, numbers_array)
    return sorted(numbers_array, key= abs)


if __name__ == '__main__':
    print(list(checkio((-20,-5,10,15))))
