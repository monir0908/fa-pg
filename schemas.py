from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    mobile: str
    
    class Config:
        orm_mode = True
    