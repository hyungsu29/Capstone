#-*- coding: utf-8 -*-
import urllib
import pymysql 
import urllib2
import os
import sys
from cookielib import CookieJar

def decodehtml(s):
    s=s.replace('&nbsp;',' ')
    s=s.replace('&lt;','<')
    s=s.replace('&gt;','>')
    s=s.replace('&amp;','&')
    s=s.replace('&quot;','"')
    return s.strip()

def gethtml(url, cookie):
    user_agent='"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"'
    req = urllib2.Request(url)
    req.add_header("Referer",'http://m.inha.ac.kr/new_plaza/talktalkDetail.aspx?bdseq=5360907&gubun=235757&page=1&k_gubun=&k_word=&category1=') 
    req.add_header("User-agent", user_agent) # 헤더추가
    req.add_header("Cookie", cookie) # 쿠키 추가
     
    response = urllib2.urlopen(req)
    headers = response.info().headers #응답 헤더
    the_page = response.read()
     
    return the_page

def getdate(data):
    #ret type : list, data : year, month, day
    ret=data
    src='<ul id="noticeinfo"><li>'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]

    src='/'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]

    
    dst='/'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()

    year=ret[0:4]
    month=ret[5:7]
    day=ret[8:10]
    rets=list()
    rets.append(str(year))
    rets.append(str(month))
    rets.append(str(day))
    return rets

def getsubject(data):
    ret=data
    src='<h3 id="title">'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]

    dst='</h3>'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()
    
    ret=ret.strip()
    ret=decodehtml(ret)
    return ret

def getno(data):
    ret=data
    src='action="talktalkDetail.aspx?bdseq='
    srcidx=ret.rfind(src)
    ret=ret[srcidx+len(src):]
    dst='&'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()
    return ret

def getcontents(data):
    ret=data
    src='<div class="bbs_con">'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]


    
    dst='<div class="space30"></div>'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()

    while(1==1):
        delstr=ret
        src='<'
        srcidx=delstr.find(src)
        if(srcidx<0):
            break
        delstr=delstr[srcidx:]
        dst='>'
        
        dstidx=delstr.find(dst)
        delstr=delstr[:dstidx+1]
        delstr=delstr.strip()
        ret=ret.replace(delstr,'')
        

    lines=ret.split('\n')
    rets=""
    for line in lines:
        rets+=line.strip()
        if(len(line)<2):
            continue
        rets+='\n'
    rets=decodehtml(rets)
    return rets.strip()


def getprevurl(data):
    ret=data
    src='<div class="tc">'
    srcidx=ret.rfind(src)
    ret=ret[srcidx+len(src):]

    
    src='<a href="'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]
    
    dst='"'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()
    ret=decodehtml(ret)
    ret=ret[2:]
    return 'http://m.inha.ac.kr/new_plaza/'+ret

def insert(n, d, s, c):
    conn = pymysql.connect(host='localhost', user='root', password='9999', db='capstone', charset='utf8')
    curs = conn.cursor()
    que='insert into DB1 values('
    que+=str(n)
    que+=','
    que+=str(d)
    que+=','
    que+="'"+s+"',"
    que+="'"+c+"','inha.ac.kr')"
    print (que)
    curs.execute(que)
    conn.commit()
    conn.close()




url='http://m.inha.ac.kr/new_plaza/plaza_main.aspx?'
cookie='"MENUINFO=p_menu=LOGIN%2c%2fLOGIN%2fLOGIN.ASPX&c_menunm=LOGIN; ASP.NET_SessionId=no5wxk55ez5xtw45oc4qo455; MobileYn=N; LOGIN=LOGIN=&IDCHK=False&PWCHK=False&lyn=1&ID=&PW=; PUSH_CNT=0; LOGIN=LOGIN=&IDCHK=False&PWCHK=False&lyn=0&ID=&PW="'
for i in range(0, 50000):
    html=gethtml(url,cookie)
    print (html)
    break
    _no =getno(html)
    print (_no)

    _date= getdate(html)
    print (_date)

    
    _subject= getsubject(html)
    print (_subject)

    _contents= getcontents(html)
    print (_contents)
    
    url=getprevurl(html)

    #print _no
    #print _date
    #print _subject
    #print _contents
    print (url)

    
    dt=getdate(html)
    datestr=dt[0]+dt[1]+dt[2]
    print (i)
    if(len(datestr)>10):
        continue
    insert(_no,_date,_subject,_contents)
