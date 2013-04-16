'''
Created on 05/04/2013

@author: synchro
'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://postgres:postgres@localhost:5432/pms', echo=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()


def init_db():
    """
        Inicializa la base de datos
    """
    db_session.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    #metadata.create_all(bind=engine)

        
def shutdown_session(exception=None):
    """
        Cierra la sesion con la base de datos 
    """
    db_session.remove()
    