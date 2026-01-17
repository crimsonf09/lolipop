import backtrader as bt
import pandas as pd

from app.data.fetch import fetch_data
from app.trading.backtest_executor import BacktestExecutor

def run():
    df = fetch_data()

    # Backtrader requires datetime index
    df.index = pd.to_datetime(df.index)

    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100_000)

    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)

    cerebro.addstrategy(BacktestExecutor)

    print("Starting Portfolio Value:", cerebro.broker.getvalue())
    cerebro.run()
    print("Final Portfolio Value:", cerebro.broker.getvalue())

    cerebro.plot(style="candlestick")

if __name__ == "__main__":
    run()
