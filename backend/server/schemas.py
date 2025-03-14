from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    phone_number: str
    created_at: str
    updated_at: str