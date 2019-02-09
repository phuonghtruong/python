#!/usr/bin/env python

s = raw_input("Enter your string:")
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))


