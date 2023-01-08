from sqlalchemy import create_engine

# student needs to add
from models import Dog

engine = create_engine('sqlite:///:memory:')

def create_table(base):
    # contains function "create_table()" that 
    # takes a declarative_base,
    # test invokes like this: engine = create_table(Base)

    # creates table "dogs" if it does not exist,
    # https://docs.sqlalchemy.org/en/14/orm/quickstart.html#emit-create-table-ddl
    #  https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.MetaData.create_all
    # from documentation: 
    # method sqlalchemy.schema.MetaData.create_all(bind=None, tables=None, checkfirst=True) 
    # from solution: 
    base.metadata.create_all(engine)
    # and returns the engine.
    return engine

def save(session, dog):
    session.add(dog)
    session.commit()
    return session

def new_from_db(session, row):
    # contains function "new_from_db()" that takes a database row 
    # need to pass in the row
    # and returns a Dog instance.
    # so just selecting that dog from the db
    return session.query(Dog).filter_by(id = row.id).first()

def get_all(session):
    return [dog for dog in session.query(Dog)]

def find_by_name(session, name):
    # how does name = name work? does it know the difference?
    return session.query(Dog).filter_by(name = name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id = id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name = name, breed = breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed 
    session.commit()
    return session