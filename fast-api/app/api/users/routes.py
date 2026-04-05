from fastapi import APIRouter
from uuid import UUID

from app.db import postgres
from psycopg.rows import dict_row

router = router = APIRouter(prefix="/users")

@router.get("/{user_id}")
async def get_user(user_id: UUID):
    query = "SELECT * FROM users WHERE user_id = %s"
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, (str(user_id),))
            row = await cur.fetchone()
            return row

@router.get("/")
async def get_users(limit: int = 10, skip: int = 0):
    query = "SELECT * FROM users LIMIT %s OFFSET %s"
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, (limit, skip))
            rows = await cur.fetchall()
            return {"users": rows}
    
# router.delete("/{user_id}")
# async def delete_user(user_id: UUID):
#     query = "SELECT * FROM users WHERE user_id = %s"
#     async with postgres.get_conn() as conn:
#         async with conn.cursor(row_factory=dict_row) as cur:
#             await cur.execute(query, (str(user_id),))
#             return {"users": "deleted"}
        
# router.put("/{user_id}")
# async def update_user(user_id: UUID):
#     query = "UPDATE * from users WHERE user_id = %s"
#     async with postgres.get_conn() as conn:
#         async with conn.cursor(query, row_factory=dict_row) as cur:
#             await cur.execute(query, (str(user_id),))
#             return {"TBD"}