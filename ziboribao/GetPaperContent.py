import builtwith
import whois
import urllib3
# 正则表达式库
from urllib import request
from urllib.parse import urlparse
from urllib import robotparser
from bs4 import BeautifulSoup
import re
AIM_WEB = 'http://paper.zbnews.net/RB/content/20180802/Page01FM.htm'
tech_used = builtwith.parse(AIM_WEB)


# print(whois.whois(AIM_WEB))

def download(url, num_retreies):
    '''

    :param url: 访问地址
    :param num_retreies: 尝试次数
    :return:
    '''
    try:
        result = request.urlopen(url)
        page = result.read()
        content = page.decode('utf-8')
        print(content)
        result = get_link_Page(content)

    except request.URLError as e:
        print("download error:", e.reason)
        if num_retreies > 0 and hasattr(e, 'code') and 500 <= e.code < 600:
            return download(url, num_retreies - 1)


def get_link_Page(html):
    '''
    :param html: 网页内容
    :return:
    '''
    soup = BeautifulSoup(html, "lxml")
    tr = soup.find_all(attrs={'id': 'Z_category'})
    for link in tr:
        get_Content(link)
        # print(BeautifulSoup(link,"lxml").a)


def get_Content(html):
    '''
    :param html: 网页内容
    :return:
    '''
    re.compile()
    print(html)

    # print("http://paper.zbnews.net/RB/content/20180802/" + html)
    # result = request.urlopen("http://paper.zbnews.net/RB/content/20180802/"+html)
    # page = result.read()
    # content = page.decode('utf-8')
    # soup = BeautifulSoup(content,"lxml")
    # tr = soup.find_all('div')
    # for link in tr:
    #     print(link)
    # return tr


download(AIM_WEB, 2)
