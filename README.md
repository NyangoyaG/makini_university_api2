          +----------------+
          |    Student     |
          |----------------|
          | student_id     |
          | full_name      |
          | program        |
          | year_of_study  |
          +----------------+
                  |
                  | 1-to-many
                  v
          +----------------+
          |    Payment     |
          |----------------|
          | payment_id     |
          | student_id     |
          | amount         |
          | payment_method |
          | transaction_id |
          | timestamp      |
          +----------------+

Welcome to the Makini University API! 🎓
This REST API is designed to integrate student data and payment notifications efficiently and developer-friendly. Think of it as a lightweight bridge between student records and payment systems.

Features

✅ Fetch student information by ID
✅ Record payments made by students
✅ Track payment history
✅ Simple, clean, and ready-to-use REST endpoints

Getting Started

Follow these instructions to set up the project locally for development and testing.

Clone the repository

git clone https://github.com/NyangoyaG/makini_university_api2.git
cd makini_university_api


Set up a virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Seed the database

python3 seed_db.py


This will create studentDb.db with predefined students and payment structures.

Run the API server

uvicorn myMain:app --reload


Open your browser and navigate to:

http://127.0.0.1:8000/

You should see:

{"message":"Welcome to Makini University API"}

API Endpoints
Students

Get student info by ID

GET /students/{student_id}


Example request:

curl http://127.0.0.1:8000/students/CS002


Response:

{
  "student_id": "CS002",
  "full_name": "Geofrey Nyangoya",
  "program": "Information Technology",
  "year_of_study": 3
}

Payments

Notify payment

POST /payments/notify?student_id={id}&amount={amount}&payment_method={method}&transaction_id={txn_id}


Example request:

curl -X POST "http://127.0.0.1:8000/payments/notify?student_id=CS001&amount=1500&payment_method=M-Pesa&transaction_id=TXN1001"

Response:

{
  "message": "Payment received successfully!"
}

Project Structure
makini_university_api2/
│
├── myMain.py               # Main FastAPI application
├── seed_db.py              # Database seeding script
├── database/
│   └── db_setup.py         # SQLAlchemy engine and session
├── models/
│   ├── student.py          # Student model
│   └── payment.py          # Payment model
├── routers/
│   ├── student_router.py   # Student endpoints
│   └── payment_router.py   # Payment endpoints
└── requirements.txt        # Project dependencies

Notes

SQLite is used for simplicity, but the setup is compatible with other databases.

The timestamp for payments is automatically generated when a payment is recorded.

Relationships between Students and Payments are set using SQLAlchemy relationship() for seamless data retrieval.

GitHub Repository

Check out the full project here:
https://github.com/NyangoyaG/makini_university_api2
