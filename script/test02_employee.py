import unittest

# from jiekou_day_03_3 import api
# from jiekou_day_03_3.api.api_employee import ApiEmployee
#
#
# from jiekou_day_03_3.tools.assert_common import assert_common



from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from tools.read_txt import read_txt


class TestEmployee(unittest.TestCase):
    #初始化
    @classmethod
    def setUpClass(cls):

        cls.api_employee= ApiEmployee()
    #新增员工
    @parameterized.expand(read_txt("employee_post.txt"))
    def test01_post(self,username,mobile,workNumber):
     #调用新增员工接口
         r=self.api_employee.api_post_employee(username,mobile,workNumber)
     #提取id
         api.user_id=r.json().get("data").get("id")   #以json读取获取data里的id
         print("新增员工的id为：",api.user_id)

     #断言
         assert_common(self,r)
    #更新
    def test02_put(self,username="bc1489"):
     #调用更新员工接口
         r=self.api_employee.api_put_employee(username)
         print("更新员工的名称结果为：",r.json())
    #断言
         assert_common(self,r)
    #查询
    def test03_get(self):
        r=self.api_employee.api_get_employee()
        print("查询员工信息为：",r.json())
    #断言
        assert_common(self,r)

    #删除
    def test04_delete(self):
         #调用删除业务方法
         r=self.api_employee.api_delete_employee(api.user_id)
         print("删除数据结果为：",r.json())
         #断言
         assert_common(self, r)

     #