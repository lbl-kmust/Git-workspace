import time

def open_web(driver,url) :
    driver.get(url)
    driver.maximize_window()

def login_web(driver,name,password) :
    driver.find_element_by_id("username").send_keys(name)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()

def search_fun(driver,url,name,password,keys) :
    open_web(driver,url)
    login_web(driver,name,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    id_number = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")  # 获取ID属性值
    driver.switch_to.frame(id_number + "-frame") #通过ID切换到iframe
    driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys(keys)
    driver.find_element_by_xpath("//a[@id='searchBtn']//span[contains(text(),'查询')]").click()
    time.sleep(10)
    bill_number = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]/td[@field="number"]/div').text  # 获取单据编号
    return bill_number
