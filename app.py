import streamlit as st
from components.components import *
from PIL import Image
from neuron_functions.neuron import Neuron
from static.style.style import testcss

neuron = Neuron(weights=[0.0], bias=0, func="sigmoid")

image = Image.open('static/images/logo.jpg')

st.set_page_config(layout="wide")

st.text(testcss())

st.markdown(f"""<style>
            {testcss()}
            </style>""", unsafe_allow_html=True)

st.image(image)

st.title("Simulador de neurona")

n_wx = st.slider('Elige el número de entradas/pesos que tendrá la neurona', 1, 10, 1)

weights_section(n_wx, neuron)

inputs = input_section(n_wx)

col1, col2 = st.columns(2)

with col1:
    bias_section(neuron)

with col2:
    func_section(neuron)

submit = st.button("Calcular la salida")
if submit:
    st.text(neuron.run(inputs))
    
