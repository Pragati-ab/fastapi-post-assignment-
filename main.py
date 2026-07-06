from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Guide",
        "author": "R K Narayan",
        "genre": "Fiction",
        "language": "English"
    },
    {
        "id": 2,
        "title": "Wings of Fire",
        "author": "A P J Abdul Kalam",
        "genre": "Biography",
        "language": "English"
    }
]

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    language: str

@app.get("/books")
def get_books():
    return books

@app.post("/books",status_code=201)
def create_book(book: BookCreate):
    new_id = max((book["id"] for book in books), default=0) + 1
    new_book = {
        "id" : new_id,
        "title" : book.title,
        "author" : book.author,
        "genre" : book.genre,
        "language" : book.language
    }
    books.append(new_book)

    return {
        "message" : "Book Added Sucessfully",
        "book" : new_book
    }