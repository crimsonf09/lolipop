# model/features.py
def make_features(candle):
    return {
        "rsi": candle["rsi"],
        "ema_fast": candle["ema_fast"],
        "ema_slow": candle["ema_slow"],
    }
