import builtwith
import whois
import urllib3
# 正则表达式库
from urllib import request
from urllib.parse import urlparse
from urllib import robotparser
from bs4 import BeautifulSoup
import re
#使用fiddler，可以发现所有报纸日期接口：
ALL_PAPER_DATE="http://paper.zbnews.net/RB/content/datelist.aspx"

INDEX_DATE_PAPER="http://paper.zbnews.net/RB/content/"
FIRST_PAGER = 'Page01FM.htm'
START=350

# print(whois.whois(AIM_WEB))
def downloadAllPaperDate(url, num_retreies):
    '''

    :param url: 访问地址
    :param num_retreies: 尝试次数
    :return:
    '''
    try:
        result = request.urlopen(url)
        page = result.read()
        content = str(page.decode('utf-8'))
        dateList = content[content.index("[") + 1:-2].replace("\r", "").replace("\n", "").replace("\"", "").split(",")
        length = len(dateList)
        for paperDate in range(length-1-START,-1,-1):
            try:
                download(dateList[paperDate], num_retreies)
            except request.URLError as e:
                pass

    except Exception as e:
        print("download error:", e.reason)
        if num_retreies > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return downloadAllPaperDate(url, num_retreies - 1)
def download(date, num_retreies):
    '''

    :param url: 访问地址
    :param num_retreies: 尝试次数
    :return:
    '''
    try:
        url=INDEX_DATE_PAPER+date+"/"+FIRST_PAGER;
        print("dd",url)
        result = request.urlopen(url)
        page = result.read()
        content = page.decode('utf-8')
        # print(content)
        paper=get_link_Page(content)
        for version in paper:
            downloadPage(date,version.href,1)

    except request.URLError as e:
        print("download error:", e.reason)
        if num_retreies > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return download(url, num_retreies - 1)


def get_link_Page(html):
    '''
    :param html: 网页内容
    :return:获取所有版面链接和标题的列表
    '''
    soup = BeautifulSoup(html, "lxml")
    # tr = soup.find_all("a")
    tr = soup.find_all(attrs={'id': 'Z_category'})
    paperVersionSet=list()

    for link in tr:
        chidlAtag=link.find_all("a")[0] #版面获取链接标签
        title=chidlAtag.text # 获取<a>标签的值
        href=chidlAtag.get("href")#获取<a>标签的超链接
        paperVersion=PaperVersion(title,href)
        paperVersionSet.append(paperVersion)
    return paperVersionSet

class PaperVersion(object):
      def __init__(self,title,href):
          self.title=title
          self.href=href

def get_Content(url,html):
    '''
    :param html: 网页内容
    :return:
    '''
    soup = BeautifulSoup(html,"lxml")
    tr = soup.find_all('div',style="display:inline") #查找标签为div,且属性为style="display:inline"的值
    for link in tr:
        if "太极" in link:
           print(url,link.text)


def downloadPage(date,herf, num_retreies):
    '''

    :param url: 访问地址
    :param num_retreies: 尝试次数
    :return:
    '''
    try:
        url=INDEX_DATE_PAPER+"/"+date+"/"+herf;
        result = request.urlopen(url)
        page = result.read()
        content = page.decode('utf-8')
        get_Content(url,content)
    except request.URLError as e:
        print("download error:", e.reason)
        if num_retreies > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return downloadPage(url, num_retreies - 1)



# download(INDEX_DATE_PAPER, 5)
downloadAllPaperDate(ALL_PAPER_DATE,2)
