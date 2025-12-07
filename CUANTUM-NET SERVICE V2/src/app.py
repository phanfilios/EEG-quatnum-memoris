import argparse
from data.loader import load_eeg
from ml.features import flatten_features
from quantum.embedding import eeg_to_quantum_state
from quantum.circuits import build_full_quantum_model
from quantum.expectations import get_expectation_values
from viz.plots import plot_band_distribution

def run_system(csv_path):
    df, features = load_eeg(csv_path)

    row = features.iloc[0]
    vec = flatten_features(row)

    embedded = eeg_to_quantum_state(vec)
    model = build_full_quantum_model(embedded)

    expectations = get_expectation_values(model)

    plot_band_distribution(df)

    return expectations

def main():
    parser = argparse.ArgumentParser(description="EEG Quantum Net System")
    parser.add_argument("csv_path", help="Path to EEG CSV file")
    args = parser.parse_args()

    results = run_system(args.csv_path)
    print("Expectation values:", results)

if __name__ == "__main__":
    main()