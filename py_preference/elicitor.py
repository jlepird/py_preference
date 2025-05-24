from py_preference.preference import PreferenceSample
import polars as pl
from dataclasses import dataclass, field
from typeguard import typechecked
from py_preference.priors import Prior


@dataclass
class Elicitor:
    _samples: list[PreferenceSample] = field(default_factory=list)
    _priors: list[Prior] = field(default_factory=list)

    @typechecked
    def add_preference(self, sample: PreferenceSample) -> None:
        self._samples.append(sample)

    def clear_samples(self) -> None:
        self._samples.clear()

    @typechecked
    def add_prior(self, prior: Prior) -> None:
        self._priors.append(prior)

    def _get_log_probability(self, means: pl.Series) -> float:
        return self._get_log_probability_for_priors(
            means
        ) + self._get_log_probability_for_samples(means)

    def _get_log_probability_for_priors(self, means: pl.Series) -> float:
        """Calculate the log probability of the means given the priors."""
        log_probs = pl.Series(
            [
                prior.distribution.logpdf(mean)
                for prior, mean in zip(self._priors, means)
            ]
        )
        return log_probs.sum()

    def _get_log_probability_for_samples(self, means: pl.Series) -> float:
        return means.sum()  # Placeholder for actual sample log probability calculation
