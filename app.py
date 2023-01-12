import streamlit as st
from components.components import *
from PIL import Image
from neuron_functions.neuron import Neuron

neuron = Neuron(weights=[0.0], bias=0, func="sigmoid")

image = Image.open('static/images/logo.jpg')

st.set_page_config(layout="wide")

st.image(image)

st.title("Simulador de neurona")

n_wx = st.slider('Elige el número de entradas/pesos que tendrá la neurona', 1, 10, 1)

weights_section(n_wx, neuron)

inputs = input_section(n_wx)

submit = st.button("Calcular la salida")
if submit:
    st.text(neuron.run(inputs))
    
