from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlmodel import Session, select
from fastapi.middleware.cors import CORSMiddleware
from models import Todo, Contact
from email_utils import send_contact_email
from sqlmodel import create_engine
from sqlmodel import SQLModel

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from auth import verify_google_token, create_jwt_token

# Database setup
DATABASE_URL = "sqlite:///./todos.db"  # Change this to PostgreSQL if needed
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your Vite dev URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello !": "Backend "}

@app.post("/contact")
async def contact_form(contact: Contact, session: Session = Depends(get_session)):
    session.add(contact)
    session.commit()
    await send_contact_email(contact.name, contact.email, contact.message)
    return {"message": "Message sent successfully!"}

@app.post("/auth/google")
async def google_auth(payload: dict):
    token = payload.get("token")
    if not token:
        return {"error": "Missing token"}

    user_info = verify_google_token(token)
    jwt_token = create_jwt_token(user_info)

    return {
        "access_token": jwt_token,
        "token_type": "bearer",
        "user": user_info,
    }
































@app.get("/todos")
def get_todos():
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
        return todos

@app.post("/todos")
def create_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo.title = updated_todo.title
        todo.completed = updated_todo.completed
        session.commit()
        return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        session.delete(todo)
        session.commit()
        return {"ok": True}