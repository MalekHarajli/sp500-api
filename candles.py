from fastapi import APIRouter, HTTPException
from app.db import supabase

router = APIRouter(prefix="/candles", tags=["Candles"])

VALID_TF = ["1m", "5m", "15m", "1h", "4h", "1d"]

TABLE_MAP = {
    "1m": "minute_ohlc",
    "5m": "ohlc_5m",
    "15m": "ohlc_15m",
    "1h": "ohlc_1h",
    "4h": "ohlc_4h",
    "1d": "ohlc_1d"
}


@router.get("/{symbol}/{timeframe}")
def get_candles(symbol: str, timeframe: str, limit: int = 500):
    symbol = symbol.upper()

    # 1. Validate timeframe
    if timeframe not in VALID_TF:
        raise HTTPException(status_code=400, detail=f"Invalid timeframe: {timeframe}")

    table = TABLE_MAP[timeframe]

    # 2. Validate symbol exists
    exists = supabase.table("companies").select("symbol").eq("symbol", symbol).execute()
    if not exists.data:
        raise HTTPException(status_code=404, detail=f"Symbol {symbol} not found")

    # 3. Choose correct column for ordering
    order_col = "ts" if timeframe == "1m" else "ts_bucket"

    # 4. Query Supabase
    try:
        res = (
            supabase.table(table)
            .select("*")
            .eq("symbol", symbol)
            .order(order_col, desc=True)
            .limit(limit)
            .execute()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not res.data:
        return []

    # 5. Return in ascending time order: oldest → newest
    return res.data[::-1]
