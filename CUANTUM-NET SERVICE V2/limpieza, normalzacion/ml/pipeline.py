import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from data.preprocess import drop_na_columns, fill_missing, normalize_features, ensure_band_columns
from .models import train_model, load_model

def run_training_pipeline(df: pd.DataFrame, target_col: str = "state", test_size=0.2, save_path=None):
    # limpieza básica
    df2 = drop_na_columns(df)
    df2 = fill_missing(df2, strategy="median")
    df2 = ensure_band_columns(df2)

    # suponemos que las columnas de banda están en Delta,Theta,...
    feature_cols = ["Delta","Theta","Alpha","Beta","Gamma"]
    X = df2[feature_cols]
    y = df2[target_col] if target_col in df2.columns else df2.iloc[:, -1]

    # split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

    model = train_model(X_train, y_train, save_path or "artifacts/models/eeg_model_v1.joblib")
    preds = model.predict(X_test)
    report = classification_report(y_test, preds, output_dict=True)
    return model, report