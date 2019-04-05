#!/usr/bin/env python3

def long_repeat(line):
    if not line: return 0
    else:
        max_repeat = 0
        count = 1
        for item in range(1,len(line)):
            if line[item] == line[item-1] :
                count += 1

            else: count = 1
            print(f'{item} : {count}')
            if max_repeat < count: max_repeat = count
        return max_repeat

if __name__ == '__main__':
    #print(long_repeat('sdsffffse'))
    #print(long_repeat('ddvvrwwwrggg'))
    #print(long_repeat('abababaab'))
    #print(long_repeat(''))
    print(long_repeat('abababa'))
