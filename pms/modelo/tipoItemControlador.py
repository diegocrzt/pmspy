'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import TipoItem
from initdb import db_session, init_db
from atributoControlador import getAtributosTipo, eliminarAtributo
from sqlalchemy import or_

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

def getTiposItemPaginados(pagina=None,tam_pagina=None, faseid=None, filtro=None):
    """
    Devuelve una lista de proyectos de tamanio tam_pagina de la pagina pagina, la pagina empieza en 0
    """
    if faseid:
        if  filtro:
            query=getTiposItemFiltrados(filtro,faseid)
        else:
            query = session.query(TipoItem).filter(TipoItem.defase==faseid).order_by(TipoItem.id)
        if pagina and tam_pagina:
            query = query.offset(pagina*tam_pagina)
        return query.limit(tam_pagina)

def getTiposItemFiltrados(filtro=None,faseid=None):
    """Devuelve una lista de proyectos por nombre, estado, id, y cantFases
    """
    if (filtro and faseid):
        if(filtro.isdigit()):
            query=session.query(TipoItem).filter(TipoItem.defase==faseid).filter(or_(TipoItem.id==filtro, TipoItem.nombre.ilike("%"+filtro+"%"), TipoItem.comentario.ilike("%"+filtro+"%")))
        else:
            query=session.query(TipoItem).filter(TipoItem.defase==faseid).filter(TipoItem.nombre.ilike("%"+filtro+"%") | TipoItem.comentario.ilike("%"+filtro+"%"))
        return query
    
def main():
    query=getTiposItemPaginados(0,5,2)
    if query:
        print query.count()
        for q in query:
            print q.nombre
    else:
        print query
        
if __name__ == "__main__":  
    main()   
    

