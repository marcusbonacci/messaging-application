import os

class Settings:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        # Postgres
        self.POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "127.0.0.1")
        self.POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
        self.POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
        self.POSTGRES_DATABASE = os.environ.get("POSTGRES_DB", "main")
        self.POSTGRES_USER = os.environ.get("POSTGRES_USER", "root")
        self.POSTGRES_URI = f"postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}"

CONFIG = Settings()