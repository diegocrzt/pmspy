'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import Atributo
from initdb import db_session, init_db

session = db_session()

def getAtributosTipo(tipoI=None):
    """Obtener tipos de items
    """
    init_db()
    res = session.query(Atributo).filter(Atributo.pertenece==tipoI).all()
    return res

def getAtributoId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    res = session.query(Atributo).filter(Atributo.id==id).first()
    return res

def getAtributoNombreTipo(nombre=None,tipo=None):
    """
    recupera un tipo por su nombre
    
    """
    if(nombre and tipo):
            res=session.query(Atributo).filter(Atributo.nombre==nombre).filter(Atributo.pertenece==tipo).first()
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
    session = db_session()
    att = Atributo(nombre=nom,TipoDato=td, pertenece=ta)
    session.add(att)
    session.commit()
    
    
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




def eliminarAtributo(idat=None):
    """
    elimina un tipo de item
    """
    if(idat):
        session.query(Atributo).filter(Atributo.id==idat).delete()
        session.commit()
