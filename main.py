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
df_UserNotRecommend= pd.read_csv('data fastapi/UsersNotRecommend.csv')
df_sentiment= pd.read_csv('data fastapi/sentiment_analysis.csv')
df_recommend = pd.read_csv('data fastapi/sistemarecomendacion.csv')


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

#Endpoint 4:El top 3 de juegos menos recomendados por usuarios para el año dado

@app.get("/año4")
def UsersNotRecommend(año:int):
    # Filtro los juegos del año deseado
    juegos_año = df_UserNotRecommend[df_UserNotRecommend['año'] == año]
    
    # Selecciono los tres juegos con la mayor calificación negativa 
    top_3_juegos = list(juegos_año.nlargest(3, 'calificación')['juego'])
    
    # Creo una lista de diccionarios con el formato deseado
    resultado = [{'Puesto {}:'.format(i+1): juego} for i,juego in enumerate(top_3_juegos)]
    
    return resultado

#Endpoint 5: Segun el año de lanzamiento devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentran categorizados

@app.get("/año5")
def sentiment_analysis(año:int):
    # Filtro los datos por año y categoría
    df_filtrado1 = df_sentiment[(df_sentiment['año'] == año) & (df_sentiment['user_review'] == 'Negative')]
    df_filtrado2= df_sentiment[(df_sentiment['año'] == año) & (df_sentiment['user_review'] == 'Neutral')]
    df_filtrado3 = df_sentiment[(df_sentiment['año'] == año) & (df_sentiment['user_review'] == 'Positive')]
    
    # Creo el diccionario a partir del resultado
    resultado = {
        'Negative': df_filtrado1['calificacion'].tolist()[0],
        'Neutral': df_filtrado2['calificacion'].tolist()[0],
        'Positive': df_filtrado3['calificacion'].tolist()[0]
    }
    
    return resultado

#Sistema de Recomendacion

# Aplicar One-Hot Encoding a las características
enc = OneHotEncoder(handle_unknown='ignore')
X = enc.fit_transform(df_recommend[['genres', 'app_name', 'tags']])

# Calcular la similitud del coseno entre los vectores resultantes
cosine_sim = cosine_similarity(X)

@app.get("/id")
def get_recommendations(id:float):
    # Obtener el índice del juego que coincide con el ID
    idx = df_recommend[df_recommend['id'] == id].index[0]

    # Obtener las puntuaciones de similitud del juego con todos los demás juegos
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ordenar los juegos según las puntuaciones de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
