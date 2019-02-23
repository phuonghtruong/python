#!/usr/bin/env python

##################################
# Author: Brian Truong
# Date:
# Description: Correct Sentecne from Checkio
########################################

from string import capwords

def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    if text.rfind('.') >= 0:
        return text[0].capitalize()+text[1:]
    else:
        return text[0].capitalize()+text[1:] + '.'

print(correct_sentence("welcome to New York"))
print(correct_sentence("greetings, friends"))

def correct_sentence2(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

print(correct_sentence2("greetings, friends"))
