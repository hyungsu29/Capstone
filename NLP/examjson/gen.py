import json
data=[
{"rank":"1","keyword":"1등","freq":"1000","percent":"10.10"},
{"rank":"2","keyword":"2등","freq":"900","percent":"9.9"},
{"rank":"3","keyword":"3등","freq":"800","percent":"8.8"},
{"rank":"4","keyword":"4등","freq":"700","percent":"7.7"},
{"rank":"5","keyword":"5등","freq":"600","percent":"6.6"},
{"rank":"6","keyword":"6등","freq":"500","percent":"5.5"},
{"rank":"7","keyword":"7등","freq":"400","percent":"4.4"},
{"rank":"8","keyword":"8등","freq":"300","percent":"3.3"},
{"rank":"9","keyword":"9등","freq":"200","percent":"2.2"},
{"rank":"10","keyword":"10등","freq":"100","percent":"1.1"}


]
print (data)
f=open('gettable.json','w')
f.write(json.dumps(data,ensure_ascii=False))
f.close()
