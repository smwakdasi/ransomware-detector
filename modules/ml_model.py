from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import joblib
import os

def train_model(data_csv, save_model_to="model/rf_model.pkl"):
    df = pd.read_csv(data_csv)
    X = df.drop("label", axis=1)
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("[MODEL] Training complete. Evaluation:")
    print(classification_report(y_test, y_pred))

    joblib.dump(model, save_model_to)
    print(f"[MODEL] Model saved to {save_model_to}")

def load_model(path="model/rf_model.pkl"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found at {path}")
    return joblib.load(path)

def predict(model, feature_df):
    return model.predict(feature_df)[0]
