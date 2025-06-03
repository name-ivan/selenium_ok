import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    # sleep(3)
    
def test_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'new-page-link')))
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'result-text')))
    # driver.get('https://www.qa-practice.com/elements/new_tab/new_page')
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(tabs[0])

def test_stale_exception(driver):
    driver.get('https://www.qa-practice.com/elements/checkboz/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    print(checkbox.id)
    checkbox.click()
    submit = driver.find_element(By.ID, "submit-id-submit")
    print(submit.id)
    submit.click()
    assert driver.find_element(By.ID, 'result-text').text == "select me or not"
    #these 2 below won't work because selenium doesn't keep the elements in its memory anymore after the page was updated when we clickde submit the first time
    checkbox.click()
    submit.click()

