from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db_setup import SessionLocal
from models.payment import Payment
from models.student import Student

router = APIRouter(prefix="/payments", tags=["Payments"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/notify")
def receive_payment_notification(student_id: str, amount: float, payment_method: str, transaction_id: str, db: Session = Depends(get_db)):
    # Validate if student exists
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found for payment")

    # Check for duplicate transaction
    existing_txn = db.query(Payment).filter(Payment.transaction_id == transaction_id).first()
    if existing_txn:
        raise HTTPException(status_code=400, detail="Duplicate transaction ID")

    # Record payment
    payment = Payment(
        student_id=student_id,
        amount=amount,
        payment_method=payment_method,
        transaction_id=transaction_id
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)

    return {
        "message": f"Payment of {amount} received successfully for {student.full_name}",
        "transaction_id": payment.transaction_id,
        "payment_method": payment.payment_method
    }

