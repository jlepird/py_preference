"""Test the add_preference method."""

from py_preference.elicitor import Elicitor
from py_preference.preference import Sample
import polars as pl


def test_add_preference_nothrow(example_dataframe: pl.DataFrame) -> None:
    elicitor = Elicitor()
    elicitor.add_preference(Sample(example_dataframe[0]) > Sample(example_dataframe[1]))
    assert len(elicitor._samples) == 1
