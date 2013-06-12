'''
Created on 12/06/2013

@author: synchro
'''

from entidad import Peticion, Voto, Usuario, Item, VersionItem, Miembro
from initdb import db_session, init_db, shutdown_session
from pms.modelo.usuarioControlador import getUsuarios
from datetime import datetime
session = db_session()



def getPeticion(id=None):
    """
    Retorna una peticion, recibe el id de la peticion
    """
    init_db()
    res=session.query(Peticion).filter(Peticion.id==id).first()
    shutdown_session()
    return res


    
def eliminarPeticion(idp=None):
    """Elimina una Peticion, recibe el id de la peticion
    """
    init_db()
    u=getPeticion(idp)
    for l in u.items:
        quitarItem(l.id)
    for l in u.votos:
        quitarVoto(l.user_id,l.peticion_id)
    session.query(Peticion).filter(Peticion.id==u.id).delete()
    session.commit()
    shutdown_session()
    
def quitarItem(idv=None):
    """Quita un Item de una peticion, recibe el id del item
    """
    init_db()
    v=getVersionId(idv)
    v.peticion_id=None
    session.merge(v)
    session.commit()
    shutdown_session()


def quitarVoto(idu=None,idp=None):
    """Elimina un voto, recibe el id del usuario y el id de la peticion
    """
    soli=getPeticion(idp)
    soli.cantVotos=soli.cantVotos-1
    init_db()
    session.query(Voto).filter(Voto.peticion_id==idp).filter(Voto.user_id==idu).delete()
    session.merge(soli)
    session.commit()
    shutdown_session()
    
def getVersionId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    item = session.query(VersionItem).filter(VersionItem.id == id).first()
    shutdown_session()
    return item