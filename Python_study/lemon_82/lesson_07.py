# 第七节课：python UI自动化和元素定位
from selenium import webdriver #从selenium工具包导入webdriver库
import time
driver = webdriver.Chrome()    #webdriver与Chrome建立会话
# driver.get("https://www.baidu.com/")  #打开百度网页
# time.sleep(2)  #等待2秒
# driver.maximize_window() #窗口最大化
# time.sleep(2)
# driver.get("https://www.taobao.com/")
# time.sleep(2)
# driver.back() #后退
# time.sleep(2)
# driver.forward() #前进
# time.sleep(2)
# driver.refresh() #刷新
# driver.close() #关闭窗口
driver.get("http://erp.lemfix.com/login.html")
driver.implicitly_wait(15)
driver.maximize_window()
title = driver.find_element_by_xpath("//b[text()='柠檬ERP']").text
if title == "柠檬ERP":
    print("标题为{}".format(title))
else :
    print("测试不通过")
# driver.find_element_by_id("username").send_keys("test123")
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_id("btnSubmit").click()
# driver.find_element_by_xpath("//span[text()='零售出库']").click()
# driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys("314")
# driver.find_element_by_xpath("//a[@id='searchBtn']//span[contains(text(),'查询')]").click()