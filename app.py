# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:16:10 2024

@author: Ola
"""

from flask import Flask

# Create a flask
app = Flask(__name__)

# Create an API end point
@app.route('/')
def say_hello():
    return "Hello World"

if __name__ == '__main__':
    app.run() # domyślnie ustawia localhost i port 5000
