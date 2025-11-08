# Heinlein Quotes API

Get random or filtered quotes from Robert Heinlein novels via a free public REST API.

## Features

- Random quote: `/quotes/random`
- Random quote from a novel: `/quotes/{novel}`
- Search/filter all quotes: `/quotes?novel=...&search=...`
- List all available novels: `/novels`
- **Auto-generated docs:** `/docs` (Swagger UI)

---

## Requirements

- Python 3.11+
- [pip](https://pip.pypa.io/)
- (Optional) [Docker](https://docs.docker.com/get-docker/)

---

## Local setup (no Docker)

1. **Clone the repo and install requirements:**

   ```sh
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Initialize and populate the database:**

   ```sh
   python populate.py
   ```

3. **Run the API server:**

   ```sh
   uvicorn main:app --reload
   ```

   Visit [http://localhost:8000/docs](http://localhost:8000/docs) for OpenAPI/Swagger docs.

---

## Docker deployment

1. **Build and start:**

   ```sh
   docker build -t heinlein-quotes .
   docker run -p 8000:8000 heinlein-quotes
   ```

   API is on [http://localhost:8000/](http://localhost:8000/)

2. **Seed the database inside Docker:** *(if you want to reset/repopulate)*

   ```sh
   docker run --rm heinlein-quotes python populate.py
   ```

---

## API Reference

| Endpoint                | Description                         |
|-------------------------|-------------------------------------|
| GET `/quotes/random`    | Random Heinlein quote               |
| GET `/quotes/{novel}`   | Random quote from a specific novel  |
| GET `/quotes`           | Search/filter quotes                |
| GET `/novels`           | List all included novels            |

See `/docs` for full OpenAPI reference and testing!

---

## Postman

- Import `postman_collection.json` into Postman for quick endpoint tests.

---

## Extending

- Edit `populate.py` and re-run it to add more quotes.
- To upgrade to Postgres or MySQL, change `DATABASE_URL` in `database.py` and install the appropriate driver.
- For authentication, see FastAPI’s Security docs.

## License

Demo and educational use only. Quotes used here are brief "fair use" examples, not for commercial redistribution.
