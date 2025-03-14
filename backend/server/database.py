from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "your_connection_string"
DATABASE_NAME = "your_database_name"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

def get_database():
    return db

async def close_database():
    client.close()