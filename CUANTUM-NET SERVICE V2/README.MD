How to integrate and run (exact steps)
Create a directory and save the files in the exact paths under your eeg-quantum-net/src/... project as I indicated.
Make sure you have a virtual environment and the dependencies:
Copy the code

Bash

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt

(If Qiskit fails, install the rest and leave Qiskit for a machine with more resources.)
Run the demo pipeline I already gave you before or the new one:
Copy code

Bash
python src/ml/pipeline_demo.py
# o
python -m src.ml.pipeline    # If you run it as a module, you could add _main_ if you want

To run the tests:
Copy code

Python

# quick example in REPL or a script

import pandas as pd
from viz.dashboard import save_band_histograms, generate_report_html
df = pd.read_csv("data/samples/eeg_data.csv")  # o tu CSV
img = save_band_histograms(df)
html = generate_report_html([img])
print("Reporte:", html)