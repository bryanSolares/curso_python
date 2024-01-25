import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="")

driver.get("https://www.selenium.dev/documentation/")

# Maximizar ventana
driver.maximize_window()

# Añadir delay
time.sleep(2)

# Extracción más sencilla de un elemento de la página
driver.find_element(By.ID, "username").send_keys("Información")
driver.find_element(By.XPATH, "//*[@id='content']").send_keys("Información")
driver.find_element(By.XPATH, "//*[@id='content'] and //*[@id='content']").send_keys("Información")

# Extrayendo a partir de selector CSS
driver.find_element_by_css_selector("#userName")

print(driver.title)
driver.close()