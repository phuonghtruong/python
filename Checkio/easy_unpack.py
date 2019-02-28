#!/usr/bin/env python3

def easy_unpack(elements: tuple)->tuple:

    #values = elements.split(",")
    #print(elements[0])
    new_element=list()
    new_element.append(elements[0])
    new_element.append(elements[2])
    new_element.append(elements[-2])
    new_element_2 = tuple(new_element)
    #print(new_element_2)
    #return (tuple(new_element))
    return(elements[0],elements[2],elements[-2])

if __name__ == '__main__':
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)

    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)

    assert easy_unpack((6, 3, 7)) == (6, 7, 3)

    print('Done! Go Check!')


