# Blinks a LED on an arduino
import serial
connected=False

ser= serial.Serial("COM5",9600)
while not connected: 
  serin = ser.read()
  connected = True
  
ser.write("1".encode())

while (ser.read() == 1):
  ser.read()
  
ser.close()
