import pymysql
import os
import sys
def cutstr(s):
	s=s.replace('<','')
	s=s.replace('>','')
	s=s.replace('"','')
	return s

site=sys.argv[1]
site=site.strip()
conn = pymysql.connect(host='localhost', user='root', password='9999', db='capstone', charset='utf8')

curs = conn.cursor()
curs.execute("delete from DB2 where site='"+site+"'")


f=open('result.txt','r')
lines=f.readlines()
for line in lines:
	line=cutstr(line).strip()
	if(line.find('},{')<0):
		continue
	raws=line.split(' ')
	seqnum=int(raws[0])
	wordraws=raws[1].split('},{')
	lhs=wordraws[0].replace('{','')
	rhs=wordraws[1].replace('}','')
	support=float(raws[2])
	lhslen=len(lhs.split(','))
	rhslen=len(rhs.split(','))
	flag=0
	if(lhslen==3 and rhslen==1):
		flag=1
	if(flag==0):
		continue
	sql='insert into DB2 values ('
	sql+="'"+lhs+"',"
	sql+="'"+rhs+"',"
	sql+=str(support)+','
	sql+="'"+site+"')"
	print (sql)
	curs.execute(sql)
conn.commit()
conn.close()
