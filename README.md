# Proyecto-de-Machine-Learning-Videojuegos
Este repositorio es un proyecto de ciencia de datos que se trata de Videojuegos. Se trabajó con tres archivos comprimidos
El repositorio cuenta con 4 carpetas que se detallan a continuación:

 ![image](https://github.com/andreasoria2022/Proyecto-de-Machine-Learning-Videojuegos/assets/105015078/9e2b9772-fc70-43b1-b4b9-c6635cdb71b3)
Contiene archivos csv que se detallan a continuación:

-	games.csv es un archivo csv que contiene los datos de steam_games.json.gz que se obtuvo luego del proceso de ETL, es decir luego de haber realizado la extracción, transformación y limpieza de los datos.


 ![image](https://github.com/andreasoria2022/Proyecto-de-Machine-Learning-Videojuegos/assets/105015078/f7ca64ad-30c1-4795-98eb-ce3a2da73b8e)
En esta carpeta se encuentra un archivo que se detalla a continuación:

-ETL.ipynb este notebook contiene el proceso de ETL es decir de extracción, transformación y limpieza de los dataset. 


 ![image](https://github.com/andreasoria2022/Proyecto-de-Machine-Learning-Videojuegos/assets/105015078/54b43a74-61c4-4015-a723-f69fac7baebe)
En esta carpeta se encuentra un archivo que se detalla a continuación:

-	EDA.ipynb este notebook contiene el EDA es decir el análisis exploratorio de datos. Se analiza nulos, duplicados, análisis de las variables categóricas más importantes se realiza gráficos de barras con el conteo, análisis estadístico de las variables cuantitativas, se aplicó el método describe, se realizaron histogramas, gráficos de caja, mapa de calor.

 ![image](https://github.com/andreasoria2022/Proyecto-de-Machine-Learning-Videojuegos/assets/105015078/52b875ec-2e22-433c-ac2a-89755e3edbed)
En esta carpeta se encuentra archivos necesarios para cumplir con los objetivos de este proyecto. Voy a proceder a detallar a continuación:

-	playTimeGenre.ipynb este notebook contiene el procedimiento necesario para lograr obtener un dataset que contiene por género, el año con más horas jugadas. El dataset  se transformó en un csv que se guardó en la carpeta FASTAPI VIDEOJUEGOS Y además una función cuyo input es el género y el output es el año con más horas jugadas (primera función) 

-	UserForGenre.ipynb este notebook contiene el procedimiento necesario para lograr obtener un dataset que contiene usuario, cantidad de horas jugadas por año. El dataset se transformó en un csv que se guardó en la carpeta FASTAPI VIDEOJUEGOS. la segunda función cuyo input es el género y cuyo output es el usuario con más horas jugadas e indica por año cuantas horas jugó (segunda función)

-	UserRecommend este notebook contiene el procedimiento necesario para lograr obtener un dataset que contiene el año, los juegos más recomendados por año El dataset se transformó en un csv que se guardó en la carpeta FASTAPI VIDEOJUEGOS. Y además una función cuyo input es el año y el output es el top 3 de juegos más recomendados. Para calcular el juego más recomendado se tomó en cuenta la columna recommend cuya información es un boleano.(tercera función)

-	UserNotRecommend este notebook contiene el procedimiento necesario para lograr obtener un dataset que contiene el año, los juegos menos recomendados por año El dataset se transformó en un csv que se guardó en la carpeta FASTAPI VIDEOJUEGOS. Y además una función cuyo input es el año y el output es el top 3 de juegos menos recomendados. Para calcular el juego menos recomendado se tomó en cuenta la columna recommend cuya información es un boleano. Para esta funcion trabaje solo con esta columna y no con el análisis de sentimientos aplicada a los comentarios ya que la columna recommend me parece a mi criterio más objetiva. (cuarta función)


-	sentiment_analysis.ipynb este notebook contiene el procedimiento necesario para lograr obtener un dataset que contiene el año y el análisis de sentimiento El dataset se transformó en un csv que se guardó en la carpeta FASTAPI VIDEOJUEGOS. Y además una función cuyo input es el año y teniendo en cuenta escala que toma como valor 0 si es malo, 1 si es neutral y 2 si es positivo y el output se categorizó en Negative, Neutral y Positive. (quinta función)

-	sistemarecomendacion.ipynb este notebook contiene el procedimiento necesario para lograr obtener un dataset que contiene el id y cinco recomendaciones de los videojuegos. Además, una función cuyo input es el id y el output son las cinco recomendaciones.(sistema de recomendación)

-	año.csv este archivo csv contiene ítem_id y el año que se utilizó para llevar a cabo la obtención del dataset para realizar la función.




  ![image](https://github.com/andreasoria2022/Proyecto-de-Machine-Learning-Videojuegos/assets/105015078/212923c7-5a10-43ed-a50f-9850d03ba8a9)
Dentro de esta carpeta esta incluidas las carpetas necesarias para hacer funcionar la api y realizar el deploy con render. 

 Se encuentra los archivos csv  usados en las funciones                                       
                                                                   . playTimeGenre.csv archivo usado en la primera función.
				          . UserForGenre.csv archivo usado en la segunda función.
				          .UserRecommend.csv archivo usado en la tercera función.
				          .UserNotRecommend.csv archivo usado en la cuarta función.
				          . sentiment_analysis.csv archivo usado en la quinta función.
 				         . recomendación.csv archivo usado en el sistema de recomendación.
                                                    archivo en el que se detalla las funciones.

                                                    archivo en donde se detallan las librerías utilizadas.
