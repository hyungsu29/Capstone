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
