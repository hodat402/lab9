from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "G:\seledriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://the-internet.herokuapp.com/")

driver.find_element_by_link_text("Form Authentication").click()

username = driver.find_element_by_name("username")
username.send_keys("tomsmith")

passs = driver.find_element_by_name("password")
passs.send_keys("SuperSecretPassword!")

passs.send_keys(Keys.ENTER)

print(driver.title)

time.sleep(5)

driver.close()
