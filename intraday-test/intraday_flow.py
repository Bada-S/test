"""A Flow used to calculate intra-day trading metrics."""
from prefect import flow

# import calculation_tasks as t


@flow(name="tastytrade Intraday Reporting")
def run_intraday_update():
    """Run a series of calculations on intraday metrics."""
    transactions = t.query_transactions()
    t.update_runtime()
    t.calculate_instrument_metrics(df=transactions)
    t.calculate_symbol_trades(df=transactions)
    t.calculate_account_activity(df=transactions)


if __name__ == "__main__":
    run_intraday_update()
