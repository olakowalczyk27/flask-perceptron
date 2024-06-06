# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:16:10 2024

@author: Ola
"""

# app.py
from flask import Flask, request, jsonify
from perceptron import Perceptron
import numpy as np

app = Flask(__name__)

# Model perceptronowy
model = Perceptron(input_size=2)
# Przykładowe dane do treningu (AND logic gate)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
d = np.array([0, 0, 0, 1])

# Trening modelu
model.fit(X, d)

@app.route('/')
def home():
    return "Model perceptronowy jest gotowy do użycia!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict(np.array(data['input']))
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
