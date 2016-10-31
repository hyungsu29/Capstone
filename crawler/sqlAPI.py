#-*- coding: utf-8 -*-
__author__ = "shpik.korea@gmail.com"

import pymysql
import sys

# Don't touch variable
reload(sys)
sys.setdefaultencoding('utf-8')
curs = 0
sql = 0
filtering = {'drop','load_file','--','#','/'}

def get_cursor(sql):
    global curs 
    curs = sql.cursor()

def connect_db():
    global sql
    try:
        sql = pymysql.connect(host='165.246.44.144',port=55555,user='capstone',passwd='qwer1234',db='Trend', charset='utf8',cursorclass=pymysql.cursors.DictCursor,autocommit=True)
    except:
        sys.exit('[*] database connect error!\n[+] Check your database server.\n')
    finally:
        get_cursor(sql)


def in_db1(no,title,content,date):
    global curs
    if no=='':
        return -1
    _query = "insert into DB1 (no, title, content, date) values ('"+no.replace("'",'')+"','"+title.replace("'",'')+"','"+content.replace("''",'')+"','"+date.replace("'",'')+"')"
    try:
        curs.execute(_query)
    except pymysql.InternalError as error:
        print error.args
        return -1
    finally:
        return 1

def in_db2(self):
    return 0

def query(_query):
    global curs
    global filtering
    if _query in filtering:
        return "[!] Do not hacking!\n"
    try:
        curs.execute(_query)
    except pymysql.InternalError as error:
        print error.args
        return -1
    finally:
        rows = curs.fetchall()
        return rows

def close_db():
    global sql
    sql.close()


