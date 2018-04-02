# Dependencies
# ----------------------------------
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float

# Create Dog and Cat Classes
# ----------------------------------
class Dog(Base):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    age = Column(Integer)

class Cat(Base):
    __tablename__ = 'cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    age = Column(Integer)

# Create a Specific Instance of the Dog and Cat classes
# ----------------------------------
dog = Dog(name='Fido', color='Brown', age=4)
cat = Cat(name="Hissy", color="Gray", age=7)

# Create Database Connection
# ----------------------------------
engine = create_engine('mysql://root:mypassword@data-bootcamp-rutgers.cn6jzamkgcqr.us-west-2.rds.amazonaws.com:3306/pets')
conn = engine.connect()

# Create a "Metadata" Layer That Abstracts our SQL Database
# ----------------------------------
Base.metadata.create_all(engine)

# Create a Session Object to Connect to DB
# ----------------------------------
from sqlalchemy.orm import Session
session = Session(bind=engine)

# Add Records to the Appropriate DB
# ----------------------------------
session.add(dog)
session.add(cat)
session.commit()

# Query the Tables
# ----------------------------------
dog_list = session.query(Dog)
for doggy in dog_list:
    print(doggy.name)

cat_list = session.query(Dog)
for kitty in cat_list:
    print(kitty.name)
