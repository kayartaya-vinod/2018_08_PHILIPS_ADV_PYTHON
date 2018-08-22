from pymysql import connect

props = {}
props['host'] = 'localhost'
props['port'] = 3306
props['user'] = 'root'
props['password'] = 'root'
props['database'] = 'philips_22_aug'


conn = connect(**props)

cur = conn.cursor()

id = input('Enter id: ')
cmd = 'select * from contacts where id = %s'

cur.execute(cmd, (id,))
c1 = cur.fetchone()
conn.close()

if c1 is None: print('No data found for id', id)
else: print(c1)

