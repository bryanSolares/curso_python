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

name = driver.find_element(By.CSS_SELECTOR, "selector").send_keys("Valor a enviar")
# Añadiendo comportamiento especial y con teclas especiales
name.send_keys(Keys.ENTER)
name.send_keys(Keys.TAB)

name.send_keys(Keys.TAB + "Texto")

print(driver.title)
driver.close()