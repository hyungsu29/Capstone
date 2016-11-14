import json
data={"Frequency":"1234"}
print (data)
f=open('getdata.json','w')
f.write(json.dumps(data,ensure_ascii=False))
f.close()
