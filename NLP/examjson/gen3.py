import json
data=[
{"rank":"1","lhs":"가,나,다","rhs":"라","support":"50.5"},
{"rank":"2","lhs":"마,바,사","rhs":"아","support":"40.4"},
{"rank":"3","lhs":"아,자,차","rhs":"카","support":"30.3"},
{"rank":"4","lhs":"타,파,하","rhs":"가가","support":"20.2"},
{"rank":"5","lhs":"나나,다다,라라","rhs":"마마","support":"10.1"}



]
print (data)
f=open('getpredict.json','w')
f.write(json.dumps(data,ensure_ascii=False))
f.close()
