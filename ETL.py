# Importamos las librerías necesarias:
import pandas as pd
import gzip
import numpy as np


# Definimos las rutas de los archivos:
ruta_games='Datasets/steam_games.json.gz'
ruta_reviews='Datasets/user_reviews.json.gz'
ruta_items='Datasets/users_items.json.gz'

# Extracción de los datos:
