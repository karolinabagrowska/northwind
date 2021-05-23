from starlette import status
from starlette.responses import HTMLResponse 
from database import get_db
from typing import List
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Response
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

@router.get("/customers1", response_model=List[schemas.Customer])
async def get_customers(companyName: str, db: Session = Depends(get_db)):
    return crud.get_params(companyName, db)

@router.post("/customers", status_code=status.HTTP_201_CREATED)
async def post_customers(customer_new: schemas.CustomerNew, db: Session = Depends(get_db)):
    return crud.post_customers(customer_new, db)

@router.delete("/customers/{customer_id}", status_code=status.HTTP_204_NO_CONTENT, response_class= Response)
async def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    check_id = crud.get_customer(db, customer_id)
    if check_id is None:
        raise HTTPException(status_code=404)
    return crud.delete_customer(db, customer_id)

@router.post("/employees", status_code=status.HTTP_201_CREATED)
async def post_employees(employee_new: schemas.Employees, db: Session = Depends(get_db)):
    return crud.post_employees(employee_new, db)
    
