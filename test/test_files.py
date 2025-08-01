import pytest

from src.defs.file import Paths


@pytest.mark.parametrize(
        "filepath",
        [Paths.DATAPATH, Paths.PLOT, Paths.MODELJOB])
def test_filepaths(filepath: Paths) -> None:
    assert filepath.value.exists()
