import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

def map(value, fmin, fmax, tmin, tmax):
    return (value - fmin) / (fmax - fmin) * (tmax - tmin) + tmin

def create_data(from_data, min_value, max_value):
    x = []
    y = []
    for data in from_data:
        x.append(np.array([map(data, min_value, max_value, 0, 1)]))
        if min_value <= data <= max_value:
            y.append(np.array([1, 0]))
        else:
            y.append(np.array([0, 1]))
    return np.array(x), np.array(y)

def get_ai_1():
    model = keras.Sequential([
        layers.Dense(1, input_shape=(1,), activation='sigmoid'),
        layers.Dense(15, activation='sigmoid'),
        layers.Dense(15, activation='sigmoid'),
        layers.Dense(2, activation='softmax'),
    ])
    model.compile(
        optimizer=tf.optimizers.Adam(),
        loss=tf.keras.losses.CategoricalCrossentropy(),
        metrics=['acc']
    )
    return model

def get_ai_2():
    model = keras.Sequential([
        layers.Dense(1, input_shape=(1,), activation='sigmoid'),
        layers.Dense(15, activation='tanh'),
        layers.Dense(2, activation='softmax'),
    ])
    model.compile(
        optimizer=tf.optimizers.Adam(),
        loss=tf.keras.losses.CategoricalCrossentropy(),
        metrics=['acc']
    )
    return model

def test_ai(model, data, min_ok, max_ok):
    for test in data:
        t = np.array([[map(test, min_ok, max_ok, 0, 1)]])
        pred = model.predict(t)

        p_ok = pred[0][0]
        p_no = pred[0][1]
        ok = p_ok > p_no
        act = min_ok <= test <= max_ok

        print(f'Testing on {test:.2f} ({t[0][0]:5.2f}): {p_ok:.2f} / {p_no:.2f} => {"Right" if ok == act else "Wrong" }')