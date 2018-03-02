# main.py -- put your code here!
from pyb import UART 

uart = UART(6, 115200)

while True:
    recv = uart.read(9)
    if len(recv) == 9:
        if recv[0] == 0x59 and recv[1] == 0x59: 
            checksum = 0
            for i in range(0, 8):
                checksum = checksum + recv[i]
            checksum = checksum % 256
            if checksum == recv[8]:
                distance = recv[2] + recv[3] * 256
                strength = recv[4] + recv[5] * 256
                print(distance, strength)    
        

