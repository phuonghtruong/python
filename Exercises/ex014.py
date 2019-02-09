#!/usr/bin/env python

value=[]
items=[x for x in raw_input("Enter binary number: ").split(',')]
for p in items:
    intp=int(p,2)
    if not intp%5:
        value.append(p)
print(','.join(value))
