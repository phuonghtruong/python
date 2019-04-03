#!/usr/bin/env python3

def checkio(text: str) -> str:
    count = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in count: count[letter] += 1
            else: count[letter] = 1

    sorted_count ={k:v for k,v in \
            sorted(count.items(),key = lambda x:( -x[1], x[0]))}

    print(sorted_count)

    return next(iter(sorted_count))

if __name__ == '__main__':
    print(checkio("Hello World!"))

    print(checkio("How do you do?"))

    print(checkio("One"))
    print(checkio("Oops!"))
    print(checkio("AAaooo!!!!"))
    print(checkio("a"*9000 + "b"*1000))

