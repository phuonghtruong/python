#!/usr/bin/env python

s=raw_input("Enter your string:")
d={"Upper Case":0,"Lower Case":0}
for c in s:
    if c.isupper():
        d["Upper Case"]+=1
    elif c.islower():
        d["Lower Case"]+=1
    else:
        pass

print("Upper Case:",d["Upper Case"])
print("Lower Case:",d["Lower Case"])

