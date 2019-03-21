#!/usr/bin/env python3

def checkio(words: str) -> bool:
    count = 0
    for index in words.split(" "):
       # print(index)
        if index.isalpha():
            count = count + 1
        else:
            count = 0
        if count == 3:
            return True
    return False


if __name__ == '__main__':
    print(checkio("Hello World hello"))
    print(checkio("He is 123 man" ))


