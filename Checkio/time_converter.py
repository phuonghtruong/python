#!/usr/bin/env python3

def time_converter(time):
    hour = time[0:2]
    minutes = time[3:5]
    am_pm = ''

    if int(hour) == 0 or int(hour) == 24:
        hour = 12
        am_pm = 'a.m'
    elif int(hour) < 12:
        am_pm = 'a.m'
    elif int(hour) == 12:
        am_pm = 'p.m'
    else:
        hour = int(hour) - 12
        am_pm = 'p.m'

    if int(hour) > 0 and int(hour) < 10:
        hour = str(hour).strip('0')

    return(f'{hour}:{minutes} {am_pm}.')


if __name__ == '__main__':
    print(time_converter('12:30'))
    print('\n')
    print(time_converter('09:00'))
    print('\n')
    print(time_converter('23:15'))
    print('\n')
    print(time_converter('00:00'))
    print('\n')
    print(time_converter('18:50'))
    print('\n')
    print(time_converter('00:10'))
    print('\n')
   # print(time_converter('23:15'))
   # print('\n')


