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
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver


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
    print(button.is_enabled())
    select = driver.find_element(By.XPATH, '//*[@id="id_select_state"]')
    dropdown = Select(select)
    dropdown.select_by_value("enabled")
    print(button.is_enabled())
    
    
def test_visible_after(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    button3 = driver.find_element(By.CSS_SELECTOR, 'visibleAfter')
    button3.click()
    # assert button3.is_displayed(), "the button is not displayed"
 


def test_cart_added_sign(driver):
    driver.get("https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html")
    sizeS = driver.find_element(By.ID, 'option-label-size-143-item-167')
    sizeS.click()
    color_black = driver.find_element(By.ID, 'option-label-color-93-item-49')
    color_black.click()
    add_to_cart_btn = driver.find_element(By.ID, "product-addtocart-button")
    add_to_cart_btn.click()
    wait = WebDriverWait(driver, 5)
    wait.until_not(
        EC.text_to_be_present_in_element_attribute(
            locator=(By.CSS_SELECTOR, ".counter.qty"),
            attribute_='class',
            text_='empty')
        )
    wait.until_not(
        EC.text_to_be_present_in_element_attribute(
            locator=(By.CSS_SELECTOR, ".counter.qty"),
            attribute_='class',
            text_='loading')
        )
    counter = driver.find_element(By.CSS_SELECTOR, '.counter-number')
    print(f"counter number is {counter.text}")
    # cart_sign = driver.find_element()
    
    
def test_visible_after1(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    wait = WebDriverWait(driver, 8)
    wait.until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    button3 = driver.find_element(By.ID, 'visibleAfter')
    button3.click()
    driver.add_cookie({'name':'test_name', 'value': 'test_value'})
    # print(driver.get_cookies())
    print(driver.get_cookie('test_name'))
    
    
def test_same_elements(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    product_link = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    print(product_link[0].text)
    print(product_link[-1].text)
    
def test_same_cards(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    product_cards = driver.find_elements(By.CLASS_NAME, 'product-item-info')
    for card in product_cards:
        print(card.find_element(By.CLASS_NAME, 'price').text)
    # print(product_cards[0].find_element(By.CLASS_NAME, 'price').text)
    
    
    
    
    
     #Different waits
 #implicitly wait
 # chrome_driver.implicitly_wait(5)

# wait = WebDriverWait(driver, 5)
# wait.until_not(
#     EC.text_to_be_present_in_element_attribute(
#         locator=(By.CSS_SELECTOR, ".counter.qty"),
#         attribute_='class',
#         text_='empty')
#     )

