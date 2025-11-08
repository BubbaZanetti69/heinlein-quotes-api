from database import Base, engine, SessionLocal
from models import Quote

# Drop & recreate tables (safe for dev/demo)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

quotes_data = [
    {"novel": "The Moon Is a Harsh Mistress", "quote": "There ain't no such thing as a free lunch."},
    {"novel": "Stranger in a Strange Land", "quote": "I never do anything I don't want to do. Nor does anyone, but in my case I am always aware of it."},
    {"novel": "Have Space Suit—Will Travel", "quote": "When in danger or in doubt, run in circles, scream and shout."},
    {"novel": "The Cat Who Walks Through Walls", "quote": "A generation which ignores history has no past—and no future."},
    {"novel": "Double Star", "quote": "If you don't like yourself, you can't like other people."},
    {"novel": "Time Enough for Love", "quote": "Never try to teach a pig to sing; it wastes your time and annoys the pig."},
    {"novel": "Starship Troopers", "quote": "Violence, naked force, has settled more issues in history than has any other factor."},
]

db = SessionLocal()
for item in quotes_data:
    db.add(Quote(**item))
db.commit()
db.close()
print("Database populated with demo quotes.")