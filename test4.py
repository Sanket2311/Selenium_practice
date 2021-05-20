import pdb
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

cur_title = driver.title
expected_title = "Welcome to Python.org"

if cur_title != expected_title:
    raise Exception("Wrong title..Current title {}".format(cur_title))

driver.implicitly_wait(10)
search_field_loc = '#id-search-field'
search_field_elm = driver.find_element(By.CSS_SELECTOR, value=search_field_loc)
search_field_elm.send_keys("numpy")

go_button_loc = "#submit"
go_button_elm = driver.find_element(By.CSS_SELECTOR, value=go_button_loc)
go_button_elm.click()

first_element_xpath = '//*[@id="content"]/div/section/form/ul/li[1]'
first_elem = driver.find_element(
    By.XPATH, value='//*[@id="content"]/div/section/form/ul/li[1]')


if first_elem.is_displayed():
    print("Test Passed")
else:
    raise Exception("After searching result not displayed")

driver.quit()
