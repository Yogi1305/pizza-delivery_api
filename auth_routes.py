from fastapi import APIRouter, Depends, HTTPException
from database import Session, engine
from schemas import SignModel
from model import User
from sqlalchemy.orm import Session as DBSession

auth_router = APIRouter()


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

@auth_router.get("/")
async def hello():
    return {"message": "Hello World from auth routes!"}

@auth_router.post("/signup", status_code=201)
async def signup(user: SignModel, db: DBSession = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.Email == user.Email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        Username=user.Username,
        Email=user.Email,
        Password=user.Password,  
        IsActive=True,
        Is_staff=False
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    
    return {
        "message": "User signed up successfully",
        "user_id": new_user.id,
        "email": new_user.Email
    }