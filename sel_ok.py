from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
#we can open the chrome window maximized (or controll size elsehow) right away by using options (don't forget to pass them as an argument into driver)
#options.add_argument('start-maximized')
#options.add_argument('--window-size=500,1080')

#if we don't need the browser not to close after testing
#options.add_experimental_option('detach', True)

#it opens the Chrome session, 'driver' is a common name
driver = webdriver.Chrome(options=options)

#only using sleep for demonstrating something, we don't use them in formal testing
time.sleep(3)
#or we can maximize an opened session if needed
#driver.maximize_window()
#driver.set_window_size(500, 1080)
driver.get('https://www.google.com/')
time.sleep(3)
print(driver.title)






