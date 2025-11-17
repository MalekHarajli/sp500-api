from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

print("Loaded .env from:", env_path)
print("URL:", os.getenv("SUPABASE_URL"))
key = os.getenv("SUPABASE_KEY")
print("KEY:", key[:6] + "..." if key else None)
