# Librerias a utilizar:
import pandas as pd
import numpy as np
import json
import ast
import gzip

# Rutas de los datos:
ruta_games='Datasets/steam_games.json.gz'
ruta_reviews='Datasets/user_reviews.json.gz'
ruta_items='Datasets/users_items.json.gz'

## Games:
games = []
with gzip.open(ruta_games, 'rt', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        games.append(linea) 

# Quitamos el '\n' al final de cada linea:
for i in range(0,len(games)):
    games[i]= games[i].replace("\n","")
# Transformo cada una de las cadenas a diccionario de Python:
for i in range(0,len(games)):
    games[i]= json.loads(games[i])
    
# Transformamos a DataFrame:
df_games = pd.DataFrame(games)

## Reviews:
reviews = []
with gzip.open(ruta_reviews, 'rt', encoding="utf-8") as archivo:
    lineas = archivo.readlines()
for linea in lineas:
    reviews.append(ast.literal_eval(linea))
    
# Transformamos a DataFrame:
df_reviews = pd.DataFrame(reviews)

## Items:
items = []
with gzip.open(ruta_items, 'rt', encoding="utf-8") as archivo:
    lineas = archivo.readlines()
for linea in lineas:
    items.append(ast.literal_eval(linea))
    
# Transformamos a DataFrame:
df_items = pd.DataFrame(items)