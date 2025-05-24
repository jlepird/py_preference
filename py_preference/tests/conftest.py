from pytest import fixture
import polars as pl
import seaborn as sns


@fixture
def example_dataframe() -> pl.DataFrame:
    return pl.from_pandas(sns.load_dataset("mpg"))
