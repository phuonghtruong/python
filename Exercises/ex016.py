#!/usr/bin/env python

s = raw_input("Enter your string:")
d={"Digits":0 ,\
        "Letters":0}
for c in s:
    if c.isdigit():
        d["Digits"]+=1
    elif c.isalpha():
        d["Letters"]+=1
    else:
        pass
print("Number of alphabet:",d["Letters"])
print("Number of digits:",d["Digits"])

