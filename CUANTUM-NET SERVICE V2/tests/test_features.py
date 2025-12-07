from ml.models import make_rf_pipeline
import numpy as np
import pandas as pd

def test_model_pipeline_fit():
    X = pd.DataFrame(np.random.rand(20,5), columns=["Delta","Theta","Alpha","Beta","Gamma"])
    y = pd.Series(["a","b"] * 10)
    model = make_rf_pipeline()
    model.fit(X, y)
    preds = model.predict(X)
    assert len(preds) == len(y)