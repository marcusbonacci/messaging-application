import psycopg
from psycopg_pool import AsyncConnectionPool
import dotenv

config = dotenv.dotenv_values("../.env")


database = 'main'
user = 'root'
host = '127.0.0.1'
password = config["POSTGRES_PASSWORD"]
port = 5432


DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"

# cursor = connection.cursor(cursor_factory=RealDictCursor)

def get_async_pool():
    return AsyncConnectionPool(DATABASE_URL)