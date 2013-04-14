'''
Created on 05/04/2013

@author: synchro
'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine('postgresql://postgres:postgres@localhost:5432/pms', echo=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def init_db():
    """
        Inicializa la base de datos
    """
    metadata.create_all(bind=engine)

        
def shutdown_session(exception=None):
    """
        Cierra la sesion con la base de datos 
    """
    db_session.remove()
    