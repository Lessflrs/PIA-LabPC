# LESSLIE MEDELLIN FLORES 
#1960113

# Importar modulos
import requests
import csv
from bs4 import BeautifulSoup
#Direccion de la pagina web
url = "http://quotes.toscrape.com/"
#Ejecutar GET-Requests
response = requests.get(url)
#Analizar sintacticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
#Extraer todas las citas y autores del archivo HTML
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")
#Crear una lista de las citas 
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)
#Crear una lista de los autores
authors = list()
for author in authors_html:
    authors.append(author.text)
#Para hacer el test: cambiar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
    print(t)
#Guardar las citas y autores en u archivo CSV en el direcctorio actual
#Abrir el archivo con excel / LibreOffice, etc.
with open('./citas_1960113.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))

import datetime
hora_actual = datetime.datetime.now()
print(hora_actual)

