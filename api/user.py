from fastapi import APIRouter, Depends

import schemas, models
from models import User
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix ="/api/user",
    tags = ["User API Endpoints"]
)


@router.post("/create", response_model=schemas.User)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    user = schemas.User(
        id=1,
        first_name="a first name",
        last_name="dfsdf",
        mobile="3423424"
    )
    return user
    