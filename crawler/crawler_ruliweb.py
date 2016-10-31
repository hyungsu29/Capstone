#!/usr/bin/python

#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import os
import sqlAPI
reload(sys)
sys.setdefaultencoding('utf-8')

# Default information
page=1
URL = "http://bbs.ruliweb.com/news?page="

# Parser
def get_title(original):
    return original.h4.text

def get_date(original):
    return original.div.div.text.split('|')[2][4:14].strip().replace('.','')

def get_content(original):
    p = str(original).find('</span>')
    q = str(original).find('<div class="row">')
    return str(original)[p+7:q].replace('<br>','')

def parser(parser_url):
    parser_r = requests.get(parser_url)
    if str(parser_r.status_code)=='200':
        parser_text = parser_r.text
        parser_soup = BeautifulSoup(parser_text,'html.parser')
        article = parser_soup.find_all('div',{"class":"news_title_wrapper row"})
        title = get_title(article[0])
        date = get_date(article[0])
        article_content = parser_soup.find_all('div',{'class':'news_content_wrapper row'})
        content = get_content(article_content[0]) 
        return title,date,content

# Crawler
def crawl(search_date,url):
    global page
    title = ''
    date = ''
    content = ''
    no = ''
    cnt = 0
    r = requests.get(url)
    res = r.text
    soup = BeautifulSoup(res,'html.parser')
    repo_list = soup.find_all('div',{"class":"title_wrapper row"})
    for i in repo_list:
        try:
            cnt += 1
            if cnt<6:
                continue
            tmp = i.a['href']
            if tmp.find('news')>5:
                no = str(tmp)[str(tmp).find('read/')+5:]
                title,date,content = parser(tmp)
            else:
                continue
        except:
            continue
        finally:
            if(str(date).strip()==str(search_date).strip()):
                sys.exit()
            '''
            os.chdir(os.getcwd())
            if not os.path.isdir('./'+str(date)):
                os.system('mkdir '+str(date))
            f=open('./'+str(date)+'/'+str(no)+'.txt','w')
            f.write(str(title))
            f.write('\n')
            f.write('/**//**/')
            f.write('\n')
            f.write(str(content))
            f.close()
            '''
            sqlAPI.in_db1(str(no),str(title),str(content),str(date))
    page += 1
    crawl(search_date,URL+str(page))

if __name__=="__main__":
    sqlAPI.connect_db()
    crawl(sys.argv[1],URL+str(page))
    sqlAPI.close_db()
