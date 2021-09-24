import re

def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / (60 * 60);
    if direction == 'W' or direction == 'S':
        dd *= -1
    return dd;

def parse_dms(dms):
    # split up the DMS string into four parts
    parts = re.findall(r'[A-Za-z]+|\d+', dms)
    coord = dms2dd(parts[0], parts[1], parts[2], parts[3])

    return (coord)