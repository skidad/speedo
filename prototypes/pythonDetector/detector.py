# Blinks a LED on an arduino
import serial
import sys

connected=False

ser= serial.Serial("COM5",9600)
while not connected: 
  serin = ser.read()
  connected = True
  
ser.write("1".encode())
lastIntVal=1
valstr = ""
while True:
  val = ser.read().decode()
  
  if (val != ';'):
    valstr += val
  else:
    if ( "" != valstr):
      intVal = int(valstr)
      valstr = ""
      if (intVal == 0):
        if (lastIntVal != 0):
          sys.stdout.write("\n")
      else:
        sys.stdout.write("{} ".format(intVal))

      lastIntVal = intVal
      
#ser.close()
