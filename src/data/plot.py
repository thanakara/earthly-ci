import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC


def plot_data(X: np.ndarray, y: np.ndarray) -> None:
    plt.plot(X[y == 0, 0], X[y == 0, 1], "b+", label="setosa")
    plt.plot(X[y == 1, 0], X[y == 1, 1], "rx", label="versicolor")
    plt.grid()
    plt.legend()


def plot_decision_boundary(clf: SVC, xmin: float | int, xmax: float | int) -> None:
    w = clf.coef_[0]
    b = clf.intercept_[0]
    x0 = np.linspace(xmin, xmax, 200)
    boundary = -(x0 * w[0] + b) / w[1]
    margin = 1 / w[1]
    gutter_up = boundary + margin
    gutter_down = boundary - margin
    svs = clf.support_vectors_

    plt.plot(x0, boundary, "k")
    plt.plot(x0, gutter_up, "g--", zorder=-2)
    plt.plot(x0, gutter_down, "g--", zorder=-2)
    plt.scatter(svs.T[0], svs.T[1], facecolors="#AAA", s=70, zorder=-1)
