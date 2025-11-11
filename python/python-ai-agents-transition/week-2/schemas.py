# type: ignore
from pydantic import BaseModel

class TeaBase(BaseModel):
    name: str
    description: str | None = None

class TeaCreate(TeaBase):
    pass

class Tea(TeaBase):
    id: int

    class Config:
        orm_mode = True