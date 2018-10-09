import json
import sqlite3

con = sqlite3.connect('sensor.db')
cur = con.cursor()
cur.execute('select * from data ORDER BY id DESC limit 10')
rows = cur.fetchall()

#print(rows)
#print(rows[0][0])
l = list()
for r in rows:
    d = dict()
    d['id'] = r[0]
    d['nowDate'] = r[1]
    d['nowTime'] = r[2]
    d['humidity'] = round(float(r[3]),2)
    d['temperature'] = round(float(r[4]),2)
    l.append(d)

jsonD = json.dumps(l)

print(jsonD)
