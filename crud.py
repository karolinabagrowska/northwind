from sqlalchemy.orm import Session
import models,schemas


def get_customers(db: Session):
    return db.query(models.Customer).all()

def get_params(companyName: str, db: Session):
    companies = db.query(models.Customer).filter(models.Customer.CompanyName == companyName).all()

    return companies
    