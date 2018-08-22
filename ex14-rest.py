from flask import Flask, request
import json
from pymysql import connect


app = Flask(__name__)


@app.route('/info')
def info():
	d = {}
	d['developer'] = 'Vinod'
	d['email'] = 'vinod@vinod.co'
	d['phone'] = '9731424784'

	return json.dumps(d)

def get_connection():
	props = {}
	props['host'] = 'localhost'
	props['port'] = 3306
	props['user'] = 'root'
	props['password'] = 'root'
	props['database'] = 'philips_22_aug'
	return connect(**props)

@app.route('/contacts', methods=['GET', 'POST'])
def get_all_contacts():
	out = 'POST is not yet handled!!!'
	if request.method=='GET':
		conn = get_connection()
		cur = conn.cursor()
		cmd = 'select * from contacts'
		cur.execute(cmd)
		out = json.dumps(cur.fetchall())
		conn.close()
	return out







