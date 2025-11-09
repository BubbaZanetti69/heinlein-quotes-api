from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Quote
import random

app = FastAPI(
    title="Heinlein Quotes API",
    description="Get random or filtered quotes from Robert Heinlein novels.",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/quotes/random", summary="Get a random Heinlein quote")
def get_random_quote(db: Session = Depends(get_db)):
    quotes = db.query(Quote).all()
    if not quotes:
        raise HTTPException(status_code=404, detail="No quotes found.")
    return random.choice([{"quote": q.quote, "novel": q.novel} for q in quotes])

@app.get("/quotes/{novel}", summary="Get a random quote from specified novel")
def get_quote_by_novel(novel: str, db: Session = Depends(get_db)):
    quotes = db.query(Quote).filter(Quote.novel.ilike(novel)).all()
    if not quotes:
        raise HTTPException(status_code=404, detail="Novel not found.")
    quote = random.choice(quotes)
    return {"quote": quote.quote, "novel": quote.novel}

@app.get("/quotes", summary="Find quotes (optionally filtered by novel/search)")
def search_quotes(
    novel: str = Query(None, description="Filter by novel name"),
    search: str = Query(None, description="Search for text in quote"),
    db: Session = Depends(get_db)
):
    query = db.query(Quote)
    if novel:
        query = query.filter(Quote.novel.ilike(f"%{novel}%"))
    if search:
        query = query.filter(Quote.quote.ilike(f"%{search}%"))
    quotes = query.all()
    return [{"quote": q.quote, "novel": q.novel} for q in quotes]

@app.get("/novels", summary="List all novels included in the database")
def list_novels(db: Session = Depends(get_db)):
    novels = db.query(Quote.novel).distinct()
    return sorted([n[0] for n in novels])

class QuoteCreate(BaseModel):
    quote: str
    novel: str

@app.post("/quotes")
def create_quote(quote_in: QuoteCreate):
    db: Session = SessionLocal()
    db_quote = Quote(quote=quote_in.quote, novel=quote_in.novel)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    db.close()
    return {"message": "Quote added!", "id": db_quote.id}
