from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool

class UpdateTodo(SQLModel):
    title: str | None
    description: str | None
    completed: bool | None
