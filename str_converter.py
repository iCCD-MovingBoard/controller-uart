def to_speeds(str):
    str = str.decode('utf-8')
    speeds_str = str.split(',')
    speeds = []
    for speed in speeds_str:
        speed = speed.strip()
        speed = int(speed)
        speeds.append(speed)
    speeds = {'left': speeds[0], 'right': speeds[1]}
    return speeds