# 1. Importamos las librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

# 2. Configuramos selenium con Chrome en modo headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--dissable-gpu")

# 3. Iniciar el navegador con Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 4. Declaramos la URL de la web
url = "https://finofilipino.org"

# 5. Pasamos la URL al driver
driver.get(url)

# Metemos una pausa de 5 segundos
print("Esperando 5 segundos...")
time.sleep(5)

# 6. Vamos a hacer Scroll para que se vaya descargando más posts
for i in range(3):
    print(f"Estamos haciendo scroll hacia abajo... {i+1}/3")
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(5)

# 7. Extraer las listas <ul class="entry-tags">
print("Extrayendo los contenidos de las etiquetas")

tags = driver.find_elements(By.CLASS_NAME, "entry-tags")

for i, ul in enumerate(tags, start = 1):
    print(f" Post{i}: {ul.text}")

# 8. Cerrar el navegador
driver.quit()