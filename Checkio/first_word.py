#!/usr/bin/env python3


##################################
# file_name : first_word.py
# author : Brian Truong
# Date create : 24th Feb, 2019
# Description : return the first word in a given text
######################################

from string import punctuation, whitespace
import re

def first_word(text:str)-> str:
    to_strip = punctuation + whitespace
    return text.lstrip(to_strip).split(' ',1)[0].rstrip(to_strip)

def first_word_2(text:str)->str:
    return re.match(r'\W*(\w[^,. !?"]*)',text).groups()[0]


def first_word_3(text:str)->str:
    return re.search("([\w']+)",text).group(1)

print(first_word("Hello world"))

print(first_word_2("Hello world"))
print(first_word_2(" a world"))
print(first_word(" a word"))
print(first_word("don't touch it"))
print(first_word_2("don't touch it"))
print(first_word_2(".... and so on ...."))


print(first_word("greetings, friend"))
print(first_word(".... and so on ...."))

print(first_word("hi"))
print(first_word("Hello.World"))



