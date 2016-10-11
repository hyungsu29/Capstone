from sqlAPI import *

connect_db()
title = query('select * from DB1')[0]['title']
print title
close_db()

