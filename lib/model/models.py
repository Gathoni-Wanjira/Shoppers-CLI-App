from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship



engine = create_engine('sqlite:///shoppers.db')


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String(), index=True)

    # Establish a many-to-many relationship with Product through Cart
    products = relationship('Product', secondary='carts', back_populates='customers')

    def __repr__(self):
        return f"Customer {self.id}: " \
            + f"{self.first_name}, " \
            + f"{self.last_name}, "

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    product_name = Column(String(), index=True)
    price = Column(Integer())
    product_serialNo = Column(Integer())

    # Establish a many-to-many relationship with Customer through Cart
    customers = relationship('Customer', secondary='carts', back_populates='products')

    def __repr__(self):
        return f"Product {self.id}: " \
            + f"{self.product_name}, " \
            + f"{self.price}, " \
            + f"{self.product_serialNo}, "

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer(), primary_key=True)
    product_id = Column(Integer(), ForeignKey('products.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    # Establish back references to Customer and Product
    customer = relationship('Customer', back_populates='products', viewonly=True)
    product = relationship('Product', back_populates='customers', viewonly=True)
    