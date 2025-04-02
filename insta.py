from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Caminho do driver
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(5)  # Espera a página carregar

# # Login
username = driver.find_element(By.NAME, "username")  #Procura o elemento na pagina e guarda a posição
password = driver.find_element(By.NAME, "password")
username.send_keys("seu_usuario")
password.send_keys("sua_senha.")
password.send_keys(Keys.RETURN)

time.sleep(5)

# # Acessar aba Salvos
driver.get("https://www.instagram.com/enriquesusin/saved/rpg/17948031698580212/")

time.sleep(5)

# Scroll até o final da página para carregar todas as imagens
last_height = driver.execute_script("return document.body.scrollHeight")  #descobre a altura da pagina com JS



        # Capturar URLs das imagens
images = driver.find_elements(By.TAG_NAME, "img")  #Procura tudo que tem tag IMG e coloca numa lista
image_urls = [img.get_attribute("src") for img in images] #Pega a URL de cada elemento da lista
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(7)  # Tempo para carregar novas imagens
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Capturar URLs das imagens
    images = driver.find_elements(By.TAG_NAME, "img")  #Procura tudo que tem tag IMG e coloca numa lista
    for img in images:
        image_urls.append(img.get_attribute("src")) #Pega a URL de cada elemento da lista

    if new_height == last_height:  # Se não carregar mais nada, parar
        break
    last_height = new_height
    # Salvar URLs em um arquivo txt
    
       
image_urls = list(set(image_urls))

with open("urls.txt", "w") as file:
    for url in image_urls:
                file.write(url + "\n")
    print("As URLs foram salvas em 'urls.txt'.")

# Fechar o navegador
driver.quit()