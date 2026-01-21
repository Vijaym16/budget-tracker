from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float
    description: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionRead(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
