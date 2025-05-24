from dataclasses import dataclass
import polars as pl
from scipy.stats import rv_continuous


@dataclass(frozen=True)
class Prior:
    """A class to represent a prior distribution for preference elicitation."""

    name: pl.Expr
    """The column expression, typically created with pl.col()."""

    distribution: rv_continuous
    """The scipy.stats distribution object representing the prior."""
