import tensorflow as tf
import numpy as np
from tensorflow import keras

def obt_precio_casa(num_habitaciones):
    x = np.array([1, 3, 4, 1, 4])
    y = np.array([450000, 750000, 900000, 420000, 885000])

    modelo = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    modelo.compile(optimizer='sgd', loss='mean_squared_error')

    modelo.fit(x, y, epochs=500)

    return modelo.predict([num_habitaciones])

print(obt_precio_casa(2))