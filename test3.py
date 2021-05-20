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
driver.find_element(
    By.CSS_SELECTOR, value='#top > nav > ul > li.pypi-meta > a').click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, value='#content > div.banner > div > h1')

cur_url = driver.current_url
expected_url = 'https://pypi.org/'
assert cur_url == expected_url, "Clicked but got{}".format(cur_url)

print("Test Passed")
driver.quit()
