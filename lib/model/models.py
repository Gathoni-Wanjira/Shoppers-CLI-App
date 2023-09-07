from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///shoppers.db')


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key = True)
    first_name = Column(String(), index = True)
    last_name = Column(String(), index = True)
    
    
    def __repr__(self):
        return f"Customer {self.id}: " \
            + f"{self.first_name}, " \
            + f"{self.last_name}, "
    
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key = True)
    product_name = Column(String(), index = True)
    price = Column(Integer())
    product_serialNo = Column(Integer())
    
    
     
    def __repr__(self):
        return f"Product {self.id}: " \
            + f"{self.product_name}, " \
            + f"{self.price}, " \
            + f"{self.product_serialNo}, "
    
    
class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer(), primary_key = True)
    
    product_id = Column(Integer(), ForeignKey('products.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    
    
    def __repr__(self):
        return f"Cart {self.id}: " \
            + f"{self.product_id}, " \
            + f"{self.customer_id}, "
 
 
