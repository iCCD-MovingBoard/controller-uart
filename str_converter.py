def to_str(byte_str):
    str = byte_str.decode('utf-8')
    return str

def to_speeds(str):
    speeds_str = str.split(',')
    speeds = []
    for speed in speeds_str:
        speed_str = speed.strip()
        speed: int = int(speed)
        speeds.append(speed)
    speeds = {'left': speeds[0], 'right': speeds[1]}
    return speeds