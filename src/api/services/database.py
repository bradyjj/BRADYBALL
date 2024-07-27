# src/api/services/database.py
import asyncpg
from src.common.config import DATABASE_URL


class DatabaseService:
    def __init__(self):
        self.pool = None

    async def connect(self):
        if not self.pool:
            self.pool = await asyncpg.create_pool(DATABASE_URL)

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    async def fetch_data(self, table: str, player: str):
        if not self.pool:
            await self.connect()

        query = f"SELECT * FROM {table} WHERE player = $1"
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, player)


db_service = DatabaseService()
