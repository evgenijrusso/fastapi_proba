from sqlalchemy import select

from database import new_session, TaskOrm
from schema import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()  # создает новый id
            await session.commit()  # отправка данных (id) в БД
            return task.id  # проба

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()  # one, first ....
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas

