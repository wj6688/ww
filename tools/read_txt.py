def read_txt(filename):
    with open("./data/"+filename,"r",encoding="utf-8") as f:
        arr=[]
        for data in f.readlines():  #遍历所有行
            arr.append(tuple(data.strip().split(","))) #转换为tuple [('bi1703', '13467893214', '6688')]
        return arr[1::] #取下标为1的数据

#测试数据
print(read_txt("employee_post.txt"))
"""
        strip: 去除字符串前后空格、换行符
        split("字符"): 以指定字符分隔字符串，并 以列表的形式返回
    """