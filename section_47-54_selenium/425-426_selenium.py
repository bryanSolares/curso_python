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

# navegando a otra página
driver.get("https://www.google.com")

# regresando a la página anterior navegada (la función de back solamente admite 3 segundos de demora)
driver.back()

# como alternativa y para manejar mejores tiempos de espera utilizar una función de javascript
driver.execute_script("window.history.go(-1)")

# indicando un tiempo de espera para que los elementos a buscar sean cargados primero según el tiempo indicado en segundos
driver.implicitly_wait(15)
driver.find_element(By.CSS_SELECTOR, "clase")

print(driver.title)
driver.close()