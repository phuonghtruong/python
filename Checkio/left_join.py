#!/usr/bin/env python3

def left_join(phrases):
    #return (','.join(list(phrases))).replace('right','left')

    return (",".join(phrases).replace('right','left'))
    #return (','.join(list(phrases))).replace('right','left')


if __name__ == '__main__':
    print(left_join(("left", "right", "left", "stop")))
