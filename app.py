import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(title="API Lab")

DB_HOST = os.getenv("DB_HOST", "banco")
engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{DB_HOST}:5432/{os.getenv('DB_NAME')}"
)

@app.get("/health")
def health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok", "db": DB_HOST}

@app.get("/api/v1/itens")
def listar():
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT * FROM itens")).fetchall()
    return [dict(r._mapping) for r in rows]