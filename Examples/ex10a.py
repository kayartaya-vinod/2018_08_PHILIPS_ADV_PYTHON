# an example to connect to sqlite3, mysql, postgres

from pymysql import connect
# from psycopg2 import connect
# from sqlite3 import connect

props = {}
props['host'] = 'localhost'
props['port'] = 3306
props['user'] = 'root'
props['password'] = 'root'
props['database'] = 'philips_22_aug'


conn = connect(**props)

cmd = '''
create table contacts(
id integer primary key auto_increment,
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
except Exception as e:
	print('There was an error!', e)
