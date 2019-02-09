#!/usr/bin/env python

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()

