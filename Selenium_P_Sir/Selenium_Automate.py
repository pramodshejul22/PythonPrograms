#Day1- Selenium-
# Test cases
#Open web browser in (Chrome/firefox/IE)
#open URL - https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#provide email (admin@yourstore.com)
#provide password (admin)
#Click on Login
#Capture title of ths dashboard page.(Actual title)
#Verify title of the page: Dashboard(Expected title)
#close the browser
######################################################################################################
import time

#Webdriver is module, which is available in selenium package.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
#
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
# time.sleep(5)
# driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
# time.sleep(5)
# driver.find_element(By.XPATH,'//button[@type="submit"]').click()
# time.sleep(5)
#
# act_title=driver.title
# exp_title="OrangeHRM"
#
# if act_title==exp_title:
#     print("Login test passed")
# else:
#     print("Login test failed")
#
# driver.close()
# time.sleep(5)

#o/p  -  Login test passed

###########################################################################################

#Assignment Test


# Test cases
#Open web browser in (Chrome/firefox/IE)
#open URL - https://demo.nopcommerce.com/login?returnUrl=%2F
#provide email (shejul.pramod22@gmail.com)
#provide password (admin)
#Click on Login
#Capture title of ths dashboard page.(Actual title)
#Verify title of the page: Dashboard(Expected title)
#close the browser
####################################################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="Email"]').send_keys("shejul.pramod22@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,'//input[@id="Password"]').send_keys("pune@1234")
time.sleep(3)
driver.find_element(By.XPATH,'//button[contains(text(),"Log in")]').click()  #//button[text()='Log in']

act_title=driver.title
exp_title='Just a moment...'
print(driver.title)

if act_title==exp_title:
    print("Login test passed successfully")
else:
    print("Login test failed")
driver.close()

#Test passed successfully