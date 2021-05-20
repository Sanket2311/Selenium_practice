from logging import error
import pdb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def open_browser():
    driver = webdriver.Chrome()
    return driver


def go_to_homepage(driver):
    driver.get("http://demostore.supersqa.com/")


def add_first_item_to_cart(driver):
    driver.implicitly_wait(10)
    add_item_loc = "/html/body/div/div/div/div[2]/main/ul/li[5]/a[2]"
    add_item_elem = driver.find_element(By.XPATH, value=add_item_loc)
    add_item_elem.click()


def go_to_cart(driver):
    driver.implicitly_wait(10)
    cart_loc = "/html/body/div/header/div[2]/div/nav/div[1]/ul/li[2]/a"
    cart_elem = driver.find_element(By.XPATH, value=cart_loc)
    cart_elem.click()


def check_if_item_in_cart(driver):
    try:
        driver.implicitly_wait(10)
        item_loc = "/html/body/div/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr[1]"
        item_elem = driver.find_element(By.XPATH, value=item_loc)
    except:
        raise Exception("Can't find items in the cart")


def check_if_coupon_in_cart_and_write(driver):

    try:
        driver.implicitly_wait(10)
        coupon_loc = "/html/body/div/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr[2]/td/div/input"
        coupon_elem = driver.find_element(By.XPATH, value=coupon_loc)
        coupon_elem.send_keys("SKP123")
    except:
        raise Exception("Can't find coupon field in the cart")


def click_apply(driver):

    try:
        driver.implicitly_wait(10)
        apply_button_loc = "/html/body/div/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr[2]/td/div/button"
        apply_button_elem = driver.find_element(
            By.XPATH, value=apply_button_loc)
        apply_button_elem.click()
    except:
        raise Exception("Can't find Apply button in the cart")


def validate_error(driver):
    driver.implicitly_wait(10)
    error_loc = "/html/body/div/div[2]/div/div[2]/main/article/div/div/div[1]/ul/li"
    error_elem = driver.find_element(By.XPATH, value=error_loc)

    if error_elem.is_displayed():
        print("Test Passed")

    else:
        print("Test Failed")


def quit_driver(driver):
    driver.quit()


if __name__ == "__main__":
    dr = open_browser()
    go_to_homepage(dr)
    # add_first_item_to_cart(dr)
    time.sleep(4)
    go_to_cart(dr)
    check_if_item_in_cart(dr)
    check_if_coupon_in_cart_and_write(dr)
    click_apply(dr)
    validate_error(dr)
    quit_driver(dr)
