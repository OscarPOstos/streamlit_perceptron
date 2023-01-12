import streamlit as st

import sys

sys.path.insert(0, 'neuron_functions')

from neuron_functions.neuron import Neuron

def weights_section(n_weights, neuron):
    st.subheader("pesos")
    weights = []
    columns = st.columns(n_weights)
    for i in range(n_weights):
        with columns[i]:
            weights.append(st.number_input(f"w{i}", step=0.01))
    st.text(f"w = {weights}")
    neuron.change_weights(weights)
    print(neuron.weights)

def show_components_tab1():
    st.subheader("Una neurona con una entrada y un peso")
    weight = st.slider("Peso", 0.0, 5.0, key="wt1")
    x = st.number_input("Introduzca el valor de la entrada", step=1.0, key="xt")
    submit1 = st.button("Calcular la salida", key="submit1")
    if submit1:
        st.text(neuronal_net(weight, x))


def show_components_tab2():
    col1, col2 = st.columns(2)
    with col1:
        weight = st.slider("Peso w0", 0.0, 5.0, key="wt21")
        x = st.number_input("Entrada x0", step=1.0, key="xt21")
    with col2:
        weight2 = st.slider("Peso w1", 0.0, 5.0, key="wt22")
        x2 = st.number_input("Entrada x1", step=1.0, key="xt22")
    submit2 = st.button("Calcular la salida", key="submit2")
    if submit2:
        st.text(neuronal_net_2(weight, weight2, x, x2))


def show_components_tab3():
    col1, col2, col3 = st.columns(3)
    with col1:
        weight = st.slider("Peso w0", 0.0, 5.0, key="wt31")
        x = st.number_input("Entrada x0", step=1.0, key="xt31")
    with col2:
        weight2 = st.slider("Peso w1", 0.0, 5.0, key="wt32")
        x2 = st.number_input("Entrada x1", step=1.0, key="xt32")
    with col3:
        weight3 = st.slider("Peso w2", 0.0, 5.0, key="wt33")
        x3 = st.number_input("Entrada x2", step=1.0, key="xt33")
    bias = st.number_input("Introduzca un valor de sesgo", step=1.0)
    submit3 = st.button("Calcular la salida", key="submit3")
    if submit3:
        st.text(neuronal_net_3(weight, weight2, weight3, bias, x, x2, x3))
