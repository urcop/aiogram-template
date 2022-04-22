import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool = Pool = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connect:
            connect: Connection
            async with connect.transaction():
                if fetch:
                    result = await connect.fetch(command, *args)
                elif fetchval:
                    result = await connect.fetchval(command, *args)
                elif fetchrow:
                    result = await connect.fetchrow(command, *args)
                elif execute:
                    result = await connect.execute(command, *args)
            return result


if __name__ == "__main__":
    pass
