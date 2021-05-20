from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("http://www.fb.com")
driver.maximize_window()

# target username
driver.refresh()
driver.find_element(By.CSS_SELECTOR, value='#email').send_keys(
    "sanket.skp@gmail.com")
driver.find_element(By.CSS_SELECTOR, value='#pass').send_keys("sanketdcool")
driver.implicitly_wait(10)
driver.find_element(
    By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

# driver.minimize_window()

time.sleep(10)
driver.quit()
