from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlmodel import Session, select

from models import Todo, SQLModel
from sqlmodel import create_engine

# Database setup
DATABASE_URL = "sqlite:///./todos.db"  # Change this to PostgreSQL if needed
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Create a todo
@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, session: Session = Depends(get_session)):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

# Read all todos
@app.get("/todos/", response_model=List[Todo])
def read_todos(session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos

# Read single todo
@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Update a todo
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo, session: Session = Depends(get_session)):
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db_todo.title = updated_todo.title
    db_todo.description = updated_todo.description
    db_todo.completed = updated_todo.completed

    session.commit()
    session.refresh(db_todo)
    return db_todo

# Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    session.delete(db_todo)
    session.commit()
    return {"message": "Todo deleted successfully"}
