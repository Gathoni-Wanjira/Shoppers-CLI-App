import click
from database.db import session
from cli import find_product_by_name , add_product_to_cart , remove_product_from_cart , calculate_cart_total
from sqlalchemy.orm.exc import NoResultFound
from model.models import Customer, Product, Cart

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


# Find a product by its name
@click.command()
@click.option('--product_name', prompt='Enter product name', help='Find a product by its name.')
def find_product_by_name(product_name):
    """
    Find a product by its name.
    """
    try:
        product = session.query(Product).filter(Product.product_name == product_name).one()
        click.echo(f"Found product: {product.product_name}, Price: ${product.price}")
    except NoResultFound:
        click.echo(f"Product {product_name} not found.")

# Add a product to the cart for a specific customer
@click.command()
@click.option('--customer_id', prompt='Enter customer ID', type=int, help='Customer ID for adding a product.')
@click.option('--product_id', prompt='Enter product ID', type=int, help='Product ID to add to the cart.')
def add_product_to_cart(customer_id, product_id):
    """
    Add a product to the cart for a specific customer.
    """
    cart = Cart(customer_id=customer_id, product_id=product_id)
    session.add(cart)
    session.commit()
    click.echo(f"Product {product_id} added to the cart for customer {customer_id}.")

# Remove a product from the cart for a specific customer
@click.command()
@click.option('--customer_id', prompt='Enter customer ID', type=int, help='Customer ID for removing a product.')
@click.option('--product_id', prompt='Enter product ID', type=int, help='Product ID to remove from the cart.')
def remove_product_from_cart(customer_id, product_id):
    """
    Remove a product from the cart for a specific customer.
    """
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
@click.command()
@click.option('--customer_id', prompt='Enter customer ID', type=int, help='Customer ID for calculating the total.')
def calculate_cart_total(customer_id):
    """
    Calculate the total price of products in a customer's cart.
    """
    cart_items = session.query(Cart).filter(Cart.customer_id == customer_id).all()
    total_price = 0

    for cart_item in cart_items:
        product = session.query(Product).filter(Product.id == cart_item.product_id).one()
        total_price += product.price

    click.echo(f"Total price of products in the cart for customer {customer_id}: ${total_price}")

