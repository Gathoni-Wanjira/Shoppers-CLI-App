from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.models import *

if __name__ == '__main__':

    engine = create_engine('sqlite:///shoppers.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    import pdb; pdb.set_trace()
