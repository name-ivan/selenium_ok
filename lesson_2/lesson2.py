from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
sleep(3)

driver.get("https://www.qa-practice.com/elements/input/simple")
text_string = driver.find_element(By.ID, "id_text_string")
text_string.send_keys("cat")
sleep(3)
#text_string.submit()
text_string.send_keys(Keys.ENTER)




sleep(3)