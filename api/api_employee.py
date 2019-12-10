import requests

import api


class ApiEmployee:
    #初始化
    def __init__(self):
        #初始化url
        #新增员工url
        self.url_add= api.BASE_URL + "/api/sys/user"
        #修改，删除，通用url   {}:是占位符，解决不同参数问题
        self.url_employee=api.BASE_URL+"/api/sys/user/{}"
    #添加员工
    def api_post_employee(self,username,mobile,workNumber):
        #定义json数据   动态：传参
        data={
              "username":username,
              "mobile":mobile,
              "workNumber":workNumber}
        #调用post方法，必须return
        return requests.post(url=self.url_add,json=data,headers=api.headers)   #在__init__里面

    #修改员工 put   根据test02_employee新增员工哪获取的员工api.user_id,来修改username
    def api_put_employee(self,username):
        #定义json数据 动态：传参
        data={"username":username}
        return  requests.put(url= self.url_employee.format(api.user_id),json=data,headers=api.headers)


    #查询员工 get   不用数据data，直接用获取的api.user_id查询
    def api_get_employee(self):
        return requests.get(url= self.url_employee.format(api.user_id),headers=api.headers)

    #删除员工   （注意：解决url{}问题）
    def api_delete_employee(self,user_id):
        return requests.delete(url=self.url_employee.format(user_id),headers=api.headers)