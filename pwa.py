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

def no_mony_cant_particpation():

    driver.get("https://pwa.iranrahyaft.ir/")
    sleep(2)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//button[text()='لیست']").click()
    sleep(1)
    driver.find_element("xpath","//a[@href='/project-profile/63e222b51900489e78d40bff']").click()
    sleep(5)
    driver.find_element("xpath","//button[text()='مشاركت پروژه']").click()
    sleep(5)
    driver.find_element("xpath","//input[@type='number']").send_keys(5)
    sleep(4)
    driver.find_element("xpath","//button[text()='ثبت مشارکت']").click()
    sleep(5)
    a=driver.find_element("xpath","//p[text()=':) پول نداری']").text
    print(a)
    assert a ==":) پول نداری"
    print(2)

def particpation():
    driver.get("https://pwa.iranrahyaft.ir/")
    sleep(2)
    driver.set_window_size(390,800)
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a[2]").click()
    sleep(5)
    driver.find_element("xpath","//button[text()='تشکل']").click()
    sleep(3)
    driver.find_element("xpath","//input[contains(@class,'w-full rounded-lg')]").send_keys("09920167175")
    sleep(3)
    driver.find_element("xpath","//button[text()='ارسال کد']").click()
    sleep(5)
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1111")
    sleep(5)
    driver.find_element('xpath',"//button[contains(@class,'z-[1003] absolute')]").click()
    sleep(5)
    driver.find_element("xpath","//a[contains(@class,'w-full text1422600')]").click()
    sleep(5)
    driver.find_element("xpath","//button[text()='مشاركت پروژه']").click()
    sleep(5)
    driver.find_element("xpath","//button[text()='حضور در رویداد']").click()
    sleep(5)
    driver.find_element("xpath","//button[text()='ثبت مشارکت']").click()
    sleep(5)
    b=driver.find_element('xpath',"//h3[contains(@class,'text1222400 text-black1')]").text
    assert b =="در انتظار تایید مشارکت"
    sleep(5)
    driver.find_element("xpath","//*[@id='__next']/section/div/div").click()
    sleep(5)
    driver.find_element("xpath","//button[text()='مدیریت پروژه']").click()
    sleep(5)
    driver.find_element("xpath","//div[contains(@class,'border-[1px] border-gray2')]/following-sibling::div").click()
    sleep(5)
    driver.find_element("xpath","//button[text()='تایید می کنم']").click()
    sleep(5)



def asign_responsobility():
    driver.get("https://pwa.iranrahyaft.ir/")
    sleep(4)
    driver.set_window_size(390,800)
    sleep(1)
    driver.find_element("xpath","//*[@id='__next']/section/div[4]/section/div[3]/a[2]").click()
    sleep(5)
    driver.find_element("xpath","//button[text()='تشکل']").click()
    sleep(3)
    driver.find_element("xpath","//input[contains(@class,'w-full rounded-lg')]").send_keys("09920167175")
    sleep(3)
    driver.find_element("xpath","//button[text()='ارسال کد']").click()
    sleep(5)
    driver.find_element("xpath","(//input[@type='tel'])[2]").send_keys("1111")
    sleep(5)
    driver.find_element('xpath',"//button[contains(@class,'z-[1003] absolute')]").click()
    sleep(3)
    driver.find_element("xpath","//a[contains(@class,'w-full text1422600')]").click()
    sleep(3)
    driver.find_element("xpath","//button[text()='مدیریت پروژه']").click()
    sleep(3)
    driver.find_element("xpath","//button[text()='اعطای مسئولیت']").click()
    sleep(5)
    driver.find_element("xpath","(//input[contains(@class,'w-full rounded-lg')])[2]").send_keys("ُسلام")
    # import pdb; pdb.set_trace()
    driver.find_element("xpath","//div[text()='انتخاب کنید']").click()
    sleep(1)
    driver.find_element("css selector",".css-10wo9uf-option").click()
    driver.find_element("xpath","//textarea[contains(@class,'w-full rounded-lg')]").send_keys('fgjkldgjskdgsdkjfvshshfsd')
    sleep(4)
    driver.find_element("xpath","//button[text()='ارسال مسئولیت']").click()
    sleep(6)
    driver.get("https://pwa.iranrahyaft.ir/notifications")
    sleep(2)
    driver.find_element("xpath","//button[text()='اعلانات']").click()
    sleep(3)
    driver.find_element("xpath","//button[text()='تایید مسئولیت']").click()
    sleep(6)


 
 


asign_responsobility()