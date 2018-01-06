'''原始字符串：r忽略所有的转义字符'''

sr=r"That is Carol\' ;\ncat"
print(sr)
"""
多行注释
"""

#字符串使用 in 和 not in

sr="hello world"
print("hello"in sr)
print("hellDD" not in sr)

def getAge():
    while True:
        print("input your age:")
        age=input()
        if age.isdecimal():
            break
        print("please enter a number for your age.")
    while True:
        print("enter a password,the password must be consist of number and letters")
        password=input()
        if password.isalnum():
            break
        print("please again enter a password,the password must be consist of number and letters")
    print("your age is:"+age +" and your password is:"+password)

# getAge()

print("hello".startswith("h"))
print("hello".endswith("h"))
"""字符串 join 和 split"""
set=["my","name","is "," hah"]
str=" ".join(set)
print(str)#将数组拼成字符串
print(str.split(" "))#拆成列表

spam="  hello   world  "
#删除空白符
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

"""
使用黏贴板，需要使用pip 安装 pyperclip
"""
import pyperclip
# pyperclip.copy("hello")
copy =pyperclip.paste()
"""
如果在linux下，"Pyperclip could not find a copy/paste mechanism for your system. "
解决：
sudo apt-get install xsel xclip 
pip install gtk PyQt4但是pip 安装会失败,所以去pypip下载之后本地安装
pygtk-2.24.0.tar.bz2


On Linux, this module makes use of the xclip or xsel commands, which should come with the os. Otherwise run "sudo apt-get install xclip" or "sudo apt-get install xsel" (Note: xsel does not always seem to work.)

Otherwise on Linux, you will need the gtk or PyQt4 modules installed.

"""
print(copy)