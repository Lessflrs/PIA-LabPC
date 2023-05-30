#LESSLIE MONTSERRAT MEDELLIN FLORES 
#1950113

#Importar modulos
import requests
#Obtener la informacion HTMl de la URL
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#Imprimir el texto de la peticion GET
print(page.text)
