from sqlalchemy.orm import Session
import models,schemas


def get_customers(db: Session):
    return db.query(models.Customer).all()