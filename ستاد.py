from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from faker import Faker
fake = Faker()
names = [fake.unique.user_name() for i in range(5)]
hq_name=names[0]
hq_username=names[1]
manger_name=names[2]
manager_username=names[3]
Service=Service(executable_path=ChromeDriverManager().install())
actions= ActionChains(driver=driver)
options=webdriver.ChromeOptions()



# admin
def signin_admin_button():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("sajjad")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("asdf@1234")
    sleep(1)
    driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
    sleep(1)
    driver.find_element("xpath","//div[@class='muirtl-dufqpb']//p").click()
    c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
    assert c=="ورود به سامانه"
    get_url = driver.current_url
    assert get_url=="https://setad.iranrahyaft.ir/signin"
    d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
    assert d == "تائید و ورود"
    sleep(3)


def signin_admin_enter():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("sajjad")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("asdf@1234")
    sleep(1)
    actions.send_keys(Keys.ENTER).perform()
    sleep(1)
    driver.find_element("xpath","//div[@class='muirtl-dufqpb']//p").click()
    c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
    assert c=="ورود به سامانه"
    get_url = driver.current_url
    assert get_url=="https://setad.iranrahyaft.ir/signin"
    d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
    assert d == "تائید و ورود"
    sleep(3)


# ستاد
def signin_setad_button():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("mohsen-setad-manager")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("qazwsx12")
    sleep(2)
    driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
    sleep(3)
    driver.find_element("xpath","(//p[contains(@class,'MuiTypography-root MuiTypography-body1')])[2]").click()
    c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
    assert c=="ورود به سامانه"
    get_url = driver.current_url
    assert get_url=="https://setad.iranrahyaft.ir/signin"
    d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
    assert d == "تائید و ورود"
    sleep(3)


def signin_setad_enter():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("mohsen-setad-manager")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("qazwsx12")
    sleep(2)
    actions.send_keys(Keys.ENTER).perform()
    sleep(3)
    driver.find_element("xpath","(//p[contains(@class,'MuiTypography-root MuiTypography-body1')])[2]").click()
    c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
    assert c=="ورود به سامانه"
    get_url = driver.current_url
    assert get_url=="https://setad.iranrahyaft.ir/signin"
    d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
    assert d == "تائید و ورود"
    sleep(3)


# hq
def signin_hq_button():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("sajjad-hq")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("test1")
    sleep(2)
    driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
    sleep(5)
    driver.find_element("xpath","(//p[contains(@class,'MuiTypography-root MuiTypography-body1')])[2]").click()
    c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
    assert c=="ورود به سامانه"
    get_url = driver.current_url
    assert get_url=="https://setad.iranrahyaft.ir/signin"
    d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
    assert d == "تائید و ورود"
    sleep(3)


def signin_hq_enter():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("sajjad-hq")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("test1")
    sleep(2)
    actions.send_keys(Keys.ENTER).perform()
    sleep(5)
    driver.find_element("xpath","(//p[contains(@class,'MuiTypography-root MuiTypography-body1')])[2]").click()
    c=driver.find_element("xpath","//h5[contains(@class,'MuiTypography-root MuiTypography-h5')]").text
    assert c=="ورود به سامانه"
    get_url = driver.current_url
    assert get_url=="https://setad.iranrahyaft.ir/signin"
    d=driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").text
    assert d == "تائید و ورود"
    sleep(3)



# ساخت قرارگاه
def create_hq_by_setad():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
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
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys(hq_name)
    driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys(hq_username)
    driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]").send_keys("09190140767")
    driver.find_element("xpath","//label[text()='آدرس وبسایت']/following::input").send_keys("www.dflkjgi.com")
    # driver.find_element("xpath","//label[text()='آدرس']/following::input").send_keys("تهران نارمک")
    # driver.find_element("xpat","//div[@class='jss4 muirtl-w2tu0y']/following-sibling::main[1]").click()
    # driver.find_element("xpath","//div[@class='muirtl-1k18m4y']//button[1]").click()
    driver.find_element("xpath","//p[text()='انتخاب از نقشه']").click()
    sleep(1)
    actions.move_by_offset(300, 400).pause(1).click_and_hold().key_down(Keys.LEFT).move_by_offset(500,300).perform()
    sleep(1)
    driver.find_element("xpath","//p[text()='CONFIRM']").click()
    sleep(1)
    driver.find_element("xpath","//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("سلام قرارگاه جهادی")
    sleep(1)
    # driver.execute_script("window.scrollBy(0, document.body.scrollHeight)") 
    driver.execute_script("window.scrollBy(0,350)")
    sleep(3)
    driver.find_element("xpath","(//textarea[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]").send_keys("قرارگاه مردمی است")
    driver.find_element("xpath","//label[text()='تسهیلات اعطایی']/following::textarea").send_keys("یک میلیارد ریال")
    driver.find_element("xpath","//label[text()='ظرفیت های قرارگاه ما']/following::textarea").send_keys("250 نفر")
    driver.find_element("xpath","//label[text()='نام']/following::input").send_keys(manger_name)
    driver.find_element("xpath","//label[text()='نام کاربری']/following::input").send_keys(manager_username)
    driver.find_element("xpath","//input[@type='password']").send_keys("qazwsx12")
    driver.find_element("xpath","//label[text()='تکرار رمز عبور']/following::input").send_keys("qazwsx12")
    sleep(2)
    driver.execute_script("window.scrollBy(0,150)")
    driver.find_element("xpath","//div[@id='__next']/div[1]/div[2]/main[1]/form[1]/div[3]/button[1]").click()
    sleep(4)
    text=driver.find_element("css selector",".SnackbarContent-root").text
    assert text=="با موفقیت انجام شد"
    sleep(10)

    


# signin_admin_button()
# signin_admin_enter()
# signin_hq_button()
# signin_hq_enter()
# signin_setad_button()
# signin_setad_enter()
# create_hq_by_setad()

# === SETAD ===
# vbehdasht
# vbehdasht_manager : asdf@1234

def accept_subset_request_by_setad():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("vbehdasht_manager")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("asdf@1234")
    sleep(2)
    driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
    sleep(2)  
    driver.find_element("css selector",".toggle-btn").click()
    driver.execute_script("window.scrollBy(0,300)")
    driver.find_element("xpath","//p[text()='لیست درخواست تعلق']").click()
    sleep(1)
    driver.find_element("xpath","(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[3]").click()
    sleep(1)
    driver.find_element("xpath","//input[@class='PrivateSwitchBase-input muirtl-1m9pwf3']").click()
    sleep(2)
    element=driver.find_element("xpath","(//button[contains(@class,'MuiButtonBase-root MuiButton-root')]/following-sibling::button)[2]")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    sleep(3)
    driver.find_element("xpath","//div[@class='muirtl-1ozf7xo']//button[1]").click()
    sleep(2)
    print("^^^^^^^^^^^^^^^^^^^^")
    text=driver.find_element('css selector',".SnackbarItem-message").text
    assert text=="با موفقیت تایید شد"
    print(text)
    sleep(5)



def accept_subset_request_by_hq():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("hahmar_manager")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("asdf@1234")
    sleep(2)
    driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
    sleep(3)
    driver.find_element("css selector",".toggle-btn").click()
    sleep(2)
    driver.execute_script("window.scrollBy(0,300)")
    driver.find_element("xpath","//p[text()='* لیست درخواست تعلق']").click()
    sleep(2)



    


def create_hqmanager_by_hq():
    driver.get("https://setad.iranrahyaft.ir")
    sleep(1)
    driver.maximize_window()
    sleep(1)
    driver.find_element("xpath","//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]").send_keys("hahmar_manager")
    b=driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("asdf@1234")
    sleep(1)
    driver.find_element("xpath","//button[contains(@class,'MuiButtonBase-root MuiButton-root')]").click()
    sleep(1)
    driver.find_element("css selector",".toggle-btn").click()
    sleep(3)
    driver.find_element("xpath","//p[contains(@class,'MuiTypography-root MuiTypography-body1')]").click()
    sleep(3)
    driver.find_element("xpath","//p[text()='افزودن']").click()
    sleep(3)
     





signin_admin_button()
sleep(3)
signin_admin_enter()
sleep(3)
signin_hq_button()
sleep(3)
signin_hq_enter()
sleep(3)
signin_setad_button()
sleep(3)
signin_setad_enter()
sleep(3)
create_hq_by_setad()
create_hqmanager_by_hq()





      