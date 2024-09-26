from pydantic import BaseModel


class STaskAdd (BaseModel):
    name: str  # по умолчанию требуется значение (required)
    description: str | None = None


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
