from database import SessionLocal, engine, Base
from models import Book, Reader, ReaderBook
from data import BOOKS_DATA, READERS_DATA, HISTORY_DATA

def seed_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        for book_dict in BOOKS_DATA:
            db_book = Book(**book_dict)
            db.add(db_book)

        for reader_dict in READERS_DATA:
            db_reader = Reader(**reader_dict)
            db.add(db_reader)
        for row in HISTORY_DATA:
            db_history = ReaderBook(
                reader_id=row[0],
                book_id=row[1],
                taken_at=row[2],
                returned_at=row[3]
            )
            db.add(db_history)
        db.commit()
    except Exception as e:
        db.rollback()  
    finally:
        db.close()
