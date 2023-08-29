import uart
import str_converter
import time
import controller
from logging import getLogger
logger = getLogger(__name__)

def main():
    joycon = controller.Joycon("/dev/input/js0")
    try:
        while True:
            # ここにコントローラーの入力を受け取る処理を書く

            #controller_data = '99, -3444'
            controller_data: str = joycon.get()

            # UARTでデータを送信
            speeds: list[int] = str_converter.to_speeds(controller_data)
            #print(speeds)

            uart.send_to_motordriver(uart.uart_port1, speeds['left'])
            receive_data1 = uart.uart_port1.readline()

            uart.send_to_motordriver(uart.uart_port2, speeds['right'])
            receive_data2 = uart.uart_port2.readline()
            
            receive_data = ', '.join([str(receive_data1), str(receive_data2)])
            print(receive_data)

            time.sleep(uart.TIMEOUT)
            #break

    except KeyboardInterrupt:
        uart.uart_port1.close()
        uart.uart_port2.close()

if __name__ == '__main__':
    main()
