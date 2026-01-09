from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import SessionLocal, engine
from models import Note as NoteModel
from pydantic import BaseModel, Field
from fastapi import Header, HTTPException, Depends
API_KEY = "supersecret123"

def require_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

NoteModel.metadata.create_all(bind=engine)
Base = declarative_base()

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for learning only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Schemas ----------

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)

class NoteOut(NoteCreate):
    id: int

    class Config:
        from_attributes = True

# ---------- DB Dependency ----------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- Routes ----------

@app.get("/notes", response_model=List[NoteOut])
def get_notes(db: Session = Depends(get_db)):
    return db.query(NoteModel).all()


@app.post(
    "/notes",
    response_model=NoteOut,
    status_code=201,
    dependencies=[Depends(require_api_key)]
)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = NoteModel(
        title=note.title,
        content=note.content
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note




@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.delete("/notes/{note_id}", status_code=204, dependencies=[Depends(require_api_key)])
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
@app.get("/")
def read_root():
    return FileResponse("static/index.html")

class NoteOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True
