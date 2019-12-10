#导包
import unittest
#定义测试套件

from tools.HTMLTestRunner import HTMLTestRunner

suite=unittest.defaultTestLoader.discover("./script")
#获取报告存储文件流并实例化HtmlTestRunner
with open("./report/report.html","wb")as f:
    HTMLTestRunner(stream=f).run(suite)