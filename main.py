from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from api import home, user
import models
app = FastAPI()

app.include_router(home.router)
app.include_router(user.router)


# To create database tables automatically
models.Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000)