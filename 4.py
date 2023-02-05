from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://esale.ikco.ir/#!/")
sleep(4)
driver.find_element("xpath","/html/body/div[1]/div/div[3]/div[1]/figure/a").click()
sleep(3)
driver.find_element('xpath',"(//input[contains(@class,'form-control ')])[2]").send_keys('hkjfjsdfg')
sleep(5)