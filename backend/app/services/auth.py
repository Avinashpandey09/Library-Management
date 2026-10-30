
from sqlalchemy.orm import Session
from models.user import User


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(
        User.id == user_id
    ).first()
