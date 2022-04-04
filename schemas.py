from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Customer(BaseModel):
    first_name: str
    last_name: str
    dob: Optional [datetime]
    