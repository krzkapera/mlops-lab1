import joblib

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def load_data():
    return load_iris(return_X_y=True)


def train_model(data):
    X, y = data
    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=0
    )

    model = LogisticRegression(random_state=0, max_iter=500)
    model.fit(X_train, y_train)

    return model


def save_model(model):
    joblib.dump(model, "model.joblib")


if __name__ == "__main__":
    data = load_data()
    model = train_model(data)
    save_model(model)
