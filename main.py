from fastapi import FastAPI
from app.routers import tickers, candles, index

app = FastAPI(title="SP500 Market API")

app.include_router(tickers.router)
app.include_router(candles.router)
app.include_router(index.router)

@app.get("/")
def home():
    return {"status": "running", "service": "SP500 Market API"}
