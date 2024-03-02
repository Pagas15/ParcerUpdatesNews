from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession


async def create(session: AsyncSession, instance, values: dict) -> None:
    try:
        session.add(instance(**values))
        await session.flush()
    except Exception as ex:
        raise Exception(f'Failed to create table in {instance.__tablename__}. {ex}')


async def create_if_not_exist(session: AsyncSession, instance, exist_instance,
                              values: dict, **kwargs):
    try:
        query = select(exist_instance).filter_by(**kwargs)
        exist_result = (await session.execute(query)).one()
    except NoResultFound:
        session.add(instance(**values))
        await session.flush()
