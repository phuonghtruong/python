#!/usr/bin/env python3

VOWELS = "aeiouy"
#translated_phrase = ""

def translate(phrase):
    translated_phrase = ""
    index = 0
    #print(len(phrase))
    while index < len(phrase):
    #for index in iter(range(0,len(phrase)+2)):
        #print(index)
        if index == len(phrase):
            break
        else:
            if phrase[index].isalpha():
                #print(phrase[index])
                if phrase[index] not in VOWELS:
                    #print(f"[Debug] {phrase[index]} not vowels")
                    if phrase[index+1] in VOWELS:
                        #print(phrase[index])
                        translated_phrase += phrase[index]
                        index = index + 2
                else:
                    if phrase[index+1] in VOWELS\
                        and phrase[index+2] in VOWELS:
                        translated_phrase += phrase[index]
                        index = index + 3
            else:
                translated_phrase += phrase[index]
                index = index + 1
        #print(index)
        #print(translated_phrase)
    return translated_phrase

if __name__ == '__main__':
    print(translate("hieeelalaooo"))
    print(translate("hoooowe yyyooouuu duoooiiine"))
    print(translate("aaa bo cy da eee fe"))
    print(translate("sooooso aaaaaaaaa"))
