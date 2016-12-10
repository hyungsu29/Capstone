import pymysql
import datetime
import time
from datetime import timedelta
import sys

_site=sys.argv[1]
_startdate=sys.argv[2]
_enddate=sys.argv[3]
_startdate=int(_startdate)
_enddate=int(_enddate)

oneday=timedelta(days=1)

conn = pymysql.connect(host='localhost', user='root', password='9999', db='capstone', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
for i in range(_startdate, _enddate+1):
	print (i)
	year=int(i/10000)
	month=i-(year*10000)
	month/=100
	day=i%100
	year=int(year)
	month=int(month)
	day=int(day)
	enddate=datetime.datetime(year,month,day)
	idx=0
	label=0
	f=open('./trainset/'+str(i)+'.txt','w')
	f.write('id	document	label\n')
	nowdate=20140801
	while(1==1):
		year2=int(nowdate/10000)
		month2=nowdate-(year2*10000)
		month2/=100
		day2=nowdate%100
		year2=int(year2)
		month2=int(month2)
		day2=int(day2)
		datenowdate=datetime.datetime(year2,month2,day2)
		datenowdate+=oneday
		print (datenowdate)
		nowdate=datenowdate.year*10000
		nowdate+=datenowdate.month*100
		nowdate+=datenowdate.day
		print (nowdate)
		if(datenowdate==enddate):
			break

		query='select no, subject, date from DB1 where date='
		query+="'"+str(nowdate)+"'"
		query+=' and '
		query+='site='
		query+="'"+_site+"'"
		query+=' order by no asc'
		curs.execute(query)
		rows=curs.fetchall()
		for row in rows:
			idx+=1
			no=row['no']
			subject=row['subject']
			date=row['date']
			no=no.replace('	','')
			subject=subject.replace('	','')
			date=date.replace('	','')
			q=str(idx)
			q+='	'
			q+=subject
			q+='	'
			q+=str(label)
			q+='\n'
			f.write(q)
		
		query='select no, subject, date from DB1 where date='
		query+="'"+str(nowdate+1)+"'"
		query+=' and '
		query+='site='
		query+="'"+_site+"'"
		query+=' order by no asc'
		curs.execute(query)
		rows=curs.fetchall()
		for row in rows:
			idx+=1
			no=row['no']
			subject=row['subject']
			date=row['date']
			no=no.replace(' ','')
			subject=subject.replace('	','')
			date=date.replace('	','')
			q=str(idx)
			q+='	'
			q+=subject
			q+='	'
			q+=str(label)
			q+='\n'
			f.write(q)
		label+=1


	f.close()
