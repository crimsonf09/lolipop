import pandas as pd

class Strategy:
    def generate_signal(self, df: pd.DataFrame):
        print("Generating signal")
        df = df.copy()

        df.loc[:, "ma_fast"] = df["close"].rolling(window=10, min_periods=10).mean()
        df.loc[:, "ma_slow"] = df["close"].rolling(window=30, min_periods=30).mean()


        if df["ma_fast"].iloc[-2] < df["ma_slow"].iloc[-2] and \
           df["ma_fast"].iloc[-1] > df["ma_slow"].iloc[-1]:
            return "BUY"

        if df["ma_fast"].iloc[-2] > df["ma_slow"].iloc[-2] and \
           df["ma_fast"].iloc[-1] < df["ma_slow"].iloc[-1]:
            return "SELL"

        return "HOLD"
