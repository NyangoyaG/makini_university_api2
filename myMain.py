from fastapi import FastAPI
from database.db_setup import Base, engine
from routers import student_router, payment_router
from models import student, payment

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Makini University - Cellulant Integration API",
    description="API for validating students and receiving payment notifications",
    version="1.0.0"
)

# Include routes
app.include_router(student_router.router)
app.include_router(payment_router.router)

@app.get("/")
def home():
    return {"message": "Welcome to Makini University API"}
