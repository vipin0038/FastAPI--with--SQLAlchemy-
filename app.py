from model import Users
from database import SessionLocal,Base,engine
from fastapi import FastAPI,Depends
from pydantic import BaseModel,EmailStr,ConfigDict
from typing import Optional,List,Annotated,Optional
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse


Base.metadata.create_all(bind = engine)


app = FastAPI()



def get_db():
    db = SessionLocal()
    try: 
       yield db
    finally:
        db.close()


# using pydantic model for schema validation
class UserResponse(BaseModel):
    id : int 
    name : str
    age : int
    email : EmailStr
    

    model_config = ConfigDict(from_attributes=True)


# i don't want ot show the password to user so while creating i use usercreate and while sending you can send user
class UserCreate(UserResponse):    
        password : str
  

# For updaing the details i have used this schema this will help in updating only those details which user wants to update  
class UpdateUser(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    email : Optional[EmailStr] = None
    model_config = ConfigDict(from_attributes=True)


# for posting data
@app.post("/create",response_model=UserResponse)
def create_user(user:UserCreate,db:Session = Depends(get_db)):
    u = Users(**user.model_dump())
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

# for retriving all data
@app.get("/view",response_model=List[UserResponse])
def get_user(db:Session = Depends(get_db)):
    return  db.query(Users).all()


# for retriving a particular data with id 
@app.get("/view/{id}",response_model=UserResponse)
def get_user(id:int,db:Session = Depends(get_db)):
    u = db.query(Users).filter(Users.id == id).first()
    return  u


# for updating whole or specific data with id
@app.put("/create/{id}",response_model=UpdateUser)
def create_user(id:int,user:UpdateUser,db:Session = Depends(get_db)):
    u = db.query(Users).filter(Users.id == id).first()
    updated_data = user.model_dump(exclude_unset=True)
    for key,value in updated_data.items():
       setattr(u, key, value)
    db.commit()
    db.refresh(u)
    return u

# for deleting specific record with id
@app.delete("/delete/{id}",response_class=JSONResponse)
def get_user(id:int,db:Session = Depends(get_db)):
    u = db.query(Users).filter(Users.id == id).first()
    db.delete(u)
    db.commit()
    return {"Message":{f"Details of {id} deleted"}}

    

