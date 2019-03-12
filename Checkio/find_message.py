#!/usr/bin/env python3

def find_message(text: str) -> str:
    result= []
    s = ""
    for letter in text:
        if letter.isupper() == True:
            result.append(letter)
    return s.join(result)

def find_message_2(text):
    return ''.join(i for i in text if i.isupper())



if __name__=='__main__':
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
