# -*- coding: utf-8 -*-
# 利用pySerial模块完成与串行端口进行通信

import serial

# Device name varies
ser = serial.Serial('/dev/tty.usbmodem641',
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)
ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
