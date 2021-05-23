from sqlalchemy.orm import Session
import models,schemas


def get_customers(db: Session):
    return db.query(models.Customer).all()

def get_customer(db: Session, id: str):
    return (
        db.query(models.Customer).filter(models.Customer.CustomerID == id).first()
    )

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

def delete_customer(db: Session, customer_id: str):
    id_delete = db.query(models.Customer).filter(models.Customer.CustomerID == customer_id).first()
    db.delete(id_delete)
    db.commit()
    return

def post_employees(employee_new: schemas.Employees, db: Session):
    employee_add = models.Employee(
        LastName = employee_new.LastName,
        FirstName = employee_new.FirstName,
        Title = employee_new.Title,
        TitleOfCourtesy = employee_new.TitleOfCourtesy,
        BirthDate = employee_new.BirthDate,
        HireDate = employee_new.HireDate,
        Address = employee_new.Address,
        City = employee_new.City,
        Region = employee_new.Region,
        PostalCode = employee_new.PostalCode,
        Country = employee_new.Country,
        HomePhone = employee_new.HomePhone,
        Extension = employee_new.Extension,
        Photo = employee_new.Photo,
        Notes = employee_new.Notes,
        ReportsTo = employee_new.ReportsTo,
        PhotoPath = employee_new.PhotoPath
    )
    db.add(employee_add)
    db.commit()
    db.refresh(employee_add)

    return employee_add


    