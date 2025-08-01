import matplotlib.pyplot as plt

from model.trainer import SVMTrainner
from src.data.plot import plot_data, plot_decision_boundary
from src.defs.file import Paths
from src.data.fetch import fetch_iris


def train_job() -> None:
    X, y = fetch_iris(to_csv=True)
    trainer = SVMTrainner(C=100)
    trainer.fit(dataset=(X, y))
    trainer.serialize()

    plot_data(X, y)
    plot_decision_boundary(
        clf=trainer.svm_clf,
        xmin=X.T[0].min(),
        xmax=X.T[0].max()
    )
    plt.savefig(Paths.PLOT.value)



if __name__ == "__main__":
    train_job()
