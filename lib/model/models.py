
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

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
            
            
            # Establish a many-to-many relationship with Product through Cart
   
carts = relationship("Cart", backref="customer", primaryjoin="Customer.id == Cart.customer_id")
    
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
            
            
    # Establish a many-to-many relationship with Customer through Cart

    carts = relationship("Cart", backref="product", primaryjoin="Product.id == Cart.product_id")


class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer(), primary_key = True)

    product_id = Column(Integer(), ForeignKey('products.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))


    def __repr__(self):
        return f"Cart {self.id}: " \
            + f"{self.product_id}, " \
            + f"{self.customer_id}, "


