from fastapi import APIRouter

router = APIRouter()

@router.get("/", include_in_schema=False)
def health_check():
    return {
        'msg': 'health is good'
    }