import backtrader as bt
import pandas as pd

from app.core.strategy import Strategy
from app.core.risk import RiskManager


class BacktestExecutor(bt.Strategy):
    params = dict(
        lookback=50
    )

    def __init__(self):
        self.strategy_engine = Strategy()
        self.risk_manager = RiskManager()

        # For plotting & logging
        self.buy_signals = []
        self.sell_signals = []

    def next(self):
        # Ensure causal window
        if len(self.data) < self.p.lookback:
            return

        # Convert Backtrader data to pandas (PAST ONLY)
        df = self.data._dataname.iloc[:len(self.data)]

        # === STRATEGY ===
        signal = self.strategy_engine.generate_signal(df)
        # Expected: 1 (buy), 0 (hold), -1 (sell)

        # === RISK ===
        decision = self.risk_manager.evaluate(
            signal=signal,
            price=self.data.close[0],
            cash=self.broker.getcash(),
            position=self.position.size
        )

        if not decision.get("allow_trade", False):
            return

        size = decision.get("size", 0)
        if size <= 0:
            return

        # === EXECUTION ===
        if signal == 1 and not self.position:
            self.buy(size=size)
            self.buy_signals.append(len(self.data))

        elif signal == -1 and self.position:
            self.sell(size=size)
            self.sell_signals.append(len(self.data))
