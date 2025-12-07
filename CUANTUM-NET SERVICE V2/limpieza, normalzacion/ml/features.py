def flatten_features(feature_row):
    """Flatten a pandas Series into a numeric vector."""
    return [v for _, v in feature_row.items() if isinstance(v, (int, float))]