import pymysql
import json


conn = pymysql.connect(host='localhost', user='root', password='9999', db='capstone', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)
sql='select * from DB1 limit 0,10'
curs.execute(sql)
rows=curs.fetchall()

data=json.dumps(rows, ensure_ascii=False)
print (data)

f=open('result.json','w')
f.write(data)
f.close()

conn.commit()
conn.close()
             
