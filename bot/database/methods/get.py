from typing import Any
from sqlalchemy import Result, ScalarResult, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from sqlalchemy.exc import NoResultFound


async def get(session: AsyncSession, instance, **kwargs) -> Result[tuple[Any]]:
    try:
        query = select(instance).filter_by(**kwargs)
        result = await session.execute(query)
        return result
    except NoResultFound as no_found:
        raise Exception(f'No query result: {no_found}')


async def get_or_create(session: AsyncSession, instance, values: dict, **kwargs) -> Result[tuple[Any]]:
    try:
        query = select(instance).filter_by(**kwargs)
        result = await session.execute(query)
        return result

    except NoResultFound:
        session.add(instance(**values))


