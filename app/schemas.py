from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

class UserAttaching(BaseModel):
    nick: str

class UserCreate(BaseModel):
    nick: str
    password: str
    class Config:
        orm_mode=True
    
class ChangePassword(BaseModel):
    password: str

class UserOut(BaseModel):
    nick: str
    created_at: datetime
    class Config:
        orm_mode=True

class AccountCreate(BaseModel):
    name: str

class Account(BaseModel):
    ID_Acc: int
    name: str
    class Config:
        orm_mode=True

class AccountOut(Account):
    owners: List[UserOut]
    class Config:
        orm_mode=True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
class CreateCategoryInput(BaseModel):
    name: str
    class Config:
        orm_mode=True
        
class CreateCategoryOutput(CreateCategoryInput):
    ID_Cat: int
        
class PredictionIn(BaseModel):
    value: float
    purpose_of_the_expendture: str
    date: date
    account: int
    category:int
    class Config:
        orm_mode=True
    
class PredictionOut(PredictionIn):
    ID_Pred: int
    class Config:
        orm_mode=True
        
class PredictionChange(BaseModel):
    value: Optional[float]
    purpose_of_the_expendture: Optional[str]
    date: Optional[date]
    account: Optional[int]
    category:Optional[int]
    class Config:
        orm_mode=True

class Operation(BaseModel):
    value: float
    purpose_of_the_expendture: str
    date: date
    prediction : Optional[int]
    account : int
    category: int
    class Config:
        orm_mode=True

class TransferIn(BaseModel):
    date: date
    value: float
    from_account: int
    to_account: int
    class Config:
        orm_mode=True
        
class Transfer(TransferIn):
    ID_Tr: int
        
class TransferChange(BaseModel):
    date: Optional[date]
    value: Optional[float]
    from_account: Optional[int]
    to_account: Optional[int]
    class Config:
        orm_mode=True