import tensorflow as tf
import numpy as np
from tensorflow import keras

x = [0, 2, 4, 6, 8, 10]
# y = x + 2
y = [2, 4, 6, 8, 10, 12]

# Crear modelo, con una neurona, peso de 1

modelo = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Definir funcs de optimizer y loss:

# Stochatic gradiant descent
# Mean Squared Error: Error de la media cuadrada

modelo.compile(optimizer='sgd', loss='mean_squared_error')

# Convetir en Numpy.array()

xs = np.array(x)
ys = np.array(y)

# Entrenar un modelo:

modelo.fit(xs, ys, epochs=500)

# Preguntar al modelo

print(modelo.predict([23]))


