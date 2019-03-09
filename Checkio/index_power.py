#!/usr/bin/env python3

def index_power(array: list, n: int) -> int:
    if len(array) < n+1:
        return -1
    else:
        return array[n]**n


if __name__ == '__main__':
    print(index_power([1,2,3,4],2))
