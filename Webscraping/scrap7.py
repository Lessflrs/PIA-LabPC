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
#Buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")
#Buscar todos los elementos que el h2 contenga en su texto
#la palabra "python"
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
    )
#Monstrarme la cantidad de elementos que complen la busqueda
print(len(python_jobs))

