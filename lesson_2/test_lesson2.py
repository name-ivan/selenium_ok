import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)

def test_id_name(driver):
    input_data = "cat"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    #text_string = driver.find_element(By.ID, "id_text_string")
    text_string = driver.find_element(By.CLASS_NAME, "form-control")
    text_string.send_keys(input_data)
    #text_string.submit()
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.CLASS_NAME, "result-text")
    assert result_text.text == input_data 

def test_tag_name(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Input field'
    
def test_linked_text(driver):
    driver.get("https://www.qa-practice.com/")
    driver.execute_script("window.scrollBy(0, 1080)")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact")))
    contact_link = driver.find_element(By.LINK_TEXT, "Contact")
    contact_link.click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'
    
#if there is no name or ID and other ways can't work too
def test_css_selector(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    #to search by selector in the devtools -> html select the code of the element and click ctrl + F and search in [] 
    #text_string = driver.find_element(By.CSS_SELECTOR, '[placeholder = "Submit me"]')
    #put the . in front
    text_string = driver.find_element(By.CSS_SELECTOR, '.form-control')
    text_string.send_keys('input_data')
    #text_string.send_keys(Keys.ENTER)
    print(text_string.value_of_css_property('border-color'))
    assert text_string.get_attribute('placeholder') == 'Submit me'
    

def test_xpath(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
    text_string.send_keys('crop')
    text_string.send_keys(Keys.ENTER)

def test_clear(driver):
    input_data = "cat"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.CLASS_NAME, "form-control")
    text_string.send_keys(input_data)
    sleep(2)
    a = text_string.get_attribute('value')
    #text_string.clear()
    #if clear doesn't work what to do
    for _ in range(len(a)):
        text_string.send_keys(Keys.BACKSPACE)
    assert text_string.is_displayed()
    
def test_button_enabled_select(driver):
    driver.get("https://www.qa-practice.com/elements/button/disabled")
    button = driver.find_element(By.ID, "submit-id-submit")
    print(button.is_enabled)
    driver.find_element(By.XPATH, "//*[@id="id_select_state"]")
    print(button.is_enabled)
    
    
    
    
    
    #assert button.is_enabled() == False


