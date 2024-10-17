from fastapi import APIRouter

teacher = APIRouter(
    prefix="/api/teachers",
    tags=["teachers"]
)

@teacher.get("/")
async def geet_student():
    return {"message" : "선생입니다!"}