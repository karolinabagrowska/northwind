from starlette.responses import HTMLResponse
from database import get_db
from typing import List
from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
import crud, models, schemas


router = APIRouter()

@router.get("/customers", response_model=List[schemas.Customer])
async def get_customer(db: Session = Depends(get_db)):

    return crud.get_customers(db)

