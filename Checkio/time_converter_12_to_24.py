#!/usr/bin/env python3

def time_converter(time):
    hour = time.split(' ')[0].split(':')[0]
    minutes = time.split(' ')[0].split(':')[1]

    if 'p' in time:
        if int(hour) < 12:
            hour = str(int(hour) + 12)
    else:
        if hour == '12':
            hour = '0'
        elif int(hour) < 10:
            hour = '0' + hour
    return hour + ':' + minutes

if __name__ == '__main__':
    print(time_converter('12:30 p.m.'))
    print(time_converter('9:00 a.m.'))
    print(time_converter('11:15 p.m.'))
