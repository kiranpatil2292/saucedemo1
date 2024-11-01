from selenium import webdriver

import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10) # seconds  # implicit wait

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,'q')

searchbox.send_keys("Selenium")
searchbox.submit()


driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.quit()

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('www.google.com')
driver.implicitly_wait(10)
driver.find_element((By.XPATH,""))