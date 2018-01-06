"""读取csv文件"""
import csv

date=csv.reader(open("/home/xuff/文档/tempfile/test.csv","r"))
for line in date:
    print(line)

"""读取excel文件 xlrd"""

"""读取xml"""
from xml.dom import minidom

dom=minidom.parse("/home/xuff/文档/tempfile/test.xml")
root=dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)