from enum import Enum
from pathlib import Path


class Paths(Enum):
    ROOT = Path.cwd()
    DATAPATH = ROOT / "src" / "data" / "iris-prep.csv"
    PLOT = DATAPATH.parent.joinpath("plot.png")
    MODELJOB = ROOT / "src" / "model" / "model.joblib"
