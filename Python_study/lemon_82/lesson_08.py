# 20210621-Python第八节课：UI自动化的等待和iframe切换
from selenium import webdriver #从selenium工具包导入webdriver库
import time
driver = webdriver.Chrome()    #webdriver与Chrome建立会话
driver.implicitly_wait(15)
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()
title = driver.title  #获取页面标题
if title == "柠檬ERP":
    print("标题为{}".format(title))
else :
    print("测试不通过")
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
username = driver.find_element_by_xpath("//p").text  #获取文本
if username == "测试用户" :
    print("登录成功，用户名是：{}".format(username))
else :
    print("登录失败")
driver.find_element_by_xpath("//span[text()='零售出库']").click()
id_number = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id") #获取ID属性值
print(id_number)
# driver.switch_to.frame(id_number + "-frame") #通过ID切换到iframe
driver.switch_to.frame(driver.find_element_by_id(id_number + "-frame")) #通过元素切换到iframe
driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys("448")
driver.find_element_by_xpath("//a[@id='searchBtn']//span[contains(text(),'查询')]").click()
time.sleep(10)
bill_number = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]/td[@field="number"]/div').text #获取单据编号
if "448" in bill_number :
    print("查询到的单据编号是：{}".format(bill_number))
else :
    print("测试不通过")