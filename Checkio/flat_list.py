#!/usr/bin/env python3

#from collections import Iterable
#from itertools import chain
import itertools

def flat_list(array):
    new_list = []
    for item in array:
        if type(item) == type([]):
            new_list.extend(flat_list(item))
        else:
            new_list.append(item)
    return new_list

if __name__ == '__main__':
    print(flat_list([1,2,3]))
    print(flat_list([1,[2,2,2], 4]))
    print(flat_list([[[2]], [4,[5,6,[6], 6,6,6],7]]))
    print(flat_list([-1,[1, [-2],1],-1]))
