from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from models import *

connection_url = "postgresql://admin:1234@172.20.145.1:5437/missions_db"
engine = create_engine(connection_url, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
    import models
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind=engine)


