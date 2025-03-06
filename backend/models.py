from sqlalchemy import Integer, String, Float, Column, DateTime, func
from database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    categoria = Column(String)
    email_fornecedor = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
    