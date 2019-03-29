#!/usr/bin/env python3

def popular_words(text: str, words: list) -> dict:
    result = {}
    for item in words:
        count = 0
        for word in text.split(' '):
            if item.lower() == word.lower():
                count += 1
        print(count)
        result[item] = count

    return result


if __name__ == '__main__':
    print(popular_words('''
    When I was One
    I had just begun
    When I was Two
    I was nearly new
    ''', ['i', 'was', 'three', 'near']))

    print(popular_words('''
     When I was One
     I had just begun
     When I was Two
     I was nearly new
     ''', ['i', 'was', 'three', 'near']))


    if popular_words('''
     When I was One
     I had just begun
     When I was Two
     I was nearly new
     ''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
        }:
        print("Coding complete? Click 'Check' to earn cool rewards!")
    else:
        print('Error')

    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
