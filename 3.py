from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")


driver.get("https://www.digikala.com/landing/camp_tools/?&promo_name=%DA%A9%D9%88%D9%84%D9%87+%D9%88+%D9%84%D9%88%D8%A7%D8%B2%D9%85+%DA%A9%D9%85%D9%BE&promo_position=home_slider_new_v2&promo_creative=137625&bCode=137625")
sleep(3)
# import  pdb; pdb.set_trace()
a=driver.find_element('xpath',"//div[contains(@class,'color-500 d-flex')]").click()
sleep(2)
driver.find_element('xpath','//*[@id="modal-root"]/div[6]/div/div/div/div/div[1]/div/div/div/div/span/label/div/div/input').send_keys('موبایل')





sleep(60)