from models import Employee
from pydantic import BaseModel
from typing import Optional

from pydantic.types import PositiveInt, constr
from sqlalchemy.sql.base import ColumnSet
from sqlalchemy.sql.sqltypes import CHAR, Date, LargeBinary, SmallInteger, Text

class Customer(BaseModel):
    CustomerID = constr(max_length=6)
    CompanyName: constr(max_length=40)
    ContactName = constr(max_length=30)
    ContactTitle = constr(max_length=30)
    Address = constr(max_length=60)
    City = constr(max_length=15)
    Region = constr(max_length=15)
    PostalCode = constr(max_length=10)
    Country = constr(max_length=15)
    Phone = constr(max_length=24)
    Fax = constr(max_length=24)

    class Config:
        orm_mode = True

class CustomerNew(BaseModel):
    CustomerID: constr(max_length=6)
    CompanyName: constr(max_length=40)
    ContactName: Optional[constr(max_length=30)]
    ContactTitle: Optional[constr(max_length=30)]
    Address: Optional[constr(max_length=60)]
    City: Optional[constr(max_length=15)]
    Region: Optional[constr(max_length=15)]
    PostalCode: Optional[constr(max_length=10)]
    Country: Optional[constr(max_length=15)]
    Phone: Optional[constr(max_length=24)]
    Fax: Optional[constr(max_length=24)]

    class Config:
        orm_mode = True

class Employees(BaseModel):
    LastName: constr(max_length=20)
    FirstName: constr(max_length=10)
    Title: Optional[constr(max_length=10)]
    TitleOfCourtesy: Optional[constr(max_length=25)]
    BirthDate: Optional[constr(max_length=25)]
    HireDate: Optional[constr(max_length=25)]
    Address: Optional[constr(max_length=60)]
    City: Optional[constr(max_length=15)]
    Region: Optional[constr(max_length=15)]
    PostalCode: Optional[constr(max_length=10)]
    Country: Optional[constr(max_length=15)]
    HomePhone: Optional[constr(max_length=24)]
    Extension: Optional[constr(max_length=4)]
    Photo: Optional[constr(max_length=25)]
    Notes: Optional[constr(max_length=25)]
    ReportsTo: Optional[constr(max_length=25)]
    PhotoPath: Optional[constr(max_length=255)]
