from datetime import date

BOOKS_DATA = [
    {"title": "1984", "author": "Джордж Оруэлл", "isbn": "978-5-17-080324-8", "year": 1949, "genre": "Антиутопия", "available_copies": 3},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "isbn": "978-5-389-01660-5", "year": 1967, "genre": "Роман", "available_copies": 2},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "isbn": "978-5-389-02281-1", "year": 1866, "genre": "Классика", "available_copies": 1},
    {"title": "Дюна", "author": "Фрэнк Герберт", "isbn": "978-5-17-091410-4", "year": 1965, "genre": "Фантастика", "available_copies": 4},
    {"title": "Цветы для Элджернона", "author": "Дэниел Киз", "isbn": "978-5-389-05585-7", "year": 1959, "genre": "Драма", "available_copies": 2},
    {"title": "Шерлок Холмс", "author": "Артур Конан Дойл", "isbn": "978-5-17-112341-3", "year": 1892, "genre": "Детектив", "available_copies": 5},
    {"title": "Маленький принц", "author": "Антуан де Сент-Экзюпери", "isbn": "978-5-699-90400-6", "year": 1943, "genre": "Сказка", "available_copies": 3}
]

READERS_DATA = [
    {"full_name": "Алексей Петров", "email": "alex@example.com", "phone": "+79991112233", "registration_date": date(2026, 1, 10)},
    {"full_name": "Мария Сидорова", "email": "maria@example.com", "phone": "+79992223344", "registration_date": date(2026, 1, 15)},
    {"full_name": "Иван Иванов", "email": "ivan@example.com", "phone": "+79993334455", "registration_date": date(2026, 2, 1)},
    {"full_name": "Ольга Кузнецова", "email": "olga@example.com", "phone": "+79994445566", "registration_date": date(2026, 2, 10)},
    {"full_name": "Дмитрий Смирнов", "email": "dima@example.com", "phone": "+79995556677", "registration_date": date(2026, 2, 20)}
]

HISTORY_DATA = [
    (1, 1, date(2026, 1, 12), date(2026, 1, 25)),
    (1, 2, date(2026, 1, 26), date(2026, 2, 10)),
    (1, 3, date(2026, 2, 15), None),  
    
    (2, 4, date(2026, 1, 16), date(2026, 1, 30)),
    (2, 5, date(2026, 2, 1), date(2026, 2, 14)),
    (2, 6, date(2026, 2, 15), date(2026, 2, 28)),
    (2, 7, date(2026, 3, 1), None),  
    
    (3, 2, date(2026, 2, 2), date(2026, 2, 12)),
    (3, 4, date(2026, 2, 13), date(2026, 2, 25)),
    (3, 6, date(2026, 2, 26), None), 
    
    (4, 7, date(2026, 2, 11), date(2026, 2, 20)),
    (4, 1, date(2026, 2, 21), date(2026, 3, 5)),
    (4, 5, date(2026, 3, 6), None),  

    (5, 3, date(2026, 2, 22), date(2026, 3, 2)),
    (5, 6, date(2026, 3, 3), date(2026, 3, 8)),
    (5, 4, date(2026, 3, 9), None) 
]
