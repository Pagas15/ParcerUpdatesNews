from bot.database.main import engine, Base
from .user import User


async def register_models() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
