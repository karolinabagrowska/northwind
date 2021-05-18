from pydantic import BaseModel
from typing import Optional

from pydantic.types import constr

class Customer(BaseModel):
    CompanyName: Optional[constr(max_length=40)]

    class Config:
        orm_mode = True