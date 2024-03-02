from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, update


async def update_or_create(session: AsyncSession, instance, values: dict, **kwargs) -> None:
    try:
        query = select(instance).filter_by(**kwargs)
        result = (await session.execute(query)).one()
        update_query = update(instance).filter_by(**kwargs).values(**values)
        await session.execute(update_query)
        await session.flush()

    except NoResultFound:
        session.add(instance(**values))
        await session.flush()