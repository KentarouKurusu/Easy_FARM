from decouple import config
import motor.motor_asyncio
import asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
client.get_io_loop = asyncio.get_event_loop

database = client.EasyFARM_Database
collection_todo = database.Todo

def todo_serializer(todo) -> dict:
    return{
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"]
    }

async def db_get_todos() -> list:
    todos = []
    for todo in await collection_todo.find().to_list(length=100):
        todos.append(todo_serializer(todo))
    return todos