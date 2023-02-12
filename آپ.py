from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

actions= ActionChains(driver=driver)
options=webdriver.ChromeOptions()
driver.implicitly_wait(10)

driver.get("https://asanpardakht.ir/")
driver.maximize_window()
sleep(5)
driver.find_element("xpath","//a[contains(@class,'nav-link dropdown-toggle')]").click()
sleep(2)
driver.find_element('xpath',"//a[@class='dropdown-item']").click()
sleep(4)

