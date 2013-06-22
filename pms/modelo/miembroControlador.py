'''
Created on 12/06/2013

@author: synchro
'''
from initdb import db_session, init_db, shutdown_session
from entidad import Miembro

session = db_session()

def eliminarMiembro(miembro=None):
    """
    funcion para eliminar un  miembro del comite de votacion
    """
    if(miembro):
        init_db()
        session.query(Miembro).filter(Miembro.proyecto_id==miembro.proyecto_id).delete()
        session.commit()
        shutdown_session()