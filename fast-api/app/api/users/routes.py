from fastapi import APIRouter
from uuid import UUID

from app.db import postgres
from psycopg.rows import dict_row

router = router = APIRouter(prefix="/users")

@router.get("/")
async def get_users(limit: int = 10, skip: int = 0):
    query = "SELECT * FROM users LIMIT %s OFFSET %s"
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, (limit, skip))
            rows = await cur.fetchall()
            return {"users": rows}
    
@router.get("/{user_id}")
async def get_user(user_id: UUID):
    query = "SELECT * FROM users WHERE user_id = %s"
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, (str(user_id),))
            row = await cur.fetchone()
            return row

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

@router.get("/{user_id}/memberships")
async def get_audiences(user_id: UUID, limit: int = 10, skip = 0):
    query = "SELECT * FROM memberships WHERE user_id = %s LIMIT %s OFFSET %s"
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, (str(user_id), limit, skip))
            row = await cur.fetchall()
            return row
        
@router.get("/{user_id}/friends")
async def get_friends(user_id: UUID, limit: int = 10, skip: int = 0):
    query = """
    SELECT
        CASE WHEN user_a_id = %(user_id)s THEN user_b_id ELSE user_a_id END AS friend_id,
        created_at, updated_at
    FROM 
        friends
    WHERE %(user_id)s IN (user_a_id, user_b_id)
    LIMIT %(limit)s
    OFFSET %(skip)s;
    """
    params = {"user_id": user_id, "limit": limit, "skip": skip}
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, params)
            rows = await cur.fetchall()
            return rows