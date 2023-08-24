import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent.parent.resolve()
DB_DIR = BASE_DIR / 'db'
DB_URL = f"sqlite:///{DB_DIR}/db.sqlite3"

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')
