from fastapi import FastAPI, Depends
from database import session_local, engine
import models, schemas, teacher_crud, student_crud
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# 제너레이터 함수
# 함수가 제너레이팅한 객체를 반환하게 하는 키워드
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        
# teacher 등록
@app.post('/teachers', response_model=schemas.TeacherResponse)
async def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    
    response = teacher_crud.create_teacher(db, teacher)
    
    return response

# [student 등록]
@app.post('/students', response_model=schemas.StudentResponse)
async def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    
    response = student_crud.create_student(db, student)
    
    return response

# teacher 단일 조회
@app.get('/teacher/{teacher_id}', response_model=schemas.TeacherResponse)
async def find_teacher_by_id(teacher_id:int, db: Session = Depends(get_db)):
    
    db_teacher = teacher_crud.get_teacher_by_id(db, teacher_id)
    
    return db_teacher

# teacher 전체 조회
@app.get('/teachers', response_model=list[schemas.TeacherResponse])
async def find_all_teacher(db: Session = Depends(get_db)):
    
    all_teachers = teacher_crud.get_all_teachers(db)
    
    return all_teachers

# [student 전체 조회]
@app.get('/students', response_model=list[schemas.StudentResponse])
async def find_all_student(db:Session = Depends(get_db)):
    
    all_students = student_crud.get_all_students(db)
    
    return all_students

# [student 단일 조회]
@app.get('/students/{student_id}', response_model=schemas.StudentResponse)
async def find_student_by_id(student_id:int, db:Session = Depends(get_db)):
    
    db_student = student_crud.get_student_by_id(db, student_id)
    
    return db_student

# teacher 수정
@app.put('/teachers/{teacher_id}', response_model=schemas.TeacherResponse)
async def update_teacher(teacher_id:int, teacher: schemas.TeacherUpdate, db: Session = Depends(get_db)):
    
    updated_teacher = teacher_crud.update_teacher(db, teacher_id, teacher)
    
    return updated_teacher

# [student 수정]
@app.put('/students/{student_id}', response_model=schemas.StudentResponse)
async def modify_student(student_id:int, student:schemas.StudentModify, db:Session = Depends(get_db)):
    
    modified_student = student_crud.modify_student(db, student_id, student)
    
    return modified_student

# teacher 삭제
@app.delete('/teachers/{teacher_id}', status_code=204)
async def delete_teacher(teacher_id:int, db:Session = Depends(get_db)):
    
    teacher_crud.delete_teacher(db, teacher_id)
    
    return None

# [student 삭제]
@app.delete('/students/{student_id}', status_code=204)
async def delete_student(student_id:int, db:Session = Depends(get_db)):
    
    student_crud.delete_student(db, student_id)
    
    return None