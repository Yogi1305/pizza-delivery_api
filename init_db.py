from database import Base,engine
from model import User,Order    
Base.metadata.create_all(bind=engine)