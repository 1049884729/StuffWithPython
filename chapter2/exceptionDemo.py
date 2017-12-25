
try:
    f=open("no.py","r")
    print(f.read())
except BaseException as msg:#打印具体的异常信息
    print(msg)
#正常情况下
f=open("baidu.py","r")
print(f.read())

'''
异常try except 与else和finally的配合使用
'''
try:
      print("异常测试")
except BaseException as msg:
      print(msg)
else:
      print("运行正常，无报错")
finally:
    print("不管有无异常。都执行")

'''
可以抛出异常的raise ,与Java的throw类似
raise 只能使用python提供的异常类                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
'''
def mustImpleMethod():
    raise NotImplementedError("没有实现")
print(mustImpleMethod())