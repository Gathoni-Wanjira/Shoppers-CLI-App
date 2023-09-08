from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Define the association table for the many-to-many relationship between Customer and Product
customer_product_association = Table(
    'customer_product_association',
    Base.metadata,
    Column('customer_id', Integer, ForeignKey('customers.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

# Define the association table for the many-to-many relationship between Product and Cart
product_cart_association = Table(
    'product_cart_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('cart_id', Integer, ForeignKey('carts.id'))
)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String(), index=True)

    # Define the many-to-many relationship with Product through the association table
    products = relationship('Product', secondary=customer_product_association, back_populates='customers')

    def __repr__(self):
        return f"Customer {self.id}: {self.first_name}, {self.last_name}"

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(), primary_key=True)
    product_name = Column(String(), index=True)
    price = Column(Integer())
    product_serialNo = Column(Integer())

    # Define the many-to-many relationship with Customer through the association table
    customers = relationship('Customer', secondary=customer_product_association, back_populates='products')

    # Define the many-to-many relationship with Cart through the association table
    carts = relationship('Cart', secondary=product_cart_association, back_populates='products')

    def __repr__(self):
        return f"Product {self.id}: {self.product_name}, {self.price}, {self.product_serialNo}"

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer(), primary_key=True)

    # Define the many-to-many relationship with Product through the association table
    products = relationship('Product', secondary=product_cart_association, back_populates='carts')

    def __repr__(self):
        return f"Cart {self.id}"
