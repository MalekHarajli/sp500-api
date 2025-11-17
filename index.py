from fastapi import APIRouter
from app.db import supabase

router = APIRouter(prefix="/index", tags=["Index"])

@router.get("/latest")
def latest_index_value():
    res = supabase.table("sp500_index_values").select("*").order("ts", desc=True).limit(1).execute()
    return res.data[0] if res.data else None
