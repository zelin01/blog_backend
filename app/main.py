import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


from app.api.v1.posts import router as posts_router
from app.api.v1.auth import router as auth_router

from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware


app = FastAPI(title = "Blog API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(posts_router, prefix = "/api/v1")
app.include_router(auth_router, prefix = "/api/v1")


@app.get("/")
def root():
    return {"message": "Blog API Running"}


@app.post("/register")
def register():
    return {"message": "register works"}

@app.get("/posts")
def posts():
    return ["message"]