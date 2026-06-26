from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.base import get_db
from app.models.post import Post
from app.schemas.post import PostCreate, PostResponse

router = APIRouter(prefix = "/posts", tags = ["blog"])

@router.post("/", response_model = PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/", response_model = List[PostResponse])
def list_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Post).offset(skip).limit(limit).all()

@router.get("/{post_id}", response_model = PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code = 404, detail = "not find blog")
    
@router.put("/{post_id}", response_model = PostResponse)
def update_post(post_id: int, post_update: PostCreate, db: Session = Depends(get_db)):
    post = db.query(Post), filter(Post.id == post.id).first()
    if not post:
        raise HTTPException(status_code = 404, detail = "not find blog")
    post.title = post_update.title
    post.content = post_update.content
    db.commif()
    db.refresh(post)
    return post

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code = 404, detail = "not find blog")
    db.delete(post)
    db.commit()
    return {"message" : "succeely delete"}