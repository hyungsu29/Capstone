#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import os

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

        for i in range(0,30):
            if title_no_tag[i].text == u'공지':
                continue

            title_no.append(title_no_tag[i].text)
            title.append(title_tag[i].find('a').text)
            href.append("http://gall.dcinside.com/board/view/?id=inha&no=%s&page=%d" % (title_no[-1], start_page))
            date.append(date_tag[i].text)

        start_page += 1

def make_directory():
    for i in range (len(date)):
        homeDir = os.getcwd()
        if not os.path.isdir(date[i]):
            os.mkdir(date[i])
        os.chdir(date[i])

        f = open(title_no[i]+'.txt', 'w')
        f.write(title[i].encode('utf-8'))
        f.write('\n//==========//\n')
        f.write(contents_spider(href[i]).encode('utf-8'))
        f.close()

        os.chdir(homeDir)
    return

if not os.path.isdir("Crawling"):
    os.mkdir("Crawling")
os.chdir("Crawling")

board_spider(5)
make_directory()
