import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('http://charliestore.x10.mx')
linkElem = browser.find_element("link text", "Contáctanos") # sentencia modificada
time.sleep(5)
linkElem.click()
time.sleep(5)
nombre = browser.find_element(By.ID,'yourName')
nombre.send_keys('Carlos Alemán')
time.sleep(3)
correo = browser.find_element(By.ID,'yourEmail')
correo.send_keys('caleman.g2013@gmail.com')
time.sleep(3)
comentarios = browser.find_element(By.ID, 'yourComments')
comentarios.send_keys('Llenado automático de formulario con Python')
time.sleep(3)
checkbox = browser.find_element(By.ID, 'suscribete')
checkbox.click()
time.sleep(5)
#checkbox.submit()
