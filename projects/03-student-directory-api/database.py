from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select

DATABASE_URL = "postgresql://postgres:***@localhost/student_directory"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[int] = mapped_column(primary_key=True)
    student_name: Mapped[str] = mapped_column(String(50), nullable=False)
    student_age: Mapped[int] = mapped_column(nullable=False)
    student_course: Mapped[str] = mapped_column(String(70), nullable=False)
    enrollment_status: Mapped[bool] = mapped_column(default=True)

db = SessionLocal()

statement = select(Student)
result = db.execute(statement)

students = result.scalars().all()

for student in students:
    print(f"{student.student_name} - {student.student_age} - {student.student_course}")

db.close()