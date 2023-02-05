"""Currency"""
from dataclasses import dataclass


class CrossCurrencyError(Exception):
    """
    Raise Error when two currencies are being operated on
    NOTE: This will be a functionality for a later date!
    """


@dataclass
class Currency:
    """Default Currency"""

    value: float
    denomination: str

    def __repr__(self) -> str:
        return f"{self.value:,.2f}"

    def _validate_currencies(self, other: "Currency") -> None:
        if self.denomination != other.denomination:
            raise CrossCurrencyError()

    def __add__(self, other: "Currency") -> "Currency":
        print("got here")
        self._validate_currencies(other)
        return Currency(
            value=(self.value + other.value),
            denomination=self.denomination,
        )

    def __radd__(self, other) -> "Currency":
        """
        Required for sum -- summation starts with 0 + x

        NOTE: Does not require currency check
        """
        return Currency(
            value=self.value + other,
            denomination=self.denomination,
        )

    def __sub__(self, other: "Currency") -> "Currency":
        self._validate_currencies(other)
        return Currency(
            value=(self.value - other.value),
            denomination=self.denomination,
        )
