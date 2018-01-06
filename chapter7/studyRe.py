# encoding=utf-8
"""
学习正则表达式
"""
import re


# 匹配电话号码：
def isPhoneNumber(testNumber):
    pattern = r"189\d{8}"  # 仅匹配189段的手机号码
    phoneRegex = re.compile(pattern)
    result = phoneRegex.search(testNumber)
    if result != None:
        print("Right:" + result.group())#获取匹配到的内容
    else:
        print("not Phone Number")


isPhoneNumber("hahah:18956478942")
isPhoneNumber("18d894561237")

"""
学习更多匹配；http://regexpal.com 或者https://www.regexpal.com/
. 	Any character except newline.
\. 	A period (and so on for \*, \(, \\, etc.)
^ 	The start of the string.
$ 	The end of the string.
\d,\w,\s 	A digit, word character [A-Za-z0-9_], or whitespace.
\D,\W,\S 	Anything except a digit, word character, or whitespace.
[abc] 	Character a, b, or c.
[a-z] 	a through z.
[^abc] 	Any character except a, b, or c.
aa|bb 	Either aa or bb.
? 	Zero or one of the preceding element.
* 	Zero or more of the preceding element.
+ 	One or more of the preceding element.
{n} 	Exactly n of the preceding element.
{n,} 	n or more of the preceding element.
{m,n} 	Between m and n of the preceding element.
??,*?,+?,
{n}?, etc. 	Same as above, but as few as possible.
(expr) 	Capture expr for use with \1, etc.
(?:expr) 	Non-capturing group.
(?=expr) 	Followed by expr.
(?!expr) 	Not followed by expr.
"""

#获取固话区号分组
def getTellPhoneArea(tellPhone):
    '''正则表达式：利用（）进行分组，有几个是几组
    groups是获取所有数组的值
    如果匹配的内容中有（，匹配时使用 \(
    '''
    pattern=r"(05\d{2})-(\d{7,})"
    phoneRegex=re.compile(pattern)
    result=phoneRegex.search(tellPhone)
    if result!=None:
        print("groups:"+str(result.groups()))
        print("group0:"+result.group(0))
        print("group1:"+result.group(1))
        print("group2:"+result.group(2))
    else:
        print("No match Phone")
getTellPhoneArea("0537-4568291")


#利用管道|匹配a或者b
def matchOr(name):
    '''利用| 匹配多选一'''
    patternAandB="a|b|c"
    result=re.compile(patternAandB).search(name)
    if result!=None:
        print("匹配成功："+result.group())
    else:
        print("匹配不成功")
matchOr("d")

#用?实现可选匹配
def optionsMath(phone):
    '''?和（）配合使用，？之前的括号内是可选匹配方案'''
    pattern=r"(\d{3,}-)?\d{7,}"
    result=re.compile(pattern).search(phone)
    if result!=None:
        print("result:"+result.group())
    else:
        print("匹配不成功")
optionsMath("7568145")
optionsMath("021-021-7568145")

"""
使用*作为匹配符时，表示*之前的分组匹配0次或多次，
使用？表示匹配0次或者1次
使用+表示1次或者多次
使用{n}匹配前面的n次数

"""

#花括号的贪心匹配和不贪心匹配

def greedMarth(name):
    """
    贪心匹配：
    系统默认贪心算法，即能匹配字符最长的，匹配最长的"""
    pattern=r"(Ha){3,5}"
    result=re.compile(pattern).search(name)
    if result!=None:
        print("greedMarth_result:"+result.group())
    else:
        print("匹配不成功")
def noGreedMarth(name):
    """
    非贪心匹配：在花括号后面加个?
    系统默认贪心算法，即能匹配字符最短的，匹配最短的"""
    pattern=r"(Ha){3,5}?"
    result=re.compile(pattern).search(name)
    if result!=None:
        print("noGreedMarth_result:"+result.group())
    else:
        print("匹配不成功")
greedMarth("HaHaHaHaHa")
noGreedMarth("HaHaHaHaHa")