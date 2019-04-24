#!/usr/bin/env python3

from typing import List

def checkio(game_result: List[str]) -> str:
    border = 3  

    for col in range(border):
        x_win = True
        o_win = True
        
        for row in range(border):
            
            if game_result[row] == 'XXX':
                return "X"
            elif game_result[row] == 'OOO':
                return "O"
            if game_result[row][col] == 'X' and x_win:
                x_win = True
                o_win = False
            elif game_result[row][col] == 'O' and o_win:
                x_win = False
                o_win = True
            else:
                x_win = False
                o_win = False
        
        if x_win: return "X"
        elif o_win: return "O"
        else:
            if game_result[0][0] + game_result[1][1] + game_result[2][2] == 'XXX' or \
               game_result[0][2] + game_result[1][1] + game_result[2][0] == 'XXX' :
                return "X"
            elif game_result[0][0] + game_result[1][1] + game_result[2][2] == 'OOO' or \
               game_result[0][2] + game_result[1][1] + game_result[2][0] == 'OOO' :
                return "O"                

    return "D"

if __name__ == '__main__':
    print(checkio([
        "X.O",
        "XX.",
        "XOO"]))

    print(checkio([
        "OO.",
        "XOX",
        "XOX"]))
    print(checkio([
        "OOX",
        "XXO",
        "OXX"]))
    print(checkio([
        "O.X",
        "XX.",
        "XOO"]))

    print("\nDone !!!")

