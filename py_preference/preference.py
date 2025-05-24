from __future__ import annotations

from dataclasses import dataclass
import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import polars as pl


@enum.unique
class Comparator(enum.Enum):
    A_PREFERRED_OVER_B = enum.auto()
    B_PREFERRED_OVER_A = enum.auto()
    EQUIVILANT = enum.auto()


@dataclass(frozen=True)
class Sample:
    _data: pl.DataFrame

    def __eq__(self, other: Sample) -> PreferenceSample:
        return PreferenceSample(self, other, Comparator.EQUIVILANT)

    def __lt__(self, other: Sample) -> PreferenceSample:
        return PreferenceSample(self, other, Comparator.B_PREFERRED_OVER_A)

    def __gt__(self, other: Sample) -> PreferenceSample:
        return PreferenceSample(self, other, Comparator.A_PREFERRED_OVER_B)


@dataclass(frozen=True)
class PreferenceSample:
    _a: Sample
    _b: Sample
    _comp: Comparator
