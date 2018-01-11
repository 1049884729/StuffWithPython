#! /usr/bin/python3
#coding=utf-8

'''
#知识点1：webbrowser 打开网页
import webbrowser,sys
size=len(sys.argv)
if size<2:
    print("没有任何搜索内容在github中,one is owner,two is projectname")
urlappend="/"
if size==2:
    urlappend+=sys.argv[1]
elif size==3:
    urlappend+=sys.argv[1]+"/"+sys.argv[2]
else:
    urlappend+="android"
    #用webbrowser打开网页
webbrowser.open("http://github.com"+urlappend)
'''

"""
知识点2：用模块requests 下载web文件
需要安装模块：sudo pip install requests
"""
import requests,os
# url="http://p0.so.qhimgs1.com/t01aa7378e6f2c96450.jpg"
def downloadImg(url):
    re=requests.get(url)
    path=os.path.basename(url)#获取url的基本文件名
    if re.status_code==requests.codes.ok:
        img=open(os.path.join("./",path),"wb")
        for chunk in re.iter_content(10000):#每次写入的缓存大小
            img.write(chunk)
        img.close()

"""
知识点3：用BeautifulSoup 模块解析Html
 BeautifulSoup 需要安装,模块简写：bs4 (Beautiful Soup 第四版)
"""
import bs4
repic=requests.get("https://helentang.tuchong.com/")
if repic.status_code==requests.codes.ok:
    content=repic.text
    soup=bs4.BeautifulSoup(content,"lxml")
    imgs=soup.select("img")
    for img in imgs:
        try:
            imgurl=str(img.attrs.get("src"))
            if imgurl != None  :
                 if imgurl.startswith("//"):
                     imgRealUrl=imgurl.replace("//","http://")
                     print(imgRealUrl)
                     downloadImg(imgRealUrl)
        except:
            pass