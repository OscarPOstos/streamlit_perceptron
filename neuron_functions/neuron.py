import numpy as np
import math

from activation_funcs import sigmoid, relu


class Neuron:
    activation = {"sigmoid": lambda x: sigmoid(x),
                  "relu": lambda x: relu(x),
                  "tanh": lambda x: math.tanh(x)}

    RELU = "relu"
    TANH = "tanh"
    SIGMOID = "sigmoid"

    def __init__(self, weights, bias, func):
        self.__check_attributes(weights, func)
        self.weights = weights
        self.bias = bias
        self.func = func

    def __check_attributes(self, weights, func):
        self.__check_weights(weights)
        self.__check_func(func)

    @staticmethod
    def __check_weights(weights):
        if len(weights) <= 0:
            raise Exception("El peso no puede estar vacio")

    @staticmethod
    def __check_func(func):
        if func not in Neuron.activation:
            raise Exception("Esa funcion de activacion no existe. Los que hay son ('relu', 'tanh', 'sigmoid')")

    def __neuronal_network(self, x):
        return 0

    def change_bias(self, bias):
        self.bias = bias

    def change_weights(self, weights):
        self.__check_weights(weights)
        self.weights = weights

    def change_func(self, func):
        self.__check_func(func)
        self.func = func

    def run(self, input_data):
        if np.size(input_data) == np.size(self.weights):
            result = self.__neuronal_network(input_data)
            return Neuron.activation[self.func](result)
        else:
            raise Exception("La longitud de w y x no son iguales")
