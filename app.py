import streamlit as st
import pandas as pd
import plotly.graph_objects as go

car_data = pd.read_csv('notebooks/vehicles_us.csv')

hist_button = st.button('Contruir Histograma')

if hist_button:
    st.write(
        'Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución de Odómetro')
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir Dispersion')

if disp_button:
    st.write('Creacion de un grafico de disperción')
    fig = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

# Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)
