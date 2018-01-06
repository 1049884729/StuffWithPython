'''
该类生产，是为单元测试test.py所需要而编写
'''
class Count(object):
    def __init__(self,a,b):
        self.a=int(a);
        self.b=int(b)

    def add(self):
        return self.b+self.a
    def sub(self):
        return self.a-self.b

