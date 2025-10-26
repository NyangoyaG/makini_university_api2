from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database.db_setup import SessionLocal
from models.student import Student

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/{student_id}")
def get_student(student_id: str):
    db: Session = SessionLocal()
    student = db.query(Student).filter(Student.student_id == student_id).first()
    db.close()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return {
        "student_id": student.student_id,
        "full_name": student.full_name,
        "program": student.program,
        "year_of_study": student.year_of_study
    }

