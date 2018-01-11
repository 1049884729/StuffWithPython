#! /usr/bin/python3
# coding=utf-8

import requests, os, bs4


def writeImg(imgurl):
    path = os.path.basename(imgurl)
    print(imgurl)
    re = requests.get("http:" + imgurl)
    if not os.path.exists("./downImg"):
        os.mkdir("./downImg")
    if re.status_code == requests.codes.ok:
        img = open(os.path.join('./downImg', path), 'wb')
        for buff in re.iter_content(10000):
            img.write(buff)
    img.close()


def getNetpage(url):
    re = requests.get(url)
    if re.status_code == requests.codes.ok:
        soup = bs4.BeautifulSoup(re.text, "lxml")
        tag = soup.select_one('#comic').select_one('img')
        imgUrl = tag.get('src')
        if imgUrl != None:
            writeImg(imgUrl)


url = "https://xkcd.com/"
for i in range(0, 3):
    re = requests.get(url)
    if re.status_code == requests.codes.ok:
        soup = bs4.BeautifulSoup(re.text, "lxml")
        getNetpage(url)
        nextLink = soup.select_one('a[rel="prev"]')
        url = "https://xkcd.com/" + nextLink.get('href')
        print(url)
