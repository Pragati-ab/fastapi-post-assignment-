from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


notes = [
    {
        "id": 1,
        "title": "FastAPI Intro",
        "content": "FastAPI is used to build backend APIs in Python.",
        "category": "Backend",
        "priority": "High"
    },
    {
        "id": 2,
        "title": "Request Body",
        "content": "A request body carries data sent by the client.",
        "category": "API",
        "priority": "Medium"
    }
]

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    priority: str


@app.get('/')
def home():
    return {
        "message": "Notes API is running"
    }


@app.get('/notes')
def get_notes():
    return notes


@app.post('/notes', status_code=201)
def create_note(note: NoteCreate):
    new_id = max([note["id"] for note in notes], default=0) + 1

    new_note = {
        "id": new_id,
        "title": note.title,
        "content": note.content,
        "category": note.category,
        "priority": note.priority
    }

    notes.append(new_note)

    return {
        "message": "Note Added Successfully",
        "note": new_note
    }




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