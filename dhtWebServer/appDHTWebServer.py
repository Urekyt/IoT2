from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3

def getData():
	conn = sqlite3.connect('../iotData.db')
	curs = conn.cursor()

	for row in curs.execute("SELECT * FROM DHT_DATA ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		hum = row[2]
	conn.close()
	return time, temp, hum

@app.route("/")
def index():
	time, temp, hum = getData()
	templateData = {
		'time':time,
		'temp':temp,
		'hum':hum
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 80, debug = True)

