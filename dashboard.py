import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# set del streamlit localhost
st.set_page_config(page_title="MOOC Dashboard",
                    page_icon=":bar_chart",
                    layout="wide")


# Cargamos los DataFrames
df_coursera = pd.read_csv('data_coursera_revisado.csv')
df_coursera.dropna(inplace=True)

df_udemy = pd.read_csv('data_udemy_revisado.csv')
df_udemy.dropna(inplace=True)

df_edx = pd.read_csv('data_edx_revisado.csv')
df_edx.dropna(inplace=True)

df_kpi = pd.read_csv('data_mooc_kpi.csv')
df_kpi.dropna(inplace=True)


st.title('Proyecto Individual #3 - Data Analysis')
st.subheader('Presentación visual de MOOCS')
st.markdown('***')

#Boton para visualizar los datasets completos
# --------------Coursera---------------
if st.checkbox('Mostrar DataFrame Coursera'):
    st.title('Dataframe Coursera')
    # Mostrar Informacion del dataframe
    st.subheader('Información del Dataframe')
    
    st.write('El Dataframe de Coursera contiene 623 registros con 6 columnas')
    st.dataframe(df_coursera)
    # WORDCLOUD
    st.subheader('WordCloud de las palabras con mas frecuencia en los títulos de Coursera')
    image = Image.open('wc_coursera.png')
    st.image(image,width=500)

    
    #Elegir cierto curso en particular
    st.subheader('Buscador')
    opciones = df_coursera['name']
    buscador_axis_val = st.selectbox('Permite seleccionar cualquiera de los cursos para visualizar sus caracteristicas', opciones)
    resultado = df_coursera.loc[df_coursera['name'] == buscador_axis_val]
    st.write(resultado)

    # BarChart Interactivo
    st.subheader('Bar Chart Interactivo')
    st.text('Esta función permite elegir entre las columnas del dataframe para crear un grafico de barras con su relación.')
    input_col, pie_col = st.columns(2)
    top_n = input_col.text_input('Cuantos registros deseas visualizar?',10)
    top_n = int(top_n)
    df_coursera_chart = df_coursera.head(top_n)
    x_axis_val = st.selectbox('Seleccionar X-Axis', options=df_coursera.columns)
    y_axis_val = st.selectbox('Seleccionar Y-Axis', options=df_coursera.columns)

    plot=px.bar(df_coursera_chart, x=x_axis_val,y=y_axis_val,width=1300)
    st.plotly_chart(plot)
    # PieChart Interactivo
    colc1, colc2,colc3 = st.columns(3,gap='small')
    with colc1:
        st.subheader('Pie Chart Idioma de los cursos.')
        pie_chart = px.pie(
            df_coursera,
        
            values= df_coursera['idioma'].value_counts(),
            names=df_coursera['idioma'].unique(),
            color_discrete_sequence=px.colors.sequential.RdBu
    
        )

        st.plotly_chart(pie_chart)
    with colc2:
        st.subheader('')
    with colc3:
        st.title('')
        st.title('')
        st.subheader('Dentro de este grafico se pueden observar los diferentes idiomas que conforman al dataframe de Coursera; siendo el idioma Ingles el que mayor contenido de cursos conforma al mismo.')
# --------------Udemy---------------
if st.checkbox('Mostrar DataFrame Udemy'):
    st.dataframe(df_udemy)
    st.title('Dataframe Udemy')
    # Mostrar Informacion del dataframe
    st.subheader('Información del Dataframe')
    
    st.write('El Dataframe de Udemy contiene 3672 registros con 6 columnas')
    
    # WORDCLOUD
    st.subheader('WordCloud de las palabras con mas frecuencia en los títulos de Udemy')
    image = Image.open('wc_udemy.png')
    st.image(image,width=500)

    # Cantidad subscriptores en base a eleccion
    st.subheader('Tipo de curso')
    opciones_subj = df_udemy['subject'].unique()
    buscador_subj = st.selectbox('Permite seleccionar cualquiera de los tipos de curso para visualizar la cantidad de subscriptores', opciones_subj)
    resul_subj = df_udemy.loc[df_udemy['subject'] == buscador_subj]
    resul_price = resul_subj['price'].sum() #Cantidad de ganancia por todos lo cursos
    resul_subscr = resul_subj['num_subscribers'].sum()
    resul_total = resul_subscr*resul_price
    st.write(f'La cantidad de subscriptores de los cursos de tipo: {buscador_subj} son de: {resul_subscr}. Considerando el pago del precio de los diferentes tipos de cursos, se estima que se produzcan unos {resul_total} USD de ganancia.')
    

    #Elegir cierto curso en particular
    st.subheader('Buscador')
    opciones = df_udemy['course_title']
    buscador_axis_val = st.selectbox('Permite seleccionar cualquiera de los cursos para visualizar sus caracteristicas', opciones)
    resultado = df_udemy.loc[df_udemy['course_title'] == buscador_axis_val]
    st.write(resultado)

    # BarChart Interactivo
    st.subheader('Bar Chart Interactivo')
    st.text('Esta función permite elegir entre las columnas del dataframe para crear un grafico de barras con su relación.')
    input_col, pie_col = st.columns(2)
    top_n = input_col.text_input('Cuantos registros deseas visualizar?',10)
    top_n = int(top_n)
    df_udemy_chart = df_udemy.head(top_n)
    x_axis_val = st.selectbox('Seleccionar X-Axis', options=df_udemy.columns)
    y_axis_val = st.selectbox('Seleccionar Y-Axis', options=df_udemy.columns)

    plot=px.bar(df_udemy_chart, x=x_axis_val,y=y_axis_val,width=1300)
    st.plotly_chart(plot)

    #Bar Chart Relacion n_subcriptos con subject
    st.subheader('Grafico de barras con la Relación de numero de subcriptores y el subject del curso')
    # Mascara para separar los valores de los subscriptores por subject
    mayor_cantidad_subscribers = df_udemy.loc[df_udemy['subject']=='Web Development']
    mayor_cantidad = mayor_cantidad_subscribers['num_subscribers'].sum()

    plot2 = px.bar(df_udemy, x=df_udemy['subject'],y=df_udemy['num_subscribers'],width=1300)
    st.plotly_chart(plot2)
    st.text(f'Se puede observar como los cursos de Web Development tienen una cantidad de {mayor_cantidad} subscriptores.')

    # PieChart Idioma
    colc1, colc2,colc3 = st.columns(3,gap='small')
    with colc1:
        st.subheader('Pie Chart Idioma de los cursos.')
        pie_chart1 = px.pie(
            df_udemy,
        
            values= df_udemy['idioma'].value_counts(),
            names=df_udemy['idioma'].unique(),
            color_discrete_sequence=px.colors.sequential.RdBu
    
        )

        st.plotly_chart(pie_chart1)
    with colc2:
        st.subheader('')
    with colc3:
        st.title('')
        st.title('')
        st.subheader('Dentro de este grafico se pueden observar los diferentes idiomas que conforman al dataframe de Udemy; siendo el idioma Ingles el que mayor contenido de cursos conforma al mismo.')
    # PIECHART NIVELES
    colu1, colu2,colu3 = st.columns(3,gap='small')
    with colu1:
        st.subheader('Pie Chart Nivel de los cursos.')
        pie_chart2 = px.pie(
            df_udemy,
        
            values= df_udemy['level'].value_counts(),
            names=df_udemy['level'].unique(),
            color_discrete_sequence=px.colors.sequential.RdBu
    
        )

        st.plotly_chart(pie_chart2)
    with colu2:
        st.subheader('')
    with colu3:
        st.title('')
        st.title('')
        st.subheader('Dentro de este grafico se pueden observar los diferentes niveles de intensidad de los cursos que conforman el dataframe de Udemy')
    
# --------------EDX---------------
if st.checkbox('Mostrar DataFrame EDX'):
    st.dataframe(df_edx)
    st.title('Dataframe EDX')

# -----------DASHBOARD---------------

if st.checkbox('Mostrar Dashboard'):
    columna1,columna2,columna3,columna4 = st.columns(4)
    # Primer Renglon
    with columna1:
        st.title('Dashboard MOOCs')
        st.write('Plantilla donde se reflejan los resultados obtenidos del análisis realizados sobre los datasets de COURSERA, EDX y UDEMY')
    with columna2:
        
        # Coursera level pie
        dif_cour = df_coursera['Difficulty']
        
        pie_chart1 = px.pie(
            dif_cour,
            
            values= dif_cour.value_counts(),
            names=dif_cour.unique(),
            color_discrete_sequence=px.colors.sequential.RdBu
            
        )
        pie_chart1.update_layout(width=280,
        height=220,title={
            'text': 'NIVELES DIFICULTAD EN COURSERA',
            'xanchor': 'center',
            'yanchor': 'top'})
        st.plotly_chart(pie_chart1,size_max=20)
    with columna3:
        # Udemy level pie
        dif_ude = df_udemy['level']
        
        pie_chart2 = px.pie(
            dif_ude,
        
            values= dif_ude.value_counts(),
            names=dif_ude.unique(),
            color_discrete_sequence=px.colors.sequential.RdBu
            
        )
        pie_chart2.update_layout(width=280,
        height=220,title={
            'text': 'NIVELES DIFICULTAD EN UDEMY',
            'xanchor': 'center',
            'yanchor': 'top'})
        st.plotly_chart(pie_chart2,size_max=20)
    with columna4:
        # Udemy level pie
        dif_edx = df_edx['Level']
        
        pie_chart3 = px.pie(
            dif_edx,
            
            values= dif_edx.value_counts(),
            names=dif_edx.unique(),
            color_discrete_sequence=px.colors.sequential.RdBu
            
        )
        pie_chart3.update_layout(width=280,
        height=220,
        title={
            'text': 'NIVELES DIFICULTAD EN EDX',
            'xanchor': 'center',
            'yanchor': 'top'})
        st.plotly_chart(pie_chart3,size_max=20)
    
    # SEGUNDO RENGLON

    st.markdown('****')
    columna1,columna2,columna3,columna4 = st.columns([6,6,6,30])

    with columna1:
        st.write('Idiomas Coursera')
        idi_cour = df_coursera['idioma'].value_counts()
        st.write(idi_cour.head(3))
    with columna2:
        st.write('Idiomas Udemy')
        idi_ude = df_udemy['idioma'].value_counts()
        st.write(idi_ude.head(3))
    with columna3:
        st.write('Idiomas EDX')
        idi_edx = df_edx['language'].value_counts()
        st.write(idi_edx.head(3))


    with columna4:
        st.write('sdasd')
        
    
    # with columna1:
    #     st.dataframe(df_kpi[['course_title','idioma','dificultad','Plataforma']],height=400)
    
    # with columna2:
        
    #     st.dataframe(df_kpi[['course_title','idioma','dificultad','Plataforma']],height=400)



    st.markdown('***')
    st.title('KPI')
    st.subheader('')
    st.markdown('***')




    if st.checkbox('Mostrar Coursera'): 
        columna1,columna2= st.columns(2)
        with columna1:
            st.dataframe(df_coursera[['name','course_id','n_reviews','idioma','Rating','Difficulty']],width=700)
        with columna2:
            st.write('Panorama general Coursera')
    if st.checkbox('Mostrar Udemy'): 
        st.dataframe(df_udemy)
    if st.checkbox('Mostrar EDX'): 
        st.dataframe(df_edx)
    

    


