# 1. Importar las librerías request para obtener el documento HTML y 
# BeautifulSoup para extraer información de las etiquetas

import requests
from bs4 import BeautifulSoup

# 2. Declarar la URL que vamos a analizar y el cabecero para simular un navegador
url = "https://www.compramostucoche.es/comprar-coche/"
cabecera = {"User-Agent": "Mozilla/5.0"}
respuesta = requests.get(url, headers=cabecera)

#print(respuesta.text)

# 3. Comprobamos que la conexión fue exitosa
if respuesta.status_code == 200:
    print("Conexión exitosa.")
else:
    print(f"Error en la conexión con código: {respuesta.status_code}")
    
# 4. Utilizaremos BeautifulSoup para extraer los datos de las etiquetas
# Primero parseamos el html
soup = BeautifulSoup(respuesta.text, "html.parser")

# Mostramos los primeros 500 caracteres del documento HTML
#print(soup.prettify()[:500])

# Vamos a intentar obtener el primer título <h1>
titulo = soup.find("h1").text
#print(titulo)

# Obtener todos los enlaces del atributo "href" de las etiquetas <a>
enlaces = [a["href"] for a in soup.find_all("a", href=True)]
#print(enlaces)

# Vamos a intentar obtener los precios de todos los coches
precios = soup.find_all("div", class_="priceValue___3gTAa")

print("\n ** Precios de coches encontrados **")
for precio in precios:
    print(precio.text)


# Vamos a intentar acceder a un contenido a través de su XPATH
#from lxml import etree
#dom = etree.HTML(str(soup))
#recios2 = []

#print(dom.xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[4]/ul/li[1]/div/div[2]/footer/div/div[2]/div[1]")[0].text)

#/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[4]/ul/li[1]/div/div[2]/footer/div/div[2]/div[1]
#/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[4]/ul/li[3]

