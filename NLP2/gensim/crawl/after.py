import pymysql
f=open('query.txt','r')

lines=f.readlines()
f.close()
f=open('go.txt','w')
q='insert into DB1 values '
for line in lines:
	q+='('
	q+=line.strip()
	q+='),\n'
f.write(q)

f.close()

q=q[:len(q)-2]
q+=';'
conn = pymysql.connect(host='localhost', user='root', password='9999', db='capstone', charset='utf8')
curs = conn.cursor()
curs = conn.cursor()
curs.execute("delete from DB1 where site='DCinside.com'")
curs.execute(q)
conn.commit()
conn.close()

