#!/usr/bin/env python3

if __name__ == '__main__':
    N = int(input())
    l = []
    i = 0
    while i < N:
        command = list(input().split(' '))
        print(command[0])
        print(command[1])
        print(command[2])
        if command[0] == 'insert':
            l.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(l)
        elif command[0] == 'remove':
            l.remove(int(command[1]))
        elif command[0] == 'append':
            l.append(int(command[1]))
        elif command[0] == 'sort':
            l.sort()
        elif command[0] == 'pop':
            l.pop()
        elif command[0] == 'reverse':
            l.reverse()
        else:
            print("Command is not the list")
        i += 1
    print(l)

