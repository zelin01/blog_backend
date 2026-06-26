from fastapi import FastAPI
from app.db.base import engine, Base
from app.api.v1.posts import router as posts_router

Base.metadata.create_all(bind = engine)

app = FastAPI(title = "Blog API")

app.include_router(posts_router, prefix = "/api/v1")

@app.get("/")
def root():
    return {"message": "Blog API Runing"}