#!/usr/bin/env python

def printDict(n):
    d=dict()
    i = 0
    while i<n:
        d[i]=i**2
        i+=1
    print(d)

printDict(10)
