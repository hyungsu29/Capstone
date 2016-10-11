from sqlAPI import *

connect_db()
title = query('select * from DB1')[0]['title']
print title
close_db()
'''
shpik@shpik-400-470kr:~/Capstone/sqlAPI$ python sample.py 
TEKKEN STRIKE ‘qudans’ 손병문, ‘물골드’ 한재균의 활약이 돋보인 8강 B조 경기
'''

