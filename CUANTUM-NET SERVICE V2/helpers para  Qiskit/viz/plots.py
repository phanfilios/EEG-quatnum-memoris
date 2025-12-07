import matplotlib.pyplot as plt

def plot_band_distribution(df):
  
    fig = df.hist(figsize=(12, 8))
    plt.tight_layout()
    return fig 