#-*- coding: utf-8 -*-
import urllib
import time 
import urllib2
import os
import sys


def decodehtml(s):
    s=s.replace('&nbsp;',' ')
    s=s.replace('&lt;','<')
    s=s.replace('&gt;','>')
    s=s.replace('&amp;','&')
    s=s.replace('&quot;','"')
    s=s.replace("'","")
    s=s.replace('"','')
    s=s.replace('`','')
    
    return s.strip()

def gethtml(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
    req = urllib2.Request(url)
    req.add_header("User-agent", user_agent)

    response = urllib2.urlopen(req)
    headers = response.info().headers
    the_page = response.read()
     
    return the_page

def getdate(data):
    #ret type : list, data : year, month, day
    ret=data
    src='<div class="w_top_right">'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]

    src='<li><b>'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]

    dst='</b></li>'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()
    aa=ret.split(' ')
    ret=aa[0]
    ret=ret.replace('-','')
    return ret


def getsubject(data):
    ret=data
    src='<title>'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]

    
    dst='</title>'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()
    ret=ret.replace(' - 인하대학교','')
    ret=decodehtml(ret)
    return ret

def getno(data):
    ret=data
    src='<input name="boardSeq" value="'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]
    dst='"'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()
    return ret

def getcontents(data):
    return ''
    ret=data
    src='<td class="view">'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]


    
    dst='</tbody>'
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
    src='<a class="btn02 bCPrev" href="'
    srcidx=ret.rfind(src)
    ret=ret[srcidx+len(src):]
    dst='"'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()
    ret=decodehtml(ret)
    return 'http://www.inha.ac.kr/user/'+ret
def isdel(data):
    if(data.find("location.replace('/error/deleted/inha');")!=-1):
        return True
    return False


ourl='http://gall.dcinside.com/board/view/?id=inha&no='
nono=int(sys.argv[1])
nono+=1
nn=1000000
for i in range(0, nn):
    nono-=1
    url=ourl+str(nono)
    html=gethtml(url)
    if(isdel(html)):
        continue
    _no=nono
    _date=getdate(html)
    _subject= getsubject(html)
    _contents= getcontents(html)
    q="'"+str(_no)+"'"
    q+=","
    q+="'"+_date+"'"
    q+=","
    q+="'"+_subject+"'"
    q+=","
    q+="'','DCinside.com'"
    q+='\n'
    print q
    f=open('query.txt','a')
    f.write(q)
    f.close()
    #time.sleep(1.5)

