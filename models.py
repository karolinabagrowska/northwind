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
)
#from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import NullType

from database import Base

class Customer(Base):
    __tablename__ = "customers"

    CustomerID = Column(NullType, primary_key=True)
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