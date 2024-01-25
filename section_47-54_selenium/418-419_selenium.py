import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="")

driver.get("https://www.selenium.dev/documentation/")

# Maximizar ventana
driver.maximize_window()

# Añadir delay
time.sleep(2)

name = driver.find_element_by_xpath('//*[@id="app"]') # Extrayendo elemento de la página inspeccionada
name = driver.find_element_by_id('identificador') #Extrayendo elemento de la página a partir de su ID
name.send_keys("Bryan")
time.sleep(2)

email = driver.find_element_by_xpath('//*[@id="app"]') # Extrayendo elemento de la página inspeccionada
email.send_keys("bryan@mail.com") # Seteando valor a elemento extraído
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Ejecutando una instrucción de Javascript dentro de la página
time.sleep(2)
driver.find_element_by_spath("//*[@id='app']").click() # Extrayendo elemento de tipo botón de la página y se da click


print(driver.title)
driver.close()