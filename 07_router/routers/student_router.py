from fastapi import APIRouter

student = APIRouter(
    prefix="/api/students",
    tags=["students"]
)

@student.get("/")
async def geet_student():
    return {"message" : "학생입니다!"}