ss = ''

f = open('R.csv','r')
f2 = open('Rt.csv','w')
	
lines = f.readlines()
for line in lines:
	print('ing...')
	ss += line + ss
f.close()
f2.write(ss)
f2.close()
