from fastapi import APIRouter

from app.db import postgres
from psycopg.rows import dict_row

router = APIRouter(prefix="/audience")

@router.get("/")
async def get_audiences(limit: int = 10, skip: int = 0):
    query = "SELECT * FROM audience LIMIT %s OFFSET %s"
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, (limit, skip))
            rows = await cur.fetchall()
            return rows