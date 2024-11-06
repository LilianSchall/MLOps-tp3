import requests
from sklearn import datasets

X, y = datasets.load_iris(return_X_y=True)

predict_url = "http://127.0.0.1:5000/predict"
update_url = "http://127.0.0.1:5000/update-model"
logged_model = 'runs:/33799f81b31b4cfab4ddde6768800a55/iris_model'

update_data = {
    "version": logged_model
}
response = requests.post(update_url, json=update_data)
assert response.status_code == 200

nb_err = 0

for i in range(len(X)):
    data = {
        "X": list(X[i])
    }
    response = requests.post(predict_url, json=data)
    prediction = response.json()["output"]

    if prediction != y[i]:
        nb_err += 1

print("Nb of errors: " + str(nb_err)) 
