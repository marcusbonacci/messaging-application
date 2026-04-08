from typing import Optional

import psycopg_pool
import os, logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.info("Fired")

from app.core import CONFIG

logger.info(CONFIG.POSTGRES_URI)

_pool: Optional[psycopg_pool.AsyncConnectionPool] = None

async def init_pool():
    print(CONFIG.POSTGRES_URI)
    global _pool
    _pool = psycopg_pool.AsyncConnectionPool(CONFIG.POSTGRES_URI, open=False)
    await _pool.open()

async def close_pool():
    global _pool
    if _pool:
        await _pool.close()

def get_conn():
    global _pool
    return _pool.connection()