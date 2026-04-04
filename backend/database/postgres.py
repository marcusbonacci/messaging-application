import psycopg2
from psycopg2.extras import RealDictCursor
import dotenv

config = dotenv.dotenv_values("../.env")

connection = psycopg2.connect(
    database = 'main',
    user = 'root',
    host = '127.0.0.1',
    password = config["POSTGRES_PASSWORD"],
    port = 5432
)

cursor = connection.cursor(cursor_factory=RealDictCursor)