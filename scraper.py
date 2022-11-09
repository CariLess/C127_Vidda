from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

# Controlador web
browser = webdriver.Chrome("/Users/cariless/Downloads/C127_Vidda/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data=[]

# Definir el método de extracción de datos para Exoplanet
def scrape():
    for i in range(0,10):
        print(f'Extrayendo página {i+1}...')
        # Objeto BeautifulSoup
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Bucle para encontrar los elementos usando XPATH
        for ul_tag in soup.find_all("ul", attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")

            temp_list= []

            for index, li_tag in enumerate(li_tags):
                if index ==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except: 
                        temp_list.append("")

            planets_data.append(temp_list)
            # Encontrar todos los elementos en la página y hacer clic para desplazarse a la siguiente


    print(planets_data[1])

# Llamada del método
scrape()

# Definir los encabezados


# Convertir a CSV