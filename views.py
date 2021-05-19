from starlette.responses import HTMLResponse
from database import get_db
from typing import List
from fastapi import FastAPI, APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import crud, models, schemas


router = APIRouter()

@router.get("/customers", response_model=List[schemas.Customer])
async def get_customer(db: Session = Depends(get_db)):

    return crud.get_customers(db)

@router.get("/customers_html")
async def get_customer(db: Session = Depends(get_db)):
    new_str = ""
    for x in crud.get_customers(db):
        content = f'<h1>Welcome {x.CompanyName} </h1>'
        new_str += content
    return HTMLResponse(content=new_str)
