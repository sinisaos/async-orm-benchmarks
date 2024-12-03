import asyncpg


class DbConnection:
    async def connect(self):
        self.pool = await asyncpg.create_pool(
            "postgresql://postgres:postgres@localhost:5432/perfdb",
        )

    async def disconnect(self):
        self.pool.terminate()


database = DbConnection()
