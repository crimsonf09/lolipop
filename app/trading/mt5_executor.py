import MetaTrader5 as mt5

class MT5Executor:
    def __init__(self):
        mt5.initialize()

    def execute(self, signal, symbol="EURUSD"):
        if signal == "BUY":
            print("Sending BUY order")
        elif signal == "SELL":
            print("Sending SELL order")
