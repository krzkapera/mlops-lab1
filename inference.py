import joblib


def load_model():
    return joblib.load("model.joblib")


def predict(model, sample):
    input_data = [
        [
            sample["sepal_length"],
            sample["sepal_width"],
            sample["petal_length"],
            sample["petal_width"],
        ]
    ]

    prediction = model.predict(input_data)[0]

    names = {0: "setosa", 1: "versicolor", 2: "virginica"}
    return names[prediction]
