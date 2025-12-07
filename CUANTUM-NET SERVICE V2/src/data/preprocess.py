import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def drop_na_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Quitar columnas con sólo NA o con demasiados NA."""
    thresh = int(0.5 * len(df))
    return df.dropna(axis=1, thresh=thresh)

def fill_missing(df: pd.DataFrame, strategy: str = "median") -> pd.DataFrame:
    """Rellenar valores faltantes por median/mean/zero."""
    res = df.copy()
    num_cols = res.select_dtypes(include=[np.number]).columns
    for c in num_cols:
        if strategy == "median":
            res[c].fillna(res[c].median(), inplace=True)
        elif strategy == "mean":
            res[c].fillna(res[c].mean(), inplace=True)
        else:
            res[c].fillna(0.0, inplace=True)
    return res

def normalize_features(df: pd.DataFrame, columns=None):
    """Escalar columnas numéricas con StandardScaler. Devuelve (df_scaled, scaler)."""
    scaler = StandardScaler()
    res = df.copy()
    if columns is None:
        columns = res.select_dtypes(include=[np.number]).columns.tolist()
    if len(columns) == 0:
        return res, None
    res_loc = res[columns].to_numpy(dtype=float)
    scaled = scaler.fit_transform(res_loc)
    res[columns] = scaled
    return res, scaler

def ensure_band_columns(df: pd.DataFrame, bands=("Delta","Theta","Alpha","Beta","Gamma")):
    """Asegura que estén presentes columnas de bandas (pone 0 si falta)."""
    res = df.copy()
    for b in bands:
        if b not in res.columns:
            res[b] = 0.0
    return res