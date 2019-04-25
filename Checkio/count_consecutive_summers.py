#!/usr/bin/env python3

def count_consecutive_summers(num):
    count = 1
    for j in range(1,num):
        _sum = 0
        for i in range(j,num):
            _sum += i
            if _sum == num:
                print(i)
                count += 1
            elif _sum > num:
                j += 1
                break

    return count

if __name__ == '__main__':
    #print(count_consecutive_summers(42))

    #print(count_consecutive_summers(99))
    #print(count_consecutive_summers(1))
    print(count_consecutive_summers(15))
    #print(count_consecutive_summers(1))
