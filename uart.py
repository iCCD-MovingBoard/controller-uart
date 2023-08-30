import serial
import time
from subprocess import run

jetson_port1 = '/dev/ttyUSB0'
jetson_port2 = '/dev/ttyUSB1'
run(f'sudo chmod 777 {jetson_port1}', shell=True)
run(f'sudo chmod 777 {jetson_port2}', shell=True)

BAUDRATE = 9600
TIMEOUT = 0.01
STOPBITS = serial.STOPBITS_ONE
PARITY = serial.PARITY_NONE
BYTESIZE = serial.EIGHTBITS

uart_port1 = serial.Serial(jetson_port1,
                            baudrate=BAUDRATE,
                            timeout=TIMEOUT,
                            stopbits=STOPBITS,
                            parity=PARITY,
                            bytesize=BYTESIZE)

uart_port2 = serial.Serial(jetson_port2,
                            baudrate=BAUDRATE,
                            timeout=TIMEOUT,
                            stopbits=STOPBITS,
                            parity=PARITY,
                            bytesize=BYTESIZE)

# 0 ~ 32767の範囲の値を 0 ~ 256の範囲に変換する
def scale_speed(speed):
    CONTROLLER_MAX_VALUE = 32767
    UART_MAX_VALUE = 255
    CONV_RATE = UART_MAX_VALUE / CONTROLLER_MAX_VALUE
    speed = int(speed * CONV_RATE)
    if speed < 0: speed = 0
    return speed

def send_to_motordriver(port, speed:int):
    scaled_speed = scale_speed(speed)
    # print(f'speed: {speed}, unsigned_speed: {unsigned_speed}, type:{type(unsigned_speed)}')
    
    # port.write(bytes([255]))
    port.write(bytes([scaled_speed]))
    # port.write(bytes([240]))
    

def main():
    try:
        while True:
            for i in range(256):
                send_data = bytes([i])
                uart_port1.write(send_data)
                uart_port2.write(send_data)
                receive_data1 = uart_port1.readline()
                receive_data2 = uart_port2.readline()
                print(receive_data1, receive_data2)
                print(send_data == receive_data1, send_data == receive_data2)

                time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        uart_port1.close()
        uart_port2.close()

if __name__ == '__main__':
    main()
