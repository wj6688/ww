#导包
import unittest
#
# from jiekou_day_03_3 import api
# from jiekou_day_03_3.api.api_login import ApiLogin
# from jiekou_day_03_3.tools.assert_common import assert_common

#TestLogin继承unittest.TestCase，unittest.TestCase里有一个self地址，
import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    #初始化
    @classmethod
    def setUpClass(cls):
        #获取ApiLogin对象
        cls.login=ApiLogin()
    #登录测试方法
    def test01_login(self,mobile="13800000002",password="123456"):
        #调用业务
        r=self.login.api_login(mobile,password)
        #提取token
        token=r.json().get("data")
        api.headers['Authorization']= "Bearer " + token    #{"Authorization":"Bearer xxx"，获取value,如果值存在就更新，如果不存在，就追加
        print("登录成功后的headers值为：",api.headers)
        print(r.json())
        #断言
        assert_common(self,r)  #self地址传给assert_common里用一个变量接收   assert_common里是用self接收的，也可以用其他变量接收，例如a
