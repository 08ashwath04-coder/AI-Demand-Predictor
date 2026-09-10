from datetime import datetime
from sqlalchemy import Column,Integer,String,Float,Date,DateTime,ForeignKey
from .database import Base
class User(Base):
 __tablename__='users'; id=Column(Integer,primary_key=True); name=Column(String,nullable=False); email=Column(String,unique=True,index=True,nullable=False); password_hash=Column(String,nullable=False); role=Column(String,nullable=False); created_at=Column(DateTime,default=datetime.utcnow)
class Product(Base):
 __tablename__='products'; id=Column(Integer,primary_key=True); name=Column(String,nullable=False); category=Column(String); description=Column(String)
class Crop(Base):
 __tablename__='crops'; id=Column(Integer,primary_key=True); name=Column(String,nullable=False); season=Column(String); category=Column(String); description=Column(String)
class Sale(Base):
 __tablename__='sales'; id=Column(Integer,primary_key=True); product_id=Column(Integer,ForeignKey('products.id')); quantity=Column(Float); price=Column(Float); date=Column(Date); location=Column(String)
class Inventory(Base):
 __tablename__='inventory'; id=Column(Integer,primary_key=True); product_id=Column(Integer,ForeignKey('products.id')); current_stock=Column(Float); minimum_stock=Column(Float); updated_at=Column(DateTime,default=datetime.utcnow)
class CalendarEvent(Base):
 __tablename__='calendar_events'; id=Column(Integer,primary_key=True); date=Column(Date); title=Column(String); event_type=Column(String); description=Column(String)
