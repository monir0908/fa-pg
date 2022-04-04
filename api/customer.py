from fastapi import APIRouter


router = APIRouter(
    prefix ="/api/customer",
    tags = "Customer API endpoints"
)