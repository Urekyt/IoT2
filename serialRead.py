import time
import serial
import datetime
import sqlite3

def logData(temp, hum):
	conn = sqlite3.connect('iotData.db')
	curs=conn.cursor()
	curs.execute("INSERT INTO DHT_data values(datetime(), (?), (?))", (temp, hum))
	conn.commit()
	conn.close()


ser = serial.Serial(
	port = '/dev/serial0',
	baudrate  = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)



while 1:

	x = ser.readline().strip()
	z = x.decode('utf-8')
	zstr = str(z)
	if x != b'':
		stringToTuple = eval(x)
		temp = stringToTuple[0]
		hum = stringToTuple[1]
		logData(temp, hum)
		print(temp, hum)
		print(type(temp), type(hum))
