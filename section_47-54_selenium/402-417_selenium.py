from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="")

driver.get("https://www.selenium.dev/documentation/")
print("Hello World")
print(driver.title)
driver.close()