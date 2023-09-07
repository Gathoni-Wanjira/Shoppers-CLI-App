from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key = True)
    first_name = Column(String(), index = True)
    last_name = Column(String(), index = True)
    
    
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key = True)
    product_name = Column(String(), index = True)
    price = Column(Integer())
    product_serialNo = Column(Integer())
    
    
class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer(), primary_key = True)
    
    product_id = Column(Integer(), ForeignKey('products.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
 