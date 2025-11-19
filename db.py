import os
from supabase import create_client, Client

# ============================================================
# ENVIRONMENT VARIABLE LOADING
# Works on both local (uvicorn) and Render Web Services
# - Local: .env loaded by uvicorn or manually in your shell
# - Render: env vars set in Render Dashboard
# ============================================================

SUPABASE_URL = os.getenv("https://sdhyewpqmfiiiirxqpbn.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNkaHlld3BxbWZpaWlpcnhxcGJuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MzEzMjMxOCwiZXhwIjoyMDc4NzA4MzE4fQ.HQ82vj224-AEkxZ0IqtvgXdNR3UKSQiYRUgNqINE5u0")  # Use SERVICE ROLE KEY on Render worker, ANON on API

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "❌ Missing SUPABASE_URL or SUPABASE_KEY.\n"
        "Make sure environment variables are set in Render.\n"
        "Do NOT rely on .env when running on Render."
    )

# Create Supabase client instance (reusable)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_client() -> Client:
    """Return shared Supabase client"""
    return supabase
