from fastapi import APIRouter


router = APIRouter()

@router.get("/auth/status")
async def auth_status():
    return {"status": "Authentication service is running"}