def flatten_features(feature_row):
    numeric = [v for v in feature_row.values if isinstance(v, (int, float))]
    return numeric