from pymysql import connect

props = {}
props['host'] = 'localhost'
props['port'] = 3306
props['user'] = 'root'
props['password'] = 'root'
props['database'] = 'philips_22_aug'

conn = connect(**props)

cur = conn.cursor()

cmd = 'select * from contacts'

cur.execute(cmd)
for c1 in cur.fetchall():
	print(c1)

# while True:
# 	c1 = cur.fetchone()
# 	if c1 is None: break
# 	print(c1)

conn.close()

