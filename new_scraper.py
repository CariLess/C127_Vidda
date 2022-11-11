from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# Enlace a NASA Exoplanet
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Controlador web
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    
    ## AGREGA CÓDIGO AQUÍ ##
    try:
        page=

        soup=

        temp_list=[]

        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):


            for td_tag in td_tags:
                try:

                except:

        new_planets_data.append(temp_list)       

    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

planet_df_1 = pd.read_csv("updated_scraped_data.csv")

# Llamar al método
for index, row in planet_df_1.iterrows():

     ## ADGREGA CÓDIGO AQUÍ ##
    print(row['hyperlink'])
     # Llama a scrape_more_data(<hyperlink>)

    print(f"La extracción de datos del hipervínculo {index+1} se ha completado")

print(new_planets_data)

# Remover el carácter '\n' de los datos extraídos
scrapped_data = []

for row in new_planets_data:
    replaced = []
    ## AGREGAR EL CÓDIGO AQUÍ ##
    for el in row: 

    
    scrapped_data.append(replaced)

print(scrapped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scrapped_data,columns = headers)

# Convertir a CSV
new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")