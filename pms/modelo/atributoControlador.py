'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import Atributo
from initdb import db_session, init_db, shutdown_session

session = db_session()

def getAtributosTipo(tipoI=None):
    """Obtener tipos de items
    """
    init_db()
    res = session.query(Atributo).filter(Atributo.pertenece==tipoI).all()
    shutdown_session()
    return res

def getAtributoId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    res = session.query(Atributo).filter(Atributo.id==id).first()
    shutdown_session()
    return res

def getAtributoNombreTipo(nombre=None,tipo=None):
    """
    recupera un tipo por su nombre
    
    """
    if(nombre and tipo):
            init_db()
            res=session.query(Atributo).filter(Atributo.nombre==nombre).filter(Atributo.pertenece==tipo).first()
            shutdown_session()
            return res
        
        
def comprobarAtributo(nombre=None, tipo=None):
    """
    valida si ya existe un item con ese nombre en esa fase
    """
    a=getAtributoNombreTipo(nombre, tipo)
    if a == None:
        return False
    else:
        return True

def crearAtributo(nom=None, td=None, ta=None):
    """Crea un tipo de item

    """
    init_db()
    att = Atributo(nombre=nom,tipoDato=td, pertenece=ta)
    session.add(att)
    session.commit()
    shutdown_session()
    
    
def editarAtributo(idat=None,nom=None, td=None, ta=None):
    """
    permite editar un tipo de item existente
    """
    init_db()
    at = getAtributoId(idat)
    at.nombre=nom
    at.tipoDato=td
    at.pertenece=ta
    session.merge(at)
    session.commit()
    shutdown_session()




def eliminarAtributo(idat=None):
    """
    elimina un tipo de item
    """
    if(idat):
        init_db()
        session.query(Atributo).filter(Atributo.id==idat).delete()
        session.commit()
        shutdown_session()
