import requests
from sklearn import datasets

X, y = datasets.load_iris(return_X_y=True)

url = "http://127.0.0.1:5000/predict"

nb_err = 0

for i in range(len(X)):
    data = {
        "X": list(X[i])
    }
    response = requests.post(url, json=data)
    prediction = response.json()["output"]

    if prediction != y[i]:
        nb_err += 1

print("Nb of errors: " + str(nb_err)) 
