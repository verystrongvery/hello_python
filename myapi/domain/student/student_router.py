from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.student import student_schema, student_crud

router = APIRouter(prefix="/api/student")

@router.post("/create")
def create_student(_create_student: student_schema.CreateStudent, db: Session = Depends(get_db)):
    student_crud.create_student(db, create_student=_create_student)

@router.get("/detail/{id}", response_model=student_schema.Student)
def student_detail(id: int, db: Session = Depends(get_db)):
    return student_crud.get_student(db, student_id=id)

@router.get("/list", response_model=list[student_schema.Student])
def student_list(db: Session = Depends(get_db)):
    return student_crud.get_student_list(db)

@router.put("/update")
def update_student(_update_student: student_schema.UpdateStudent, db: Session = Depends(get_db)):
    student_crud.update_student(db, _update_student)

@router.post("/delete/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    student_crud.delete_student(db, id)