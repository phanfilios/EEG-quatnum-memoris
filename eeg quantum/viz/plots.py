import matplotlib.pyplot as plt

def plot_band_distribution(df):
    df.hist(figsize=(12, 8))
    plt.tight_layout()
    return plt