'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import TipoItem, Proyecto, Fase
from initdb import db_session, init_db, shutdown_session
from atributoControlador import getAtributosTipo, eliminarAtributo
from sqlalchemy import or_

session = db_session()

def getTiposFase(fase=None):
    """Obtener tipos de items
    """
    init_db()
    res = session.query(TipoItem).filter(TipoItem.defase==fase).order_by(TipoItem.id)
    shutdown_session()
    return res

def getTipoItemId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    tipoitem = session.query(TipoItem).filter(TipoItem.id==id).first()
    shutdown_session()
    return tipoitem

def getTipoItemNombre(nombre=None,fase=None):
    """
    recupera un tipo por su nombre
    
    """
    if(nombre and fase):
        init_db()
        res=session.query(TipoItem).filter(TipoItem.nombre==nombre).filter(TipoItem.defase==fase).first()
        shutdown_session()
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
    titem = TipoItem(nombre=nom,comentario=com, defase=fa)
    session.add(titem)
    session.commit()
    shutdown_session()
    
    
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
    shutdown_session()




def eliminarTipoItem(idti=None):
    """
    elimina un tipo de item
    """
    if(idti):
        init_db()
        at = getAtributosTipo(idti)        
        for a in at:
            eliminarAtributo(a.id)
        session.query(TipoItem).filter(TipoItem.id==idti).delete()
        session.commit()
        shutdown_session()

def getTiposItemPaginados(pagina=None,tam_pagina=None, faseid=None, filtro=None):
    """
    Devuelve una lista de proyectos de tamanio tam_pagina de la pagina pagina, la pagina empieza en 0
    """
    if faseid:
        init_db()
        if  filtro:
            query=getTiposItemFiltrados(filtro,faseid)
        else:
            query = session.query(TipoItem).filter(TipoItem.defase==faseid).order_by(TipoItem.id)
        if pagina and tam_pagina:
            query = query.offset(pagina*tam_pagina)
        shutdown_session()
        return query.limit(tam_pagina)

def getTiposItemFiltrados(filtro=None,faseid=None):
    """Devuelve una lista de proyectos por nombre, estado, id, y cantFases
    """
    if (filtro and faseid):
        init_db()
        if(filtro.isdigit()):
            
            query=session.query(TipoItem).filter(TipoItem.defase==faseid).filter(or_(TipoItem.id==filtro, TipoItem.nombre.ilike("%"+filtro+"%"), TipoItem.comentario.ilike("%"+filtro+"%")))
        else:
            query=session.query(TipoItem).filter(TipoItem.defase==faseid).filter(TipoItem.nombre.ilike("%"+filtro+"%") | TipoItem.comentario.ilike("%"+filtro+"%"))
        shutdown_session()
        return query
    
def getAllTiposItem():
    init_db()
    query=session.query(TipoItem)
    shutdown_session()
    return query 
    
def getAllTiposItemPaginados(pagina=None,tam_pagina=None, filtro=None):
    """Devuelve todos los tipos de items que existen
    """
    init_db()
    query=session.query(TipoItem).join(Fase).join(Proyecto).order_by(Proyecto.nombre)
    if(filtro):
        query=getAllTipoFiltrados(filtro)
    if pagina and tam_pagina:
        query = query.offset(pagina*tam_pagina)
    shutdown_session()
    return query.limit(tam_pagina)

def getAllTipoFiltrados(filtro=None):
    if(filtro):
        query=session.query(TipoItem).join(Fase).join(Proyecto).filter(TipoItem.nombre.ilike("%"+filtro+"%") | Proyecto.nombre.ilike("%"+filtro+"%") | Fase.nombre.ilike("%"+filtro+"%"))
        return query
