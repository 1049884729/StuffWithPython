"""
shutil 模块:文件的复制/移动，改名 删除
"""
import shutil,os
# os.chdir("/home/xuff")

os.chdir("/home/xuff/test/")
#"""retree方法比较文献"""
# shutil.rmtree()

import zipfile
os.chdir("/media/xuff/study/codeSpace/PythonTestResource")
examplezip=zipfile.ZipFile("home.zip","w")
examplezip.write("home.txt")
print(os.listdir("."))

"""
使用send2trash 模块 安全删除
该模块需要 pip install send2trash
"""
# import send2trash
# send2trash.send2trash("./tempt.txt")
