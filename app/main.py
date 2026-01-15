from fastapi import FastAPI
from app.api.trade import router

app = FastAPI(title="AI Trading Engine")
app.include_router(router)