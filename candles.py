from fastapi import APIRouter, HTTPException
from app.db import supabase

router = APIRouter(prefix="/candles", tags=["Candles"])

@router.get("/{symbol}/{timeframe}")
def get_candles(symbol: str, timeframe: str, limit: int = 500):
    valid = ["5m","15m","1h","4h","1d"]
    if timeframe not in valid:
        raise HTTPException(status_code=400, detail="Invalid timeframe")

    table_map = {
        "5m": "historical_prices_5m",
        "15m": "historical_prices_15m",
        "1h": "historical_prices_1h",
        "4h": "historical_prices_4h",
        "1d": "historical_prices_1d"
    }

    table = table_map[timeframe]

    res = (
        supabase.table(table)
        .select("*")
        .eq("symbol", symbol.upper())
        .order("ts", desc=True)
        .limit(limit)
        .execute()
    )
    return res.data[::-1]    # return oldest → newest
