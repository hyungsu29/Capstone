import pymysql
conn = pymysql.connect(host='localhost', user='root', password='9999', db='capstone', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
curs.execute("select no, subject, date from DB1 order by no asc")
rows=curs.fetchall()
f=open('train.txt','w')
f.write('id	document	label\n')
for row in rows:
	no=row['no']
	subject=row['subject']
	date=row['date']
	no=no.replace('	','')
	subject=subject.replace('	','')
	date=date.replace('	','')
	q=no
	q+='	'
	q+=subject
	q+='	'
	q+=date
	q+='\n'
	f.write(q)

f.close()
