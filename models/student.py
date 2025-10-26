from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db_setup import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    program = Column(String, nullable=False)
    year_of_study = Column(Integer, nullable=False)

    payments = relationship("Payment", back_populates="student")

