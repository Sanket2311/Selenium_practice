from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.set_page_load_timeout(10)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("I love you")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.maximize_window()
time.sleep(10)
driver.refresh()
print("Test Completed successfully")
driver.quit()
