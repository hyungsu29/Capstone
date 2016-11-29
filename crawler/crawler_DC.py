#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import os
import re
from sqlAPI import *
title_no = []
title = []
href = []
date = []

def contents_spider(href):
    if href == "null":
        contents = "null contents"
    else:
        contents_url = href
        contents_code = urllib.urlopen(contents_url)
        contents_soup = BeautifulSoup(contents_code, 'lxml')
        contents = contents_soup.find('td').text
    return contents

def board_spider(max_page):
    start_page = 1
    while start_page <= max_page:
        url = "http://gall.dcinside.com/board/lists/?id=inha&page=" + str(start_page)
        source_code = urllib.urlopen(url)
        soup = BeautifulSoup(source_code, "lxml")
        title_no_tag = soup.findAll('td', attrs={"class": "t_notice"})
        title_tag = soup.findAll('td', attrs={'class': 't_subject'})
        date_tag = soup.findAll('td',attrs={'class':'t_date'})

        for i in range(0,29):
            if title_no_tag[i].text == u'공지':
                continue

            title_no.append(title_no_tag[i].text)
            title.append(title_tag[i].find('a').text)
            href.append("http://gall.dcinside.com/board/view/?id=inha&no=%s&page=%d" % (title_no[-1], start_page))
            date.append(date_tag[i].text)

        start_page += 1

def make_directory():
    for i in range (len(date)):
        '''
        str = date[i]   # -- 창현이의 부탁으로 인해 yyyymmdd로 바꾸기 위한 작업
        strs = re.sub('[.]', '', str)

        if not os.path.isdir(strs):
            os.mkdir(strs)
        os.chdir(strs)

        f = open(title_no[i]+'.txt', 'w')
        f.write(title[i].encode('utf-8'))
        f.write('\n//==========//\n')
        f.write(contents_spider(href[i]).encode('utf-8'))
        f.close()

        os.chdir(homeDir)
        '''
        in_db1(str(title_no[i]),str(title[i]),str(contents_spider(href[i])),str(date[i]))
    return


connect_db()
if not os.path.isdir("Crawling"):
    os.mkdir("Crawling")
os.chdir("Crawling")

board_spider(100) # 몇 페이지를 크롤링 할 것인가? 사용자는 여기만 수정하면 됨.


make_directory()
close_db()

