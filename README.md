# Simulador Neurona
Este proyecto consiste en imitar el comportamiento de un perceptron donde podemos incluir una cantidad variable de entradas y pesos, un sesgo y una función de activación

## Acceso a la aplicacion

Se podrá acceder a la aplicación pinchando en el siguiente link

[Simulador de neurona](https://oscarpostos-streamlit-perceptron-app-6opg29.streamlit.app "Simulador de neurona")

## Funcionamiento de la neurona

[![Ejemplo de la app](https://i.postimg.cc/HxHMFMPm/imagen-2023-01-23-090248406.png "Ejemplo de la app")](https://i.postimg.cc/HxHMFMPm/imagen-2023-01-23-090248406.png "Ejemplo de la app")

### Rango

Lo primero que podemos ver en la aplicación es un rango de numeros que dependiendo de su valor podeis ver que la app mostrará esa cantidad de pesos y entradas a modificar lo que nos ayudará en casos de que tengamos que resolver un problema de por ejemplo 2 entradas como un Y logico o un problema con 1 entrada como un NOT logico

### Pesos

Tendremos una cantidad de inputs que representan el peso de la neurona donde un $w_i$ lo multiplicaremos con el $x_i$

### Entradas

Aqui es donde escribiremos nuestros valores para nuestros casos de prueba y comprobar que sale en la salida

### Sesgo

Tambien llamado bias, es un valor que se añade al resultado de la suma de productos $w*x$ 
Un ejemplo de uso de este input es por ejemplo en un calculo de distancias donde un coche ya ha recorrido 60 km por lo que en la neurona podemos añadir al sesgo esos 60 km para que la neurona tenga en cuenta esa distancia recorrida

### Funcion de activación

Aqui podemos elegir entre estas opciones:

* ReLu
* Sigmoide
* TanH

#### ReLu

[![Relu formula](https://i.ytimg.com/vi/68BZ5f7P94E/maxresdefault.jpg "Relu formula")](https://i.ytimg.com/vi/68BZ5f7P94E/maxresdefault.jpg "Relu formula")

#### Sigmoide

[![Formula sigmoide](https://miro.medium.com/max/1033/0*D5do3xhv5ulF50w2.png "Formula sigmoide")](https://miro.medium.com/max/1033/0*D5do3xhv5ulF50w2.png "Formula sigmoide")

#### TanH

En este caso ya no es una formula, sino una función que directamente python te lo da con la libreria math que es la de la tangente hiperbolica cuya grafica sería esta:

[![Grafica tanh](https://www.medcalc.org/manual/functions/tanh.png "Grafica tanh")](https://www.medcalc.org/manual/functions/tanh.png "Grafica tanh")

### Boton Submit

Internamente realiza este calculo

$y = \sum(w_i*x_i) + bias$

## Ejemplo de uso real

Vamos a intentar hacer un Y logico por lo que tendremos la siguiente configuracion

[![Configurancion](https://i.postimg.cc/dQCfvc1V/imagen-2023-01-23-093221596.png "Configurancion")](https://i.postimg.cc/dQCfvc1V/imagen-2023-01-23-093221596.png "Configurancion")

Aqui dejaremos una tabla de la verdad para que veais lo que se tiene que imprimir en cada entrada

[![Tabla AND](https://www.allaboutcircuits.com/uploads/articles/two-input-and-gate-truth-table.jpg "Tabla AND")](https://www.allaboutcircuits.com/uploads/articles/two-input-and-gate-truth-table.jpg "Tabla AND")

Ahora vamos a probar las distintas entradas

[![](https://i.postimg.cc/XqKx53GK/imagen-2023-01-23-093335180.png)](https://i.postimg.cc/XqKx53GK/imagen-2023-01-23-093335180.png)

[![](https://i.postimg.cc/28z7tsLJ/imagen-2023-01-23-093430078.png)](https://i.postimg.cc/28z7tsLJ/imagen-2023-01-23-093430078.png)

[![](https://i.postimg.cc/wMK2G3YY/imagen-2023-01-23-093511276.png)](https://i.postimg.cc/wMK2G3YY/imagen-2023-01-23-093511276.png)

[![](https://i.postimg.cc/28z7tsLJ/imagen-2023-01-23-093430078.png)](https://i.postimg.cc/28z7tsLJ/imagen-2023-01-23-093430078.png)

[![](https://i.postimg.cc/wTwf6qhL/imagen-2023-01-23-093727788.png)](https://i.postimg.cc/wTwf6qhL/imagen-2023-01-23-093727788.png)

[![](https://i.postimg.cc/28z7tsLJ/imagen-2023-01-23-093430078.png)](https://i.postimg.cc/28z7tsLJ/imagen-2023-01-23-093430078.png)

[![](https://i.postimg.cc/XJWcfmfn/imagen-2023-01-23-093823852.png)](https://i.postimg.cc/XJWcfmfn/imagen-2023-01-23-093823852.png)

[![](https://i.postimg.cc/2jchyVKk/imagen-2023-01-23-093937007.png)](https://i.postimg.cc/2jchyVKk/imagen-2023-01-23-093937007.png)

Vemos que imprime bastante bien la tabla de la verdad con lo que podremos decir que esta simulación ha sido un exito

## Conclusión

Este simulador sirve para interactuar de manera grafica con una neurona y para fines educativos como por ejemplo como funciona un perceptrón, que pasa si meto estos pesos y entradas, para que sirve, etc.

Ahora que hicimos el caso de uso real, se puede ver que es un exito este simulador
