import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]
DEF_STATIC_DIR = os.path.join(BASE_DIR, "staticfiles")
DEF_MEDIA_DIR = os.path.join(BASE_DIR, "mediafiles")


class Environment:
    def __init__(self):
        self.brand_name = os.getenv("BRAND_NAME") or "Djangonauts Philippines"
        self.app_env = os.getenv("DJANGO_ENV") or "development"
        self.base_url = os.getenv("BASE_URL") or "http://localhost:8000"
        self.secret_key = os.getenv("SECRET_KEY") or "django_insecure_secret_key"
        self.debug = os.getenv("DEBUG") == "True"

        self.static_url = os.getenv("STATIC_URL") or "/static/"
        self.static_root = os.getenv("STATIC_ROOT") or DEF_STATIC_DIR
        self.media_url = os.getenv("MEDIA_URL") or "/media/"
        self.media_root = os.getenv("MEDIA_ROOT") or DEF_MEDIA_DIR

        self.database_url = os.getenv("DATABASE_URL")
        self.allowed_hosts = self.allowed_hosts = ["*", "localhost"]
        if os.getenv("ALLOWED_HOSTS"):
            self.allowed_hosts = os.getenv("ALLOWED_HOSTS").strip().split(",")


config = Environment()
