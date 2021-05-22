from sqlalchemy import (
    Column,
    Date,
    Float,
    Integer,
    LargeBinary,
    SmallInteger,
    String,
    Table,
    Text,
    CHAR
)
#from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import NullType

from database import Base

class Customer(Base):
    __tablename__ = "customers"

    CustomerID = Column(CHAR(6), primary_key=True)
    CompanyName = Column(String(40), nullable=False)
    ContactName = Column(String(30))
    ContactTitle = Column(String(30))
    Address = Column(String(60))
    City = Column(String(15))
    Region = Column(String(15))
    PostalCode = Column(String(10))
    Country = Column(String(15))
    Phone = Column(String(24))
    Fax = Column(String(24))

class Employee(Base):
    __tablename__ = "employees"

    EmployeeID = Column(SmallInteger, primary_key=True)
    LastName = Column(String(20), nullable=False)
    FirstName = Column(String(10), nullable=False)
    Title = Column(String(30))
    TitleOfCourtesy = Column(String(25))
    BirthDate = Column(Date)
    HireDate = Column(Date)
    Address = Column(String(60))
    City = Column(String(15))
    Region = Column(String(15))
    PostalCode = Column(String(10))
    Country = Column(String(15))
    HomePhone = Column(String(24))
    Extension = Column(String(4))
    Photo = Column(LargeBinary)
    Notes = Column(Text)
    ReportsTo = Column(SmallInteger)
    PhotoPath = Column(String(255))
