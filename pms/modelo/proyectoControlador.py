'''
Created on 14/04/2013

@author: mpoletti
'''
from entidad import Proyecto
from initdb import db_session, init_db

session = db_session()

def getProyectos():
    """Obtener usuarios
    """ 
    init_db()
    proyectos = session.query(Proyecto).all()
    return proyectos