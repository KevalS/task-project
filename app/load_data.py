import json
from sqlalchemy.orm import Session
from app.database import engine
from app.models import Base, Document

# Create the database tables
Base.metadata.create_all(bind=engine)

# Load the JSON data
with open('data.json') as f:
    documents_data = json.load(f)

# Create a new session
db = Session(bind=engine)

# Insert the data
for document_data in documents_data:
    document = Document(**document_data)
    db.add(document)

db.commit()
db.close()

print("Data loaded successfully!")
