#!/usr/bin/env python3

import itertools

class Lamp:

    def __init__(self):
        #self.color = color
        self.state= itertools.cycle(('Green', 'Red', 'Blue', 'Yellow'))

    def light(self):
        return next(self.state)


if __name__ == '__main__':

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light()
    lamp_1.light()
    lamp_2.light()

    print(lamp_1.light())
    print(lamp_1.light())
    print(lamp_1.light())
    print(lamp_2.light())
    print(lamp_2.light())

