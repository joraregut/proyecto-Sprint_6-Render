# Importar las librerias
import pandas as pd
import plotly.express as px
import streamlit as st

data_vehicles = pd.read_csv('notebooks/vehicles_us.csv')

# Creación de encabezado
st.header(
    'Proyecto del Sprint 6, uso de herramientas para publicar',
    divider="blue")

# Botón para histograma
button_build_hist = st.button('Construcción de histograma')

# Botón para dispersión
button_build_scatter = st.button('Construcción de gráfico de dispersión')

# Logica de funcionamiento para boton de histograma
if button_build_hist:  # Clic en el botón
    # Mensaje
    st.write(
        'Creación de histograma de las fechas de anunciós de venta de autos')

    # creación de histograma
    hist_date = px.histogram(
        data_vehicles,
        x="date_posted",
        nbins=35,
        color='condition')

    # Muestra de gráfico interactivo
    st.plotly_chart(hist_date, use_container_width=True)


# Logica de funcionamiento para boton de dispersión
if button_build_scatter:  # Clic en el botón
    # Mensaje
    st.write(
        'Creación de gráfico de dispersión de los años de vehiculos en venta Vs su precio')

    # creación de dispersión
    scatter_year_price = px.scatter(
        data_vehicles,
        x="model_year",
        y='price',
        color='type')

    # Muestra de gráfico interactivo
    st.plotly_chart(scatter_year_price, use_container_width=True)


# Creación de separador
st.header(
    '',
    divider="blue")

# Creación de encabezado
st.header(
    'Uso de casillas de verificación',
    divider="gray")

# Casilla de verificación para grafica de barras
Checkbox_build_bar = st.checkbox(
    'Construcción de gráfico de barras por tipo y precio de los vehiculos')

# Logica de funcionamiento para la casilla de verificación
if Checkbox_build_bar:  # Selección de casilla
    # Mensaje
    st.write(
        'Creación de gráfica de barras de los tipos y precio de los vehiculos en venta')

    # creación de barras
    bar_type = px.bar(
        data_vehicles,
        x="type",
        y='price')

    # Muestra de gráfico interactivo
    st.plotly_chart(bar_type, use_container_width=True)


# Creación de subencabezado
st.subheader(
    '',
    divider="red")
# Creación de subencabezado
st.subheader(
    'Elaborado por Jorge Arévalo',
    divider="red")
