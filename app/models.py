from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String,create_engine, func,Date
from datetime import date
from database import Base, engine

class Book(Base):
    id = Column(Integer,primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, nullable=False)
    year = Column(Integer, nullable=True)
    genre = Column(String, nullable=False)
    available_copies = Column(Integer, default=1)

class Reader(Base):
    id  = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True,nullable=False)
    phone = Column(Integer, nullable=False)
    registration_date = Column(Date, default=date.today)

class Reader_books(Base):
    id = Column(Integer,primary_key=True)
    reader_id = Column(Integer, ForeignKey('readers.id'),nullable=False)
    book_id  = Column(Integer, ForeignKey('books.id'), nullable=False)
    taken_at = Column(Date, nullable=False)
    returned_at = Column(Date, nullable=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False, default="librarian")
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
