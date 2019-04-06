#!/usr/bin/env python3

def sun_angle(time):

    ANGLE_HOUR = 15
    ANGLE_MIN = 0.25

    hour = time[0:2]
    minutes = time[3:5]

    print(f'{hour} : {minutes}')

    if int(hour) < 6 or (int(hour) >= 18 and int(minutes) > 0):
        return 'I don\'t see the sun!'
    else:
        if int(minutes) == 0:
            return str((int(hour) -6)*ANGLE_HOUR)
        else:
            return str((int(hour) -6)*ANGLE_HOUR + (int(minutes) * ANGLE_MIN))


if __name__ == '__main__':
    print(sun_angle('07:00'))
    print(sun_angle('01:23'))
    print(sun_angle('12:15'))
