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
df_forgenre = pd.read_csv('data fastapi/UserForGenre.csv')
df_UserRecommend =pd.read_csv('data fastapi/UsersRecommend.csv')


#Endpoint 1: El usuario con mas horas jugadas para el genero y una lista de la acumulación de horas jugadas por año

@app.get("/Genero1/{genres}")
def PlayTimeGenre(genres:str):
    genero = df_play[df_play['genres'] == genres]
    
    año = genero['año'].tolist()[0]

    return {'Año de lanzamiento con más horas jugadas para género': genres, 'año': año}

#Endpoint 2: El usuario que acumula mas horas jugadas para el genero dado y una lista de la acumulación de horas jugadas por año

@app.get("/Genero2")
def UserForGenre(genres: str):
    # Filtrar los usuarios del año deseado
    genero = df_forgenre[df_forgenre['genres'] == genres]
    
    if len(genero) == 0:
        return 'El género no existe'

    horas_por_año = genero.apply(lambda x: {'Año': x['año'], 'Horas jugadas:': x['horas']}, axis=1).tolist()

    user_id = genero['user_id'].values[0]

    return {'El usuario con más horas jugadas para el género': genres, 'es' :user_id, 'Horas jugadas': horas_por_año}


#Endpoint 3: El top 3 de juegos mas recomendados por usuarios para el año dado

@app.get("/año3")
def UsersRecommend(año: int):
    # Filtrar los juegos del año deseado
    juegos_año = df_UserRecommend[df_UserRecommend['año'] == año]
    
    # Seleccionar los tres juegos con la calificación más alta
    top_3_juegos = list(juegos_año.nlargest(3, 'calificación')['juego'])
    
    # Crear una lista de diccionarios con el formato deseado
    resultado = [{'Puesto {}:'.format(i+1): juego} for i,juego in enumerate(top_3_juegos)]
    
    return resultado
