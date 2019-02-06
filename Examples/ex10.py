# an example to connect to sqlite3, mysql, postgres

# from pymysql import connect
# from psycopg2 import connect
from sqlite3 import connect

conn = connect('mydb.sqlite3')

cmd = '''
create table contacts(
id integer primary key autoincrement,
name varchar(50) not null,
email varchar(200) unique,
phone varchar(200) unique,
address varchar(255)
)
'''

cur = conn.cursor()
try:
	cur.execute(cmd)
	print('Table created!')
except(Exception):
	print('There was an error!')
