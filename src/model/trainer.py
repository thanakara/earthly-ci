import numpy as np
import joblib
from sklearn.svm import SVC
from sklearn.exceptions import NotFittedError

from src.defs.file import Paths


class SVMTrainner:
    def __init__(self, C=1) -> None:
        self._is_fitted = False
        self.svm_clf = SVC(kernel="linear", C=C)

    def fit(self, dataset: tuple[np.ndarray]) -> None:
        self.svm_clf.fit(*dataset)
        self._is_fitted = True

    def serialize(self) -> None:
        if not self._is_fitted:
            raise NotFittedError("SVM not fitted yet.")
        else:
            joblib.dump(
                self.svm_clf, filename=Paths.MODELJOB.value.as_posix(), protocol=4
            )
