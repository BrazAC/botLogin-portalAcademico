from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#Mantem navegador aberto apos terminar script
options = Options()
options.add_experimental_option("detach", True)

service = Service()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://sistemas.ufmt.br/ufmt.portalsistemas")

driver.implicitly_wait(3)

#Digitar cpf
box_login = driver.find_element(by=By.NAME, value="usuario")
box_login.send_keys("05329024161")

#Digitar senha
box_senha = driver.find_element(by=By.NAME, value="senha")
box_senha.send_keys("050_Bam05")

#Apertar botao de envio
buttons = driver.find_elements(By.CSS_SELECTOR, ".br-button.primary.small.my-3")
buttons[0].click()

