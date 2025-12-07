import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

DEFAULT_MODEL_PATH = "artifacts/models/eeg_model_v1.joblib"

def make_rf_pipeline(n_estimators=50, max_depth=6, random_state=42):
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state))
    ])
    return pipe

def train_model(X, y, save_path=DEFAULT_MODEL_PATH):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    model = make_rf_pipeline()
    model.fit(X, y)
    joblib.dump(model, save_path)
    return model

def load_model(path=DEFAULT_MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found at {path}")
    return joblib.load(path)

def predict(model, X):
    return model.predict(X)