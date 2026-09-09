from pydantic import BaseModel,Field, field_validator

class Book(BaseModel):
    id: int
    author: str
    name: str

class Reader(BaseModel):
    id: int
    name: str
    surname: str

class ReaderProfile(Reader):
    reading_history: list[Book]

class BookDetail(Book):
    is_available: bool
    reader_name: str | None = None