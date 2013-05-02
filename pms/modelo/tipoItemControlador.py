'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import TipoItem
from initdb import db_session, init_db
from atributoControlador import getAtributosTipo, eliminarAtributo

session = db_session()

def getTiposFase(fase=None):
    """Obtener tipos de items
    """
    init_db()
    res = session.query(TipoItem).filter(TipoItem.defase==fase).order_by(TipoItem.id)
    return res

def getTipoItemId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    tipoitem = session.query(TipoItem).filter(TipoItem.id==id).first()
    return tipoitem

def getTipoItemNombre(nombre=None,fase=None):
    """
    recupera un tipo por su nombre
    
    """
    if(nombre and fase):
            res=session.query(TipoItem).filter(TipoItem.nombre==nombre).filter(TipoItem.defase==fase).first()
            return res
        
        
def comprobarTipoItem(nombre=None, fase=None):
    """
    valida si ya existe un item con ese nombre en esa fase
    """
    a=getTipoItemNombre(nombre,fase)
    if a == None:
        return False
    else:
        return True

def crearTipoItem(nom=None, com=None, fa=None):
    """Crea un tipo de item

    """
    init_db()
    session = db_session()
    titem = TipoItem(nombre=nom,comentario=com, defase=fa)
    session.add(titem)
    session.commit()
    
    
def editarTipoItem(idti=None,nom=None, com=None, fa=None):
    """
    permite editar un tipo de item existente
    """
    init_db()
    f = getTipoItemId(idti)
    f.nombre=nom
    f.comentario=com
    f.defase=fa
    session.merge(f)
    session.commit()




def eliminarTipoItem(idti=None):
    """
    elimina un tipo de item
    """
    if(idti):
        at = getAtributosTipo(idti)        
        for a in at:
            eliminarAtributo(a.id)
        session.query(TipoItem).filter(TipoItem.id==idti).delete()
        session.commit()
