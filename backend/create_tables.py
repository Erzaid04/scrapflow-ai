from app.database.connection import engine
from app.models.base import Base
#import models so SQL ALchemy can discover them
from app.models.user import User
from app.models.inventory import Inventory
from app.models.transaction import Transaction
print("creating tables...")
Base.metadata.create_all(bind= engine)
print("Tables created successfully")
