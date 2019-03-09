#!/usr/bin/env python3

def between_markers(text:str, begin:str, end:str)-> str:
    if begin in text:
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0

    if end in text:
        end_index = text.find(end)
    else:
        end_index = len(text)
    return text[begin_index:end_index]




def between_markers_2(text: str, begin: str, end: str) -> str:

   m1 = 0 if text.find(begin) < 0 else text.find(begin) + len(begin)

   m2 = len(text) if text.find(end) < 0 else text.find(end)

   return text[m1:m2]



if __name__ == '__main__':
    print(between_markers('What is >apple<', '>','<'))
