import pdb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://demostore.supersqa.com/")

expected_url = "http://demostore.supersqa.com/"

driver.implicitly_wait(10)
cart_loc = "/html/body/div/header/div[2]/div/nav/div[1]/ul/li[2]/a"
cart_elem = driver.find_element(By.XPATH, value=cart_loc)

if cart_elem.is_displayed():
    pass
else:
    raise Exception("Can't find Cart button")


driver.implicitly_wait(10)
add_item_loc = "/html/body/div/div/div/div[2]/main/ul/li[5]/a[2]"
add_item_elem = driver.find_element(By.XPATH, value=add_item_loc)

add_item_elem.click()

time.sleep(4)
cart_elem.click()


driver.implicitly_wait(10)
item_loc = "/html/body/div/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr[1]"
item_elem = driver.find_element(By.XPATH, value=item_loc)

if item_elem.is_displayed():
    pass
else:
    raise Exception("Can't find items in the cart")

driver.implicitly_wait(10)
coupon_loc = "/html/body/div/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr[2]/td/div/input"
coupon_elem = driver.find_element(By.XPATH, value=coupon_loc)

if coupon_elem.is_displayed():
    coupon_elem.send_keys("SKP123")
else:
    raise Exception("Can't find coupon field in the cart")


driver.implicitly_wait(10)
apply_button_loc = "/html/body/div/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr[2]/td/div/button"
apply_button_elem = driver.find_element(
    By.XPATH, value=apply_button_loc)

apply_button_elem.click()

driver.implicitly_wait(10)
error_loc = "/html/body/div/div[2]/div/div[2]/main/article/div/div/div[1]/ul/li"
error_elem = driver.find_element(By.XPATH, value=error_loc)

if error_elem.is_displayed():
    print("Test Passed")

else:
    print("Test Failed")

driver.quit()
