"""
FastAPI todo app schemas
"""

from typing import Optional
from sqlmodel import SQLModel, Field


class Todo(SQLModel, table=True):
    """
    Todo schema (SQLModel)
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    completed: bool = False


class CreateTodo(SQLModel):
    """
    Todo create schema
    """

    title: str
