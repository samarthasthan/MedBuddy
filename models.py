from secrets import token_hex
import uuid
from sqlalchemy import Column, Enum, Float, Integer, String, Boolean, DateTime, ForeignKey
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


def generate_uuid():
    return token_hex(16)

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True,
                         index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String,unique=True)
    phone_number = Column(Integer,unique=True)
    gender = Column(String)
    dob = Column(DateTime)
    fcm_token = Column(String)
    firebase_id = Column(String,unique=True)
    date_created = Column(DateTime, default=datetime.now())
    last_login = Column(DateTime)
    is_active = Column(Boolean)
    height=Column(String)
    weight=Column(String)
    profile_url= Column(String)
    is_active= Column(Boolean)
    last_login=Column(DateTime)

class Hospital(Base):
    __tablename__="hospitals"

    hostpital_id=Column(Integer, primary_key=True,
                         index=True, autoincrement=True)
    name= Column(String)
    is_verified= Column(Boolean)
    address= Column(String)
    photo_url= Column(String)


class Doctor(Base):
    __tablename__="doctors"

    doctor_id= Column(Integer, primary_key=True,
                         index=True, autoincrement=True)
    
    first_name = Column(String)
    last_name = Column(String)
    hostpital= Column(String,ForeignKey('hospitals.hostpital_id'))
    profile_url= Column(String)
