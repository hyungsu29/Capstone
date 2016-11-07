import pymysql

f=open('result.txt','r')
lines=f.readlines()
i=-1
dt=dict()
def cutword(s):
	s=s.replace('"','')
	s=s.replace('{','')
	s=s.replace('}','')
	return s



for line in lines:
	i+=1
	if(i==0):
		continue
	line=cutword(line)
	raws=line.strip().split(' ')
	rawlhs=raws[1]
	lhss=rawlhs.split(',')
	if(len(lhss)!=3):
		continue
	print (raws)
	lhs=rawlhs
	rhs=raws[3]
	support=float(raws[4])
	confidence=float(raws[5])
	lift=float(raws[6])
	if(lift<=1.0):
		continue
	dt[rhs]={}
	dt[rhs]['lhs']=lhs
	dt[rhs]['support']=support
	dt[rhs]['confidence']=confidence
	dt[rhs]['lift']=lift
#print(dt)
i=-1

conn = pymysql.connect(host='localhost', user='root', password='9999',
                       db='capstone', charset='utf8')
 
curs = conn.cursor()
curs.execute('delete from DB2')
for line in lines:
	i+=1
	if(i==0):
		continue
	line=cutword(line)
	raws=line.strip().split(' ')
	rawlhs=raws[1]
	lhss=rawlhs.split(',')
	if(len(lhss)!=3):
		continue
	lhs=rawlhs
	rhs=raws[3]
	support=float(raws[4])
	confidence=float(raws[5])
	lift=float(raws[6])
	if(lift<=1.0):
		continue
	sql='insert into DB2 values ('
	sql+="'"+lhs+"',"
	sql+="'"+rhs+"',"
	sql+=str(support)+','
	sql+=str(confidence)+','
	sql+=str(lift)+')'
	print (sql)
	curs.execute(sql)
	#print (lhs+' '+rhs+' '+str(support)+' '+str(confidence)+' '+str(lift))

conn.commit()
conn.close()

