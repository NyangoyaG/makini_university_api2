from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from database.db_setup import Base
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.student_id"))
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    transaction_id = Column(String, unique=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Use string 'Student' instead of direct class reference
    student = relationship("Student", back_populates="payments")

