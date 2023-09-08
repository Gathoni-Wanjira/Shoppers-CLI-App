import click
from database.db import session
from sqlalchemy.orm.exc import NoResultFound
from model.models import Customer, Product, Cart

# Find a product by its name
def find_product_by_name():
    product_name = click.prompt("Enter product name")
    try:
        product = session.query(Product).filter(Product.product_name == product_name).one()
        click.echo(f"Found product: {product.product_name}, Price: ${product.price}")
    except NoResultFound:
        click.echo(f"Product {product_name} not found.")

# Add a product to the cart for a specific customer
def add_product_to_cart():
    customer_id = click.prompt("Enter customer ID", type=int)
    product_id = click.prompt("Enter product ID", type=int)
    
    cart = Cart(customer_id=customer_id, product_id=product_id)
    session.add(cart)
    session.commit()
    click.echo(f"Product {product_id} added to the cart for customer {customer_id}.")

# Remove a product from the cart for a specific customer
def remove_product_from_cart():
    customer_id = click.prompt("Enter customer ID", type=int)
    product_id = click.prompt("Enter product ID", type=int)
    
    cart = session.query(Cart).filter(
        Cart.customer_id == customer_id,
        Cart.product_id == product_id
    ).first()

    if cart:
        session.delete(cart)
        session.commit()
        click.echo(f"Product {product_id} removed from the cart for customer {customer_id}.")
    else:
        click.echo(f"Product {product_id} not found in the cart for customer {customer_id}.")

# Calculate the total price of products in a customer's cart
def calculate_cart_total():
    customer_id = click.prompt("Enter customer ID", type=int)
    
    cart_items = session.query(Cart).filter(Cart.customer_id == customer_id).all()
    total_price = 0

    for cart_item in cart_items:
        product = session.query(Product).filter(Product.id == cart_item.product_id).one()
        total_price += product.price

    click.echo(f"Total price of products in the cart for customer {customer_id}: ${total_price}")

# Create a Click group and add the functions
@click.group()
def cli():
    pass

cli.add_command(find_product_by_name)
cli.add_command(add_product_to_cart)
cli.add_command(remove_product_from_cart)
cli.add_command(calculate_cart_total)

if __name__ == "__main__":
    cli()

