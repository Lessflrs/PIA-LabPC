#LESSLIE MONTSERRAT MEDELLIN FLORES 
#1960113

#Importacion de modulos
import requests
from bs4 import BeautifulSoup 
#Obtencion de los datos mediante peticion GET 
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#Analizamos el contenido HTML con BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#Formateamos la salida del objeto results de BeautifulSoup
print(results.prettify())
