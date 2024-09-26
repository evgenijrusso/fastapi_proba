from fastapi import APIRouter, Depends
from typing import Annotated
from schema import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(prefix='/tasks')  # по умолчанию на всех адрес, а ниже его убираем ('')

#tasks = []


@router.post('')  # убираю у всех
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
# async def add_task(task: Annotated[dict, Depends(STaskAdd)]):  # можно по-другому,
    task_id = await TaskRepository.add_one(task)
    # tasks.append(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async  def get_tasks() -> list[STask]:
#    task = Task(name='Запиши что-нибудь', description='')  # некая запись
    tasks = await TaskRepository.find_all()
    return tasks
