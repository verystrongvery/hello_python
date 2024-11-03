from models import Student
from sqlalchemy.orm import Session

from domain.student.student_schema import CreateStudent
from domain.student.student_schema import UpdateStudent


def create_student(db: Session, create_student: CreateStudent):
    student = Student(name=create_student.name, age=create_student.age, email=create_student.email)
    db.add(student)
    db.commit()

def get_student_list(db: Session):
    return db.query(Student).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).get(student_id)

def update_student(db: Session, update_student: UpdateStudent):
    student = get_student(db, update_student.id)
    if update_student.name is not None:
        student.name = update_student.name
    if update_student.age is not None:
        student.age = update_student.age
    if update_student.email is not None:
        student.email = update_student.email
    db.commit()

def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    db.delete(student)
    db.commit()