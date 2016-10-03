#-*- coding: utf-8 -*-
import urllib
 
import urllib2
import os
import sys


def decodehtml(s):
    s=s.replace('&nbsp;',' ')
    s=s.replace('&lt;','<')
    s=s.replace('&gt;','>')
    s=s.replace('&amp;','&')
    s=s.replace('&quot;','"')
    return s.strip()

def gethtml(url, cookie):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
    req = urllib2.Request(url)
    req.add_header("User-agent", user_agent)
    req.add_header("Cookie", cookie)
    req.add_header("Host", 'www.inha.ac.kr')

    response = urllib2.urlopen(req)
    headers = response.info().headers
    the_page = response.read()
     
    return the_page

def getdate(data):
    #ret type : list, data : year, month, day
    ret=data
    src='<span><span>등록일&nbsp;&nbsp;</span>'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]
    dst='</span>'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()

    raws=ret.split('.')
    rets=list()
    rets.append(str(raws[0]))
    rets.append(str(raws[1]))
    rets.append(str(raws[2]))
    return rets

def getsubject(data):
    ret=data
    src='<div class="bbsView">'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]

    src='<h4>'
    srcidx=ret.find(src)
    ret=ret[srcidx+len(src):]

    
    dst='</h4>'
    dstidx=ret.find(dst)
    ret=ret[:dstidx]
    ret=ret.strip()
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




url="http://www.inha.ac.kr/user/boardList.do?command=view&page=7&boardId=235757&boardSeq=5340912&id=plaza_010100000000"
cookie='elevisor_for_j2ee_uid=5549439729676447256; WT_FPC=id=29bd355034caf88b89b1473250991325:lv=1473251006303:ss=1473250991325; _ga=GA1.3.1736089513.1473413238; JSESSIONID=9F71291D6966139E837702471F346291'
for i in range(0, 100):
    html=gethtml(url,cookie)
    _no =getno(html)
    _date= getdate(html)
    _subject= getsubject(html)
    _contents= getcontents(html)
    url=getprevurl(html)

    #print _no
    #print _date
    #print _subject
    #print _contents
    print url

    
    dt=getdate(html)
    datestr=dt[0]+dt[1]+dt[2]
    print i
    if(len(datestr)>10):
        continue
    mkq='mkdir '+datestr
    os.system(mkq)

    f=open('./'+datestr+'/'+_no+'.txt','w')
    f.write(_subject)
    f.write('\n')
    f.write('/**//**/')
    f.write('\n')
    f.write(_contents)
    f.close()


