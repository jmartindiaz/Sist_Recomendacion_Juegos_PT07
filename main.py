# el main llamara a las librerias y llamara a los archivos en los que figuran las funciones aplicadas por ejemplo, en ETL

# Importación de librerias y archivos necesarios:
from fastapi import FastAPI
import pandas as pd
import numpy as np

# Lectura de los datos:

df_user_recommend = pd.read_csv(r'Datasets para API\df_user_recommend.csv')

# pd.read_parquet......

# Instanciamos la clase de nuestr API:
app = FastAPI()

# Endpoints de nuestra API:
    ## Inicio de la página
@app.get("/")
def index():
    return "Éste proyecto tiene por finalidad..."

    ## PlayTimeGenre: deberá devolver el año con mas horas jugadas para el género ingresado.
@app.get("/PlayTimeGenre/{genre}")
def PlayTimeGenre(genre: str):
    return "No realizado"

    ## UserForGenre: deberá devolver el usuario que acumula mas horas jugadas para el género ingresado 
    ## y una lista de la acumulación de horas jugadas por año.
@app.get("/UserForGenre/{genre}")
def UserForGenre(genre: str):
    return "No realizado"

    ## UsersRecommend: deberá devolver el top 3 juegos mas recomendados por usuarios para el año ingresado.
@app.get("/UsersRecommend/{anio}")
def UsersRecommend(anio: int):
    cond1 = df_user_recommend['recommend']==True
    cond2 = df_user_recommend['posted_year']==anio
    ep3 = df_user_recommend[cond1 & cond2].groupby('title').count().sort_values('recommend', ascending=False)
    top3 = ep3.head(3).index.tolist()
    return [{'Puesto 1':top3[0]}, {'Puesto 2':top3[1]}, {'Puesto 3':top3[2]}]

    ## UsersNotRecommend: deberá devolver el top 3 juegos MENOS recomendados por usuarios para el año ingresado.
@app.get("/UsersNotRecommend/{anio}")
def UsersNotRecommend(anio: int):
    cond1 = df_user_recommend['recommend']==False
    cond2 = df_user_recommend['posted_year']==anio
    ep4 = df_user_recommend[cond1 & cond2].groupby('title').count().sort_values('recommend', ascending=False)
    top3 = ep4.head(3).index.tolist()
    return [{'Puesto 1':top3[0]}, {'Puesto 2':top3[1]}, {'Puesto 3':top3[2]}]

    ## sentiment_analysis: deberá devolver una lista con la cantidad de registros de reseñas de usuarios que se encuentren
    ## categorizados con un análisis de sentimiento.
@app.get("sentiment_analysis/{anio}")
def sentiment_analysis():
    return "No realizado"