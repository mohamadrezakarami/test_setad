from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://food.iranrahyaft.ir/app_order/order/")
# import  pdb; pdb.set_trace()
# # sleep(60)
u=driver.find_element("name",'username')
u.send_keys('mrkarami')
sleep(2)
p=driver.find_element("name",'password')
p.send_keys('mo31383138')
sleep(2)
driver.find_element("xpath","//input[@value='ورود']").click()

driver.find_element("xpath","//a[@href='/app_order/order/add/']").click()
driver.find_element("xpath","//div[@class='related-widget-wrapper']//select[1]").send_keys("چلو کباب")
driver.find_element("xpath","//label[text()='تاریخ سفارش:']/following::input").send_keys("1401-11-03")
driver.find_element("xpath","//input[@value='ذخیره']").click()
sleep(10)