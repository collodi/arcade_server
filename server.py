import os
from flask import Flask, request
from tinydb import TinyDB, Query

fn = '/tmp/arcade.db'
app = Flask(__name__)

@app.route('/register', methods = ['POST'])
def register():
	dev_id = request.form['id']
	group = request.form['group']
	color = request.form['color']
	ip = request.form['ip']

	data = { 'id': dev_id, 'group': group, 'color': color, 'ip': ip, 'push': 0 }
	with TinyDB(fn) as db:
		device = Query()
		db.upsert(data, device.id == dev_id)

		print(db.all())

	return 'OK'

@app.route('/push', methods = ['POST'])
def button_pushed():
	dev_id = request.form['id']
	epoch = request.form['epoch']

	with TinyDB(fn) as db:
		device = Query()
		db.update({ 'push': epoch }, device.id == dev_id)

		print(db.all())

	return 'OK'

if __name__ == '__main__':
	app.run(host = '0.0.0.0')
