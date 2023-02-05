"""Core Accounting Equations"""
from pyfi.types.currency import Currency
from pyfi.types.ratios import Percent


def current_ratio(
    current_assets: list[Currency], current_liabilities: list[Currency]
) -> Percent:
    """Calculate the current ratio

    Params:
        current_assets (float): list of assets
        current_liabilities (float): list of liabilities

    Returns:
        Percentage
    """
    return Percent(sum(current_assets) / sum(current_liabilities))


def net_income(income: list[Currency], expenses: list[Currency]) -> Currency:
    return sum(income) - sum(expenses)


def cost_of_goods_sold(
    open_inventory: Currency, close_inventory: Currency, purchases: Currency
) -> Currency:
    return open_inventory + purchases - close_inventory


def gross_profit(
    sales: Currency,
    open_inventory: Currency | None = None,
    close_inventory: Currency | None = None,
    purchases: Currency | None = None,
    cogs: Currency | None = None,
) -> Currency | None:
    if (
        open_inventory is None
        and close_inventory is None
        and purchases is None
        and cogs is None
    ):
        return None
    if cogs is None:
        return sales - cogs(open_inventory, close_inventory, purchases)
    return sales - cogs
