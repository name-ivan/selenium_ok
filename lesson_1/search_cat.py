from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
#we can open the chrome window maximized (or controll size elsehow) right away by using options (don't forget to pass them as an argument into driver)
#options.add_argument('start-maximized')
#options.add_argument('--window-size=500,1080')

#if we don't need the browser not to close after testing
#options.add_experimental_option('detach', True)

#it opens the Chrome session, 'driver' is a common name
driver = webdriver.Chrome(options=options)

#only using sleep for demonstrating something, we don't use them in formal testing
sleep(3)
#or we can maximize an opened session if needed
#driver.maximize_window()
#driver.set_window_size(500, 1080)
driver.get('https://www.google.com/')
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("cat")
search_input.send_keys(Keys.ENTER)
page_source = driver.page_source
if "our systems have detected unusual traffic" in page_source or "captcha" in page_source or "i'm not a robot" in page_source:
    print("you caught a capcha")
else:
    page_title = driver.title
    assert 'cat' in page_title, "Error, 'Cat' is not in the page's title"
    print("Page title:", driver.title)

sleep(3)







