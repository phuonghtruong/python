#!/usr/bin/env python3

def second_index(text:str, symbol:str)->[int, None]:
    index = 0
    cnt = 0
    while index < len(text):
        if text[index] == symbol:
           # print("found")
           #  print(text[index])
        #index = index + 1
            cnt = cnt + 1
        if cnt == 2:
            break
        index = index + 1
    print(index)
    print(cnt)
    if cnt < 2:
        return None
    else:
        return index


if __name__ == '__main__':
    print(second_index("sims", "s"))
    print('Example:')

    print(second_index("sims", "s"))


    # These "asserts" are used for self-checking and not for an auto-testing

    assert second_index("sims", "s") == 3, "First"

    assert second_index("find the river", "e") == 12, "Second"

    assert second_index("hi", " ") is None, "Third"

    assert second_index("hi mayor", " ") is None, "Fourth"

    assert second_index("hi mr Mayor", " ") == 5, "Fifth"

    print('You are awesome! All tests are done! Go Check it!')


