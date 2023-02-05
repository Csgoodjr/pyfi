"""Accounting Tests"""
from unittest import TestCase
from pyfi.types.currency import Currency, CrossCurrencyError
from pyfi.accounting import net_income


class TestAccounting(TestCase):
    """Test Accounting Formulas"""

    def test_net_income(self):
        income = [Currency(100.0, "usd"), Currency(200.0, "usd")]
        expenses = [Currency(50.0, "usd")]
        expected = Currency(250.0, "usd")
        self.assertEqual(expected, net_income(income, expenses))

    def tets_net_income_currency_error(self):
        income = [Currency(100.0, "usd"), Currency(100.0, "cad")]
        expenses = [Currency(100.0, "usd")]
        with self.assertRaises(CrossCurrencyError):
            net_income(income, expenses)