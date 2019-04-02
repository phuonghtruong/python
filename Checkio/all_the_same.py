#!/usr/bin/env python3

from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    isSame = True
    for n in range(0,len(elements) - 1):
        if elements[n] != elements[n+1]:
            isSame = False
    return isSame


if __name__ == '__main__':
    print(all_the_same([1,1,1]))
    print(all_the_same([1,2,1]))
    print(all_the_same(['a','a','a']))
    print(all_the_same([]))
    print(all_the_same([1]))
