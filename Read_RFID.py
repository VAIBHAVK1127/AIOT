Read_RFID:

import time
import serial
                
data = serial.Serial(
                    port='/dev/ttyAMA0',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
                    #timeout=1 # must use when using data.readline()
                    #)
print (" ")
          
try:     
   while 1:
         #x=data.readline()#print the whole data at once
         #x=data.read()#print single data at once
         
         print ("Place the card")
         x=data.read(12) #print upto 10 data at once and the 
                         #remaining on the second line
         output = str(x, 'UTF-8')
         print ("RFID Card No : ",output)
         print (" ")

except KeyboardInterrupt:
       data.close()
