#!/usr/bin/env python3

import collections

def frequency_sort(items):
    lst = []
    counts = collections.Counter(items)
    #print(counts)

    new_counts = [(k,counts[k]) for k in sorted(counts, key=counts.get,reverse = True)]
    #print(new_counts)

    #lst_1 = sorted(items, key=lambda x: (counts[x],x), reverse=True)
    #print(lst_1)
    #lst_2 = sorted(sorted(items), key= items.count, reverse=True)
    #print(lst_2)

    for k,v in new_counts :
        for i in range(v):
            lst.append(k)
    return lst

if __name__ == '__main__':
    print(frequency_sort([4,6,2,2,6,4,4,4]))
    print(frequency_sort(['bob','bob','carl','alex','bob']))
    print(frequency_sort([17, 99, 42]))
    print(frequency_sort([]))
    print(frequency_sort([1]))
    print(frequency_sort([4,6,2,2,2,6,4,4,4,4]))
