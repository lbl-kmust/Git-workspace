
from selenium import webdriver
from commen import method #从Python package 导入定义好的函数
from testdata import data
driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = data.data_01["url"]
name = data.data_01["name"]
password = data.data_01["password"]
keys = data.data_01["keys"]
result = method.search_fun(driver=driver,url=url,name=name,password=password,keys=keys)
if "448" in result :
    print("测试结果PASS，单据号是：{}".format(result))
else :
    print("测试结果FAIL")