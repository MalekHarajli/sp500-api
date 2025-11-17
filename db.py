import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load .env relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Validate required environment variables
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        f"""
❌ Missing environment variables.

Loaded from: {ENV_PATH}

SUPABASE_URL found: {SUPABASE_URL is not None}
SUPABASE_KEY found: {SUPABASE_KEY is not None}

Make sure your .env file looks EXACTLY like:

SUPABASE_URL=https://YOUR_PROJECT.supabase.co
SUPABASE_KEY=YOUR_ANON_OR_SERVICE_KEY

No quotes, no spaces, no extra characters.
"""
    )

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_client() -> Client:
    """Helper for routers"""
    return supabase

