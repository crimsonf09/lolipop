from fastapi import FastAPI
from app.core.strategy import Strategy
from app.data.fetch import fetch_data
from app.trading.mt5_executor import MT5Executor

app = FastAPI()
strategy = Strategy()
executor = MT5Executor()

@app.post("/trade")
def trade():
    df = fetch_data(period="5d", interval="5m")
    signal = strategy.generate_signal(df)
    executor.execute(signal)
    return {"signal": signal}
