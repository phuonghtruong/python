#!/usr/bin/env python

items=[x for x in raw_input("Enter a string:").split(',')]
items.sort()
print(','.join(items))

