from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())



a=driver.get("https://food.iranrahyaft.ir/app_order/order/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)