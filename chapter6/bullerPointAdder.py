#! /usr/bin/python3
# coding=utf-8

'''
从黏贴板复制一段内容，并将这段内容添加无序列表
'''
import pyperclip

content = pyperclip.paste()
print("old:\n" + content)
contentSplit = content.split("\n")
for item in range(len(contentSplit)):
    contentSplit[item] = "* " + contentSplit[item]
content = "\n".join(contentSplit)
pyperclip.copy(content)
print("new:\n" + content)
