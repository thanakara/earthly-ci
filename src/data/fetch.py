import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

from src.defs.file import Paths


def fetch_iris(to_csv: bool = False) -> tuple[np.ndarray]:
    iris = load_iris(as_frame=True)
    X = iris.data
    X.columns = X.columns.str.replace(" (cm)", "").str.replace(" ", "_")
    X = X[["petal_length", "petal_width"]]
    y = iris.target
    setosa_or_versi = (y == 0) | (y == 1)
    X = X[setosa_or_versi]
    y = y[setosa_or_versi]
    if to_csv:
        datapath = Paths.DATAPATH.value
        df = pd.concat((X, y), axis=1)
        df.to_csv(datapath)
    return X.to_numpy(), y.values
