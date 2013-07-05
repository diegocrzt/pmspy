'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import Atributo
from initdb import db_session, init_db, shutdown_session

session = db_session()

def getAtributosTipo(tipoI=None):
    """
    Retorna un atributo por su tipo, recibe el id del tipo de item
    """
    init_db()
    res = session.query(Atributo).filter(Atributo.pertenece==tipoI).all()
    shutdown_session()
    return res

def getAtributoId(id=None):
    """
    Retorna un atributo por su id
    """
    init_db()
    res = session.query(Atributo).filter(Atributo.id==id).first()
    shutdown_session()
    return res

def getAtributoNombreTipo(nombre=None,tipo=None):
    """
    Retorna un atributo por su nombre y su tipo
    """
    if(nombre and tipo):
            init_db()
            res=session.query(Atributo).filter(Atributo.nombre==nombre).filter(Atributo.pertenece==tipo).first()
            shutdown_session()
            return res
        
        
def comprobarAtributo(nombre=None, tipo=None):
    """
    Valida si ya existe un tributo con ese nombre en ese tipo, recibe el nombre del atributo y el id del tipo
    """
    a=getAtributoNombreTipo(nombre, tipo)
    if a == None:
        return False
    else:
        return True

def crearAtributo(nom=None, td=None, ta=None):
    """
    Crea un Atributo, recibe el nombre de atributo, tipo de atributo y el id del tipo al que pertenece
    """
    init_db()
    att = Atributo(nombre=nom,tipoDato=td, pertenece=ta)
    session.add(att)
    session.commit()
    shutdown_session()
    
    
def editarAtributo(idat=None,nom=None, td=None, ta=None):
    """
    Edita un atributo existente, recibe el id y el nombre de atributo, el tipo de dato que contiene y el id del tipo de item al que pertenece
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
    Elimina un atributo, recibe el id del atributo a ser eliminado
    """
    if(idat):
        init_db()
        session.query(Atributo).filter(Atributo.id==idat).delete()
        session.commit()
        shutdown_session()
