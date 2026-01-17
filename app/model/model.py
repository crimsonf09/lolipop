# model/model.py
from app.core.signals import Signal

class SimpleModel:
    def predict(self, features: dict) -> Signal:
        rsi = features["rsi"]

        if rsi < 30:
            return Signal.BUY
        if rsi > 70:
            return Signal.SELL
        return Signal.HOLD
