import argparse
import backtrader as bt
import pandas as pd

from app.data.fetch import fetch_data
from app.trading.backtest_executor import BacktestExecutor


def run(plot: bool = True):
    # ===== DATA =====
    df = fetch_data()

    # Ensure datetime index (Backtrader requirement)
    df.index = pd.to_datetime(df.index)

    # ===== CEREBRO =====
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100_000)
    cerebro.broker.setcommission(commission=0.001)

    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)

    cerebro.addstrategy(BacktestExecutor)

    # ===== RUN =====
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue():.2f}")
    cerebro.run()
    print(f"Final Portfolio Value: {cerebro.broker.getvalue():.2f}")

    # ===== CONDITIONAL PLOTTING =====
    if plot:
        # GUI-safe plotting (no interactive window)
        figs = cerebro.plot(style="candlestick", iplot=False)
        fig = figs[0][0]
        fig.savefig("backtest_result.png")
        print("Plot saved to backtest_result.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--plot",
        action="store_true",
        help="Save equity curve plot to file"
    )
    args = parser.parse_args()

    run(plot=args.plot)
