import streamlit as st
from components.components import *
from PIL import Image
from neuron_functions.neuron import Neuron

neuron = Neuron(weights=[0.0], bias=0, func="sigmoid")

image = Image.open('static/images/logo.jpg')

st.image(image)

st.title("Simulador de neurona")

n_wx = st.slider('Elige el número de entradas/pesos que tendrá la neurona', 0, 10, 1)

weights_section(n_wx, neuron)

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    show_components_tab1()

with tab2:
    show_components_tab2()

with tab3:
    show_components_tab3()
    
