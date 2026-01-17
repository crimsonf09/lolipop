import yfinance as yf
import pandas as pd


def fetch_data(symbol="GC=F", period="10d", interval="5m"):
    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False
    )

    # Flatten MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.columns = df.columns.str.lower()

    # Ensure volume exists
    if "volume" not in df.columns:
        df["volume"] = 0

    df = df[~df.index.duplicated(keep="first")]
    df = df.sort_index()
    df = df.asfreq("5min", method="pad")

    df = df.dropna()
    return df
