from database.db import session
from sqlalchemy.orm.exc import NoResultFound
from model.models import Customer, Product, Cart

from sqlalchemy.orm.exc import NoResultFound

# Find a product by its name
def find_product_by_name(product_name):
    try:
        product = session.query(Product).filter(Product.product_name == product_name).one()
        return product
    except NoResultFound:
        return None

# Add a product to the cart for a specific customer
def add_product_to_cart(customer_id, product_id):
    cart = Cart(customer_id=customer_id, product_id=product_id)
    session.add(cart)
    session.commit()

# Remove a product from the cart for a specific customer
def remove_product_from_cart(customer_id, product_id):
    cart = session.query(Cart).filter(
        Cart.customer_id == customer_id,
        Cart.product_id == product_id
    ).first()

    if cart:
        session.delete(cart)
        session.commit()

# Calculate the total price of products in a customer's cart
def calculate_cart_total(customer_id):
    cart_items = session.query(Cart).filter(Cart.customer_id == customer_id).all()
    total_price = 0

    for cart_item in cart_items:
        product = session.query(Product).filter(Product.id == cart_item.product_id).one()
        total_price += product.price

    return total_price

if __name__ == "__main__":
    # Example usage of the methods
    product_name_to_find = "chair"
    customer_id = 1  # Replace with the desired customer ID
    product_id_to_add = 1  # Replace with the desired product ID to add
    product_id_to_remove = 2  # Replace with the desired product ID to remove

    found_product = find_product_by_name(session, product_name_to_find)
    if found_product:
        print(f"Found product: {found_product.product_name}, Price: ${found_product.price}")
    else:
        print(f"Product {product_name_to_find} not found.")

    add_product_to_cart(session, customer_id, product_id_to_add)
    print(f"Product {product_id_to_add} added to the cart for customer {customer_id}.")

    remove_product_from_cart(session, customer_id, product_id_to_remove)
    print(f"Product {product_id_to_remove} removed from the cart for customer {customer_id}.")

    cart_total = calculate_cart_total(session, customer_id)
    print(f"Total price of products in the cart for customer {customer_id}: ${cart_total}")


