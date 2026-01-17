import yfinance as yf
import pandas as pd


def fetch_data(symbol="EURUSD=X", period="1y", interval="1h"):
    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False
    )

    # ---- FIX: flatten MultiIndex columns safely ----
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Now it's a normal Index → safe to use .str
    df.columns = df.columns.str.lower()

    # ---- Backtrader required columns ----
    required = {"open", "high", "low", "close"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Backtrader requires volume
    if "volume" not in df.columns:
        df["volume"] = 0

    # Drop NaNs
    df = df.dropna()

    return df
