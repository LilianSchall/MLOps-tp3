from flask import request, abort, redirect
import mlflow
import pandas as pd
import numpy as np
import binascii
import os

mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")
logged_model = 'runs:/33799f81b31b4cfab4ddde6768800a55/iris_model'
current_model = ""
next_model = ""

def index():
    return "Hello, world!"

def update_model():
    global current_model
    global next_model
    data = request.get_json()

    if not "version" in data.keys():
        return abort(400)

    version = data["version"]
    if len(current_model) == 0:
        current_model = version
        next_model = version
    else:
        current_model = next_model
        next_model = version

    return f"Changed next model version to: {version}"

def accept_model():
    global current_model
    global next_model

    if len(current_model) == 0:
        return abort()
    else:
        current_model = next_model
    return f"Changed next model version to: {next_model}"

def predict():
    global current_model
    global next_model
    p = 0.8
    
    if len(current_model) == 0:
        return abort(400)

    selected_model = current_model if np.random.uniform(0, 1) < p else next_model

    data = request.get_json()
    print(data)
    # Load the model back for predictions as a generic Python Function model
    loaded_model = mlflow.pyfunc.load_model(selected_model)
    predictions = loaded_model.predict(np.array([data["X"]]))

    output = {
        "version": selected_model,
        "output": int(predictions[0])
    }
    print(output)

    return output
