import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    # chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)

def test_scroll(driver):
    driver.get("https://www.onliner.by/")
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

def test_scroll_to_element(driver):
    driver.get('https://the-internet.herokuapp.com/')
    link = driver.find_element(By.LINK_TEXT, 'JQuery UI Menus')
    driver.execute_script('arguments[0].scrollIntoView();', link)

def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    submit = driver.find_element(By.ID, 'file-submit')
    path_to_cat_img = r'C:\Users\wits\Desktop\Projects\Sel_OK\selenium_ok\lesson_5\images.jpg'
    upload.send_keys(path_to_cat_img)
    submit.click()


