import pandas as pd
import numpy as np
from collections import defaultdict

BANDS = ["Delta", "Theta", "Alpha", "Beta", "Gamma"]

REQUIRED = {
    "timestamp", "subject_id", "brain_region",
    "signal_amplitude", "frequency_band", "experimental_condition"
}

def load_eeg(csv_path: str):
    """Load EEG data and compute statistical features per band."""
    df = pd.read_csv(csv_path)

    if not REQUIRED.issubset(df.columns):
        raise ValueError(f"Missing required columns. Required: {REQUIRED}")

    df["frequency_band"] = df["frequency_band"].astype(str).str.capitalize()

    agg = defaultdict(lambda: {b: [] for b in BANDS})

    for _, row in df.iterrows():
        key = (
            str(row["subject_id"]),
            str(row["brain_region"]),
            str(row["experimental_condition"])
        )
        band = str(row["frequency_band"]).capitalize()
        amp = float(row["signal_amplitude"])
        if band in BANDS:
            agg[key][band].append(amp)

    rows = []
    for (subject, region, cond), band_dict in agg.items():
        feat = {
            "subject_id": subject,
            "brain_region": region,
            "experimental_condition": cond
        }
        for b in BANDS:
            arr = np.array(band_dict[b]) if band_dict[b] else np.array([0.0])
            feat[f"{b}_mean"] = float(np.mean(arr))
            feat[f"{b}_std"] = float(np.std(arr))
            feat[f"{b}_median"] = float(np.median(arr))
            feat[f"{b}_count"] = int(len(arr))
        rows.append(feat)

    features_df = pd.DataFrame(rows)
    return df, features_df