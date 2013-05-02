'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import Item, VersionItem
from initdb import db_session, init_db
from tipoItemControlador import getTiposFase
from atributoControlador import getAtributosTipo

session = db_session()

def getItemsTipo(tipo=None):
    """Obtener tipos de items
    """
    init_db()
    res = session.query(Item).filter(Item.tipo==tipo).all()
    return res

def getItemEtiqueta(etiqueta=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    item = session.query(Item).filter(Item.etiqueta==etiqueta).first()
    return item

def getItemId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    item = session.query(Item).filter(Item.id==id).first()
    return item

def getVersionItem(idi=None):
    init_db()
    version = session.query(VersionItem).filter(VersionItem.deitem==idi,VersionItem.actual==True).first()
    return version
        
        
def comprobarItem(nombre=None, fase=None, etiqueta=None):
    """
    valida si ya existe un item con ese nombre en esa fase
    """
    tipos=getTiposFase(fase)
    for t in tipos:
        for i in t.instancias:
            for v in i.version:
                if(v.actual==True and (v.nombre==nombre or i.etiqueta == etiqueta)):
                    return True
                else:
                    return False                
    

def crearItem(ti=None,etiq=None,nom=None, est=None):
    """Crea un tipo de item

    """
    init_db()
    session = db_session()
    itm = Item(tipo=ti, etiqueta=etiq)
    session.add(itm)
    session.commit()
    i=getItemEtiqueta(etiq)
    ver=VersionItem(nombre=nom,version=1,estado=est,actual=True,deitem=i.id)
    session.add(ver)
    session.commit()
    
def editarItem(idi=None,nom=None, est=None):
    """
    permite editar un tipo de item existente
    """
    init_db()
    v = getVersionItem(idi)
    v.actual=False
    session.merge(v)
    session.commit()
    ver=VersionItem(nombre=nom,version=(v.version+1),estado=est,actual=True,deitem=idi)
    session.add(ver)
    session.commit()



def eliminarItem(idi=None):
    """
    elimina un tipo de item
    """
    if(idi):
        init_db()
        v = getVersionItem(idi)
        v.actual=False
        session.merge(v)
        session.commit()
        ver=VersionItem(nombre=v.nombre,version=(v.version+1),estado="Eliminado",actual=True,item=idi)
        session.add(ver)
        session.commit()