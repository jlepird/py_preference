from polars.testing import assert_frame_equal
from py_preference.preference import Comparator, Sample


def test_basic_sample(example_dataframe) -> None:
    row_0 = example_dataframe[0]
    row_1 = example_dataframe[1]

    pref = Sample(row_0) > Sample(row_1)

    assert_frame_equal(pref._a._data, row_0)
    assert_frame_equal(pref._b._data, row_1)
    assert pref._comp == Comparator.A_PREFERRED_OVER_B
