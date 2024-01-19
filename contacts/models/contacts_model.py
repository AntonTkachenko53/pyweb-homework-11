from sqlalchemy import Column, String, Date, Boolean
from .base import BaseModel, Base


class ContactModel(BaseModel):
    __tablename__ = 'contacts'

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String)
    phone_number = Column(String, nullable=False)
    birthday = Column(Date)
    favorite = Column(Boolean, default=False)
