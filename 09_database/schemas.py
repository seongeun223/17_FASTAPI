from pydantic import BaseModel
from typing_extensions import Optional

# request 받거나, response를 받을 때
# 기본 형식을 만들어 놓을 수 있다.
class TeacherBase(BaseModel):
    name: str
    is_active: bool
    nickname: Optional[str] = None
    description: Optional[str] = None
    
# SqlAlchemy 모델 : 데이터베이스의 통신을 위한 데이터 구조 정의
# Pydantic 모델 : API 요청과 응답을 위한 데이터 구조 정의
    
# requset 요청 모델
class TeacherCreate(TeacherBase):
    pass

# response 응답 모델
class TeacherResponse(TeacherBase):
    id: int
    
# 업데이트할 때 사용되는 모델
class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None
    nickname: Optional[str] = None
    description: Optional[str] = None
    
# ---------------------------------------------------------------------------------------
    
# Student
class StudentBase(BaseModel):
    name: str
    lunch_menu: Optional[str] = None
    nickname: Optional[str] = None
    description: Optional[str] = None
    
class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    
class StudentModify(BaseModel):
    name: Optional[str] = None
    lunch_menu: Optional[str] = None
    nickname: Optional[str] = None
    description: Optional[str] = None