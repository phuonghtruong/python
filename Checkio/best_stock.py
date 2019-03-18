#!/usr/bin/env python3

def best_stock(data):
    value = 0
    name = ''
    for k,v in data.items():
        if v > value:
            value = v
            name = k
    return name

def best_stock_2(data):
    return max(data, key=data.get)



if __name__ == '__main__':
    print(best_stock({
        'CAC' : 10.0,
        'ATX' : 390.2,
        'WIG' : 1.2
        }))
