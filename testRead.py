import time
import serial
import sqlite3
import datetime

def Main()

	try:
		con = sqlite3.connect('test.db')
		cur = con.curson()
		cur.execute('CREATE TABLE Temp(temp INT, hum INT, time TEXT)')
		cur.execute('INSERT INTO Temp VALUES(1,1,?)',
				(datetime.now(),strftime('%Y%m%d%H%M%S'),))
		cur.execute
