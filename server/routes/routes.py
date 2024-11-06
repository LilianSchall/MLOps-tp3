from flask import request, abort, redirect
import mlflow
import pandas as pd
import numpy as np
import binascii
import os

mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

def index():
    return "Hello, world!"

def predict():
    data = request.get_json()
    print(data)
    logged_model = 'runs:/33799f81b31b4cfab4ddde6768800a55/iris_model'
    # Load the model back for predictions as a generic Python Function model
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    predictions = loaded_model.predict(np.array([data["X"]]))

    output = {
        "output": int(predictions[0])
    }
    print(output)

    return output
