from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete as delete_query


async def delete(session: AsyncSession, instance, **kwargs) -> None:
    await session.execute(delete_query(instance).filter_by(**kwargs))
