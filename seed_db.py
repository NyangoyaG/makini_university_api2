from database.db_setup import Base, engine, SessionLocal
from models.student import Student
from models.payment import Payment

# Create tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear old data
db.query(Payment).delete()
db.query(Student).delete()
db.commit()

# Add students
db.add_all([
    Student(student_id="CS001", full_name="Faith Doe", program="Computer Science", year_of_study=4),
    Student(student_id="CS002", full_name="Geofrey Nyangoya", program="Information Technology", year_of_study=3),
    Student(student_id="CS034", full_name="Bravo Johns", program="Computer Science", year_of_study=3),
    Student(student_id="CS009", full_name="Jeff Nyangoya", program="Information Technology", year_of_study=1),
])
db.commit()
db.close()

print("Students seeded successfully, database created: studentDb.db")

