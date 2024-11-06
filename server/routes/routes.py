from flask import request, abort, redirect
import mlflow
import pandas as pd
import binascii
import os

def index():
    return "Hello, world!"

def predict():
    data = request.get_json()
    logged_model = 'runs:/33799f81b31b4cfab4ddde6768800a55/iris_model'
    # Load the model back for predictions as a generic Python Function model
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    predictions = loaded_model.predict(data["X"])

    return predictions
