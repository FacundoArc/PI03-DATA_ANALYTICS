<p align='center'>
<img src ="https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png">
<p>

<h1 align='center'>
 <b>PROYECTO INDIVIDUAL Nº3</b></br>
    <b>Facundo Gabriel Arce</b>

</h1>
 
## **Introducción** ##
Bienvenidos a mi ultimo proyecto individual de la etapa de labs de la carrera Data Scientist de SoyHenry. Mi nombre es Facundo Gabriel Arce y en este ultimo trabajo realizo las tareas del rol de un ***Data Analyst***

## **Trabajo a realizar** ##
Una start-up de tecnología esta interesada en introducirse en las MOOCs(Massive Open Online Courses), por lo que consiguieron fuentes de información de competidores para evaluar y sacar conclusiones acerca de esta idea.
Se nos asignó la tarea de analizar diferentes datasets y sus niveles de venta según su precio, idioma, nivel y rating de cada curso para analizar que tanto influyen dichas variables en la demanda del producto. También se nos pidió un WordCloud con la palabras mas repetidas dentro de los títulos de los datasets.
Con el fin de monitorear la eficacia de los objetivos de la empresa, se nos pidió **establecer _al menos_ 1 KPI** producto de su análisis y que el mismo se pueda **visualizar** en un dashboard.

## **Trabajo realizado** ##
**EDA** </br>
Como medida principal busqué realizar el Análisis Exploratorio de Datos sobre los archivos provistos por el Project Manager. Ejecute una limpieza de datos irrelevantes para la consigna para asi dejarme con la información más importante para el análisis.
Procedí a guardar los datasets como archivos nuevos para no alterar los que nos habian sido entregados.

**WordCloud** </br>
En un notebook aparte decidí realizar el WordCloud de los títulos de los cursos de cada plataforma por separado. Empecé separando la columna de los nombres de los cursos de los datasets y guardándolos en archivos '.csv'.Luego normalicé la columna de títulos para poder realizar un merge de las tres plataformas y así conseguir la nube de palabras correspondiente al resultado de la unión de los datasets.
Utilicé la librería de WordCloud para separar aquellas palabras que quería visualizar; y Matplotlib para poder crear las imagenes con el respectivo WordCloud. Los resultados, además de poderlos visualizar en el notebook, también fueron descargados como archivos '.png' y guardados en la carpeta WC_TITLES.

**Dashboard** </br>
El dashboard lo confeccioné en el archivo dashboard.py, donde utilicé la librería de Streamlit y de Plotly para crear mi presentación visual conformada con los gráficos y los diferentes análisis de mi trabajo sobre los datasets.
El KPI(Key Performance Indicator) que utilice fue el de Tasa de Conversión de los clientes utlizando el numero de personas inscriptas de cada curso por parte de cada plataforma.



## **Conclusiones** ##
Para concluir llegue a la conclusión de que rol de Data Analyst solicita tener la información adecuada para poder realizar los análisis que se le son pedidos. Pero que no por falta de ello no puedan realizar un trabajo apropiado.
Por parte del trabajo solicitado se conoce la información provista por los datasets de Coursera, Udemy y EDX; considerando que faltó desde un principio aquella información relevante para las cosignas en algunos de los datasets; se llega a la conclusión de que




## **Contenido de Repositorio** ##
Dentro de este repositorio se pueden encontrar los datasets originales de las MOOCs Coursera, EDX y Udemy. También los mismos datasets pero con el EDA hecho para realizar el analisis.
A su vez se encuentra una copia con los titulos de los mismos con los que se realizaron los WordClouds de las palabras mas frecuentadas. </br>
Por otra parte estan los archivos: eda.ipynb donde se realizó el Análisis Exploratorio de Datos y wc_titles.ipynb que fue donde hice los WordClouds con las palabras con mas frecuencia de los titulos de los cursos por separado y tambien uno con toda la unión de las 3 plataformas. En la carpeta WC_TITLES se encuentran los respectivos WordClouds mencionados.
Por último, se encuentra el dashboard.py que como su nombre lo indica, contiene el Dashboard ejecutado con la librería de Streamlit.

## **Tecnologías Utilizadas** ##
Para este trabajo se utilizó el lenguaje de:</br>

    -Python

Y las librerías:</br>

    -Pandas
    -Matplotlib
    -Streamlit
    -WordCloud
    -Langdetect
    -Plotly.express
    -PIL

<p align='center'>

