from fastapi import APIRouter
from app.db import supabase


router = APIRouter(prefix="/tickers", tags=["Tickers"])

@router.get("/")
def get_tickers():
    res = supabase.table("companies").select("symbol").execute()
    return res.data
