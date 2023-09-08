from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

engine = create_engine("sqlite:///shoppers.db")
Session = sessionmaker(bind=engine)
session = Session()

from model.models import Customer, Product, Cart

if __name__ == "__main__":
    session = Session()

    session.query(Customer).delete()
    session.query(Product).delete()
    session.query(Cart).delete()

    fake = Faker()

    customers = []
    for i in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )

        # add and commit individually to get IDs back
        session.add(Customer)
        session.commit()

        customers.append(customer)

    
    products = ['chair', 'stool', 'table', 'mug', 'cup', 'desk lamp', 'floor lamp', ' desk', 'shelf', 'sofa', 'tea cup', 'tea pot', 'cutlery', 'chess set', 'lounge', ' alarm clock', 'phone dock', 'keyboard', 'side table', 'wallet', 'vase', 'dog bed', 'bird house', 'wine holder', 'skateboard', 'calculator', 'coathanger', 'salt & pepper shaker', 'coasters', "piggy bank", "headphones", "sculpture", "telephone", "flashlight", "mail sorter", "playing cards", "fan", "jewelry box", "mouse", "lantern", "walking cane", "sword", "wall clock", "mirror", "bed", "crib", "hammock", "plate", "bowl", "coffee mug", "espresso cup", "glasses", "fork", "spoon", "knife", "serving tray", "toy train", "action figure", "lamp shade", "cutting board", "dresser", "shoe rack", "rocking chair", "usb key", "8 ball", "frying pan", "drawer handle", "doorknob", "cable organizer", "planter pot", "coat hanger", "bottle opener", "can opener", "coasters", "pocket knife", "surfboard", "shoes", "book", "calendar", "house numbers", "spice rack", "suitcase", "button", "ring", "baking tray", "tape dispenser", "flower pot", "canoe", "basket", "pillow", "rug", "wall tile", "road bike", "bike seat", "handlebars"]
    for i in range(10):
        product = Product(
            product_name=random.randrange(products),
            price=fake.randint(100, 1000),
            product_serialNo=fake.ean(length=13)
        )

        # add and commit individually to get IDs back
        session.add(product)
        session.commit()

        products.append(product)
        

    carts = []
    for i in range(10):
        cart = Cart(
            name=fake.unique.name(),
            product_id=random.randint(1, 100),
            customer_id=random.randint(1, 50),
        )

        carts.append(cart)

    session.bulk_save_objects(carts)
    session.commit()
    session.close()
