from sqlalchemy.orm import Session
import models,schemas


def get_customers(db: Session):
    return db.query(models.Customer).all()

def get_params(companyName: str, db: Session):
    companies = db.query(models.Customer).filter(models.Customer.CompanyName == companyName).all()

    return companies

def post_customers(customer_new: schemas.CustomerNew, db: Session):
    customer_add = models.Customer(
        CustomerID = customer_new.CustomerID,
        CompanyName = customer_new.CompanyName,
        ContactName = customer_new.ContactName,
        ContactTitle = customer_new.ContactTitle,
        Address = customer_new.Address,
        City = customer_new.City,
        Region = customer_new.Region,
        PostalCode = customer_new.PostalCode,
        Country = customer_new.Country,
        Phone = customer_new.Phone,
        Fax = customer_new.Fax
    )
    db.add(customer_add)
    db.commit()
    db.refresh(customer_add)

    return customer_add
    