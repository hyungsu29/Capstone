#-*- coding: utf-8 -*-
import simplejson
import sqlAPI
import collections

sqlAPI.connect_db()
rows = sqlAPI.query("select * from DB1 limit 3;")
a = []
for i in range(len(rows)):
    d = {
            'no':rows[i]['no'],
            'title':rows[i]['title'],
            'date':rows[i]['date'],
            'content':rows[i]['content']
            }
    print d
    a.append(d)
j = simplejson.dumps(a)
objects_file = 'student_objects.js'
f = open(objects_file,'w')
print >> f, j

sqlAPI.close_db()
