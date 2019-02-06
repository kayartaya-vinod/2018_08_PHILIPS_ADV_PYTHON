# from sqlite3 import connect
from pymysql import connect

# conn = connect('mydb.sqlite3')

props = {}
props['host'] = 'localhost'
props['port'] = 3306
props['user'] = 'root'
props['password'] = 'root'
props['database'] = 'philips_22_aug'


conn = connect(**props)


cur = conn.cursor()

name = input('Enter name: ')
email = input('Enter email: ')
phone = input('Enter phone: ')
address = input('Enter address: ')

cmd = 'insert into contacts(name, email, phone, address) values (%s,%s,%s,%s)'

try:
	cur.execute(cmd, (name, email, phone, address))
	conn.commit()
	print('Data saved successfully!')
except Exception as e:
	print('There was an error: ', e)