import operator
import json
import pymysql
import os
import sys
_site=sys.argv[1]
_startdate=sys.argv[2]
_enddate=sys.argv[3]


conn = pymysql.connect(host='localhost', user='root', password='9999', db='capstone', charset='utf8')
curs = conn.cursor(pymysql.cursors.DictCursor)
curs.execute("select * from DB2 where site="+"'"+_site+"' order by support desc")
rows=curs.fetchall()

d=dict()
l=list()
for row in rows:
	rhs=row['rhs']
	lhss=row['lhs'].split(',')
	d[rhs]=0
	for lhs in lhss:
		d[lhs]=0
rank=1
for row in rows:
	dd=dict()
	rhs=row['rhs']
	lhss=row['lhs'].split(',')
	dd[rhs]=1
	for lhs in lhss:
		dd[lhs]=1
	if(len(dd)!=4):
		continue
	



	if(d[rhs]!=0):
		continue
	flag=0
	for lhs in lhss:
		if(d[lhs]!=0):
			flag=1
	if(flag==1):
		continue
	d[rhs]=1
	for lhs in lhss:
		d[lhs]=1
	v=dict()
	v['rank']=str(rank)
	v['lhs']=row['lhs']
	v['rhs']=row['rhs']
	v['support']=row['support']*100.0
	v['support']=str(round(v['support'],1))
	rank+=1
	l.append(v)
for i in range(rank,6):
	v=dict()
	v['rank']=str(rank)
	v['lhs']='Unknown'
	v['rhs']='Unknown'
	v['support']='Unknown'
	l.append(v)
	rank+=1
retjson=json.dumps(l,ensure_ascii=False)
f=open('./examjson/getpredict.json','w')
f.write(retjson)
f.close()
conn.close()
