import typing
from copy import deepcopy
from typing import Any, Generic, Type, TypeVar

from sqlalchemy import delete, func, select, update
from sqlalchemy.cimmutabledict import immutabledict
from sqlalchemy.engine import Result
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm import Query

from infrastructure.database.base import Base

ConcreteSchema = TypeVar("ConcreteSchema", bound=Base)

__all__ = ["BaseCRUD"]


class BaseCRUD(Generic[ConcreteSchema]):
    schema_class: Type[ConcreteSchema]

    def __init__(self, session):
        self.session = session

    async def _execute(self, query: Query) -> Result:
        """Executes the specified query and returns the result"""
        return await self.session.execute(
            query,
            execution_options=immutabledict({"synchronize_session": False}),
        )

    async def _update_one(
        self, lookup: str, value: Any, schema: ConcreteSchema
    ) -> ConcreteSchema:
        """
        Updates records by lookup and return one record wrapped to schema
        Error cases:
         1. If there is no record to return then raise
                sqlalchemy.exc.NoResultFound
         2. If there is more than 1 record is updated then raise
                sqlalchemy.exc.MultipleResultsFound
        """
        query = update(self.schema_class)
        query = query.where(getattr(self.schema_class, lookup) == value)
        query = query.values(**dict(schema))
        query = query.returning(self.schema_class)
        db_result = await self._execute(query)
        results = db_result.fetchall()
        if len(results) == 0:
            raise NoResultFound()
        elif len(results) > 1:
            raise MultipleResultsFound()
        return self.schema_class(**dict(zip(results[0].keys(), results[0])))

    async def _update(
        self,
        lookup: str,
        value: Any,
        schema: ConcreteSchema,
    ) -> list[ConcreteSchema]:
        """
        Update records by lookup and return records wrapped to schema
        """

        query = update(self.schema_class)
        query = query.where(getattr(self.schema_class, lookup) == value)
        query = query.values(**dict(schema))
        query = query.returning(self.schema_class)

        db_result = await self._execute(query)
        results = db_result.fetchall()
        return [
            self.schema_class(**dict(zip(result.keys(), result)))
            for result in results
        ]

    async def _get(self, key: str, value: Any) -> ConcreteSchema | None:
        """Return only one result by filters"""

        query = select(self.schema_class).where(
            getattr(self.schema_class, key) == value
        )
        results = await self._execute(query=query)

        return results.scalars().one_or_none()

    async def _create(self, schema: ConcreteSchema) -> ConcreteSchema:
        """Creates a new instance of the model in the related table"""
        self.session.add(schema)
        await self.session.flush()
        await self.session.refresh(schema)

        return deepcopy(schema)

    async def _create_many(
        self, schemas: list[ConcreteSchema]
    ) -> list[ConcreteSchema]:
        """Creates a new instance of the model in the related table"""
        self.session.add_all(schemas)
        await self.session.flush()
        for schema in schemas:
            await self.session.refresh(schema)
        return deepcopy(schemas)

    async def _all(self) -> list[ConcreteSchema]:
        query = select(self.schema_class)
        results = await self._execute(query=query)

        return results.scalars().all()

    async def count(self) -> int:
        query = func.count(self.schema_class.id)
        results = await self._execute(query=query)

        value = results.scalar()

        if not isinstance(value, int):
            raise Exception(
                "For some reason count function returned not an integer."
                f"Value: {value}",
            )

        return value

    async def _delete(self, key: str, value: Any) -> None:
        query: Query = delete(self.schema_class).where(
            getattr(self.schema_class, key) == value
        )
        await self._execute(query)

        return None

    async def exist_by_key(self, key: str, val: typing.Any) -> bool:
        field = getattr(self.schema_class, key)
        query: Query = select(field)
        query = query.where(field == val)
        query = query.where(
            self.schema_class.is_deleted == False  # noqa: E712
        )
        query = query.exists()
        db_result = await self._execute(select(query))
        return db_result.scalars().first() or False
