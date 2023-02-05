from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

actions= ActionChains(driver=driver)

driver.get("https://setad.iranrahyaft.ir")
sleep(1)
driver.maximize_window()
sleep(1)
# driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("sajjad")
# b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("asdf@1234")
# sleep(1)
# # driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
# actions.send_keys(Keys.ENTER).perform()
# sleep(1)
# driver.find_element("xpath","//div[@class='muirtl-dufqpb']//p").click()
# c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
# assert c=="ورود به سامانه"
# get_url = driver.current_url
# assert get_url=="https://setad.iranrahyaft.ir/signin"
# d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
# assert d == "تائید و ورود"
# sleep(3)

# ستاد
# driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("mohsen-setad-manager")
# b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("qazwsx12")
# sleep(2)
# driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
# actions.send_keys(Keys.ENTER).perform()
# sleep(3)
# driver.find_element("xpath","(//p[contains(@class,'MuiTypography-root MuiTypography-body1')])[2]").click()
# c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
# assert c=="ورود به سامانه"
# get_url = driver.current_url
# assert get_url=="https://setad.iranrahyaft.ir/signin"
# d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
# assert d == "تائید و ورود"
# sleep(3)


# hq
# driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("sajjad-hq")
# b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("test1")
# sleep(2)
# driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
# # actions.send_keys(Keys.ENTER).perform()
# sleep(5)
# driver.find_element("xpath","(//p[contains(@class,'MuiTypography-root MuiTypography-body1')])[2]").click()
# # c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
# # assert c=="ورود به سامانه"
# # get_url = driver.current_url
# # assert get_url=="https://setad.iranrahyaft.ir/signin"
# # d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
# # assert d == "تائید و ورود"
# sleep(3)


# ساخت قرارگاه
driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("mohsen-setad-manager")
b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("qazwsx12")
sleep(1)        
driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
actions.send_keys(Keys.ENTER).perform()
sleep(1)
driver.find_element("css selector",".toggle-btn").click()
sleep(1)
driver.get("https://setad.iranrahyaft.ir/setad/hq/list")
sleep(1)
driver.find_element("xpath","//p[text()='افزودن زیرمجموعه قرارگاه']").click()
sleep(2)
driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("ابوتراب")
driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("محمدرضا")
driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]").send_keys("09190140767")
driver.find_element("xpath","//label[text()='آدرس وبسایت']/following::input").send_keys("www.dflkjgi.com")
driver.find_element("xpath","//label[text()='آدرس']/following::input").send_keys("تهران نارمک")
driver.find_element("xpath","//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("سلام عزیزکم")
sleep(1)
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)") 
driver.execute_script("window.scrollBy(0,350)")
sleep(10)