"""读取csv文件"""
import csv

date=csv.reader(open("/home/xuff/文档/tempfile/test.csv","r"))
for line in date:
    print(line)