'''
实用unittest进行单元测试
'''
from calculator import Count
import unittest
def setUpModule():
    print("模块开始 Module\n")

def tearDownModule():
    print("模块结束 Module\n")

class TestCount(unittest.TestCase):
    def setUp(self):
        print("unittest start")
    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)
    def test_Not(self):
        j=Count(23,3)
        self.assertEqual(j.add(),26,msg="结果相等")

    def tearDown(self):
        print("unittest end")
class TestSub(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("class unittest类开始 ")
    def setUp(self):
        print("unittest sub start")
    @classmethod
    def tearDownClass(cls):
        print("class unittest tearDown类结束 ")
    def tearDown(self):
        print("unittest sub end")
    @unittest.skipIf(3>2,"跳过")
    def test_sub(self):
        j=Count(5,2)
        self.assertEqual(j.sub(),3)
        print("unittest test_sub")

    def test_sub2(self):
        j=Count(105,21)
        self.assertEqual(j.sub(),84)
        print("unittest test_sub2")

if __name__=='__main__':
      testSuit=unittest.TestSuite()
      testSuit.addTest(TestSub("test_sub"))
      testSuit.addTest(TestSub("test_sub2"))
      testSuit.addTest(TestCount("test_Not"))
      # testSuit.addTest(TestCount("test_add"))
      runner=unittest.TextTestRunner()
      runner.run(testSuit)
