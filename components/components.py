import streamlit as st

import sys

sys.path.insert(0, 'neuron_functions')

from neuron_functions.neuron import Neuron


def weights_section(n_weights, neuron):
    st.subheader("Pesos")
    weights = []
    columns = st.columns(n_weights)
    for i in range(n_weights):
        with columns[i]:
            weights.append(round(st.number_input(f"w{i}", step=0.01), 2))
    st.text(f"w = {weights}")
    neuron.change_weights(weights)


def input_section(n_inputs, neuron):
    st.subheader("Entradas")
    inputs = []
    columns = st.columns(n_inputs)
    for i in range(n_inputs):
        with columns[i]:
            inputs.append(round(st.number_input(f"x{i}", step=0.01), 2))
    st.text(f"x = {inputs}")
    return inputs


def bias_section(neuron):
    st.subheader("Sesgo")
    bias = round(st.number_input("Introduce el valor de sesgo", step=0.01), 2)
    neuron.change_bias(bias)


def func_section(neuron):
    functions = {"Sigmoide": Neuron.SIGMOID,
                 "ReLU": Neuron.RELU,
                 "Tangente hiperbólica": Neuron.TANH}
    st.subheader("Función de activación")
    func = st.selectbox("Elige la función de activación",
                        ("Sigmoide", "ReLU", "Tangente hiperbólica"))
    neuron.change_bias(functions[func])

