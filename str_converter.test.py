import str_converter

def test_to_speeds(str, correct_speeds):
    speeds = str_converter.to_speeds(str)
    if speeds == correct_speeds:
        print('Test passed')
    else:
        print('Test failed')

test_to_speeds(b'+255, -255', [ 255, -255])
test_to_speeds(b'-190, 0',    [-190,    0])
test_to_speeds(b'0, 0',       [   0,    0])
test_to_speeds(b'10, +0',     [  10,    0])