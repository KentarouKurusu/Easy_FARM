from fastapi import APIRouter
from schemas import Todo
from database import db_get_todos
from typing import List

router = APIRouter()

@router.get("/api/todo", response_model=List[Todo])
async def get_todos():
    res = await db_get_todos()
    return res