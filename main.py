from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder

app = FastAPI()

#http://127.0.0.1:8000

@app.get ("/")
def index():
    return {"message":"Hola Mundo"}

#Datos a usar

df_play =pd.read_csv('data fastapi/playTimeGenre.csv')


#Endpoint 1: El usuario con mas horas jugadas para el genero y una lista de la acumulación de horas jugadas por año

@app.get("/Genero1/{genres}")
def PlayTimeGenre(genres:str):
    genero = df_play[df_play['genres'] == genres]
    
    año = genero['año'].tolist()[0]

    return {'Año de lanzamiento con más horas jugadas para género': genres, 'año': año}