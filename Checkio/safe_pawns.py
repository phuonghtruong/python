#!/usr/bin/env python3

def safe_pawns(pawns: set) -> int:
    num_pawns_safe = 0
    pawns_indexes = set()

    for pawn in pawns:
        row = int(pawn[1])
        col = ord(pawn[0]) - 97
        pawns_indexes.add((row,col))

    for row,col in pawns_indexes:
        isSafe = ((row-1,col-1) in pawns_indexes)\
                or ((row-1,col+1) in pawns_indexes)
        if isSafe:
            num_pawns_safe += 1
    return num_pawns_safe

if __name__ == '__main__':
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
    print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
    print(safe_pawns({"e7", "e6", "d5", "f5", "c4", "e4", "g4", "e8"}))
