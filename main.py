# el main llamara a las librerias y llamara a los archivos en los que figuran las funciones aplicadas por ejemplo, en ETL

# Importación de librerias y archivos necesarios:
from fastapi import FastApi
import pandas as pd
import numpy as np

# Lectura de los datos:
# pd.read_parquet......

# Instanciamos la clase de nuestr API:
app = FastApi()

# Endpoints de nuestra API:
    ## Inicio de la página
@app.get("/")
def index():
    return "Éste proyecto tiene por finalidad..."

    ## PlayTimeGenre: deberá devolver el año con mas horas jugadas para el género ingresado.
@app.get("/PlayTimeGenre/{genre}")
def PlayTimeGenre(genre: str):
    return

    ## UserForGenre: deberá devolver el usuario que acumula mas horas jugadas para el género ingresado 
    ## y una lista de la acumulación de horas jugadas por año.
@app.get("/UserForGenre/{genre}")
def UserForGenre(genre: str):
    return

    ## UsersRecommend: deberá devolver el top 3 juegos mas recomendados por usuarios para el año ingresado.
@app.get("/UsersRecommend/{anio}")
def UsersRecommend(anio: int):
    return 

    ## UsersNotRecommend: deberá devolver el top 3 juegos MENOS recomendados por usuarios para el año ingresado.
@app.get("/UsersNotRecommend/{anio}")
def UsersNotRecommend(anio: int):
    return

    ## sentiment_analysis: deberá devolver una lista con la cantidad de registros de reseñas de usuarios que se encuentren
    ## categorizados con un análisis de sentimiento.
@app.get("sentiment_analysis/{anio}")
def sentiment_analysis()