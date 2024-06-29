from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/documents", response_model=List[schemas.Document])
def read_documents(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    documents = crud.get_documents(db, skip=skip, limit=limit)
    return documents

@app.post("/documents", response_model=schemas.Document)
def create_document(document: schemas.DocumentCreate, db: Session = Depends(database.get_db)):
    return crud.create_document(db, document)
