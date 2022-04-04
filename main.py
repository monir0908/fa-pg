from fastapi import FastAPI
import uvicorn

from api import home,customer

app = FastAPI()

app.include_router(home.router)
app.include_router(customer.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)