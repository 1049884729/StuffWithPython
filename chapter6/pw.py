#! /usr/bin/python3
# coding=utf-8
'''
if raise :
SyntaxError: Non-ASCII character '\xe5' in file pw.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
please : coding=utf-8 必须在第二行
'''


"""
口令保管箱
"""
passwords = {"email": "email_DDDDewklelsdlkaldaldfal;d", "blog": "blog+dleidlkeidkadad54552",
             "luggage": "dadfadf2aedaf2e544e!!#d"}

import sys
import pyperclip
if len(sys.argv)<2:
    print("Usage : python pw.py [account]  ,copy account password")
    sys.exit()
argv1=sys.argv[0]#第一个系统参数 默认是文件名
print(argv1)
account = sys.argv[1]

if account in passwords:
    password=passwords[account]
    pyperclip.copy(password)
    print(password)
else:
    print("账户不存在")
    sys.exit()
