'''
Created on 14/04/2013

@author: mpoletti

'''
import flask.views
from flask import request
from entidad import TipoItem, Proyecto, Fase
from initdb import db_session, init_db, shutdown_session
from atributoControlador import getAtributosTipo, eliminarAtributo
from sqlalchemy import or_
from datetime import datetime

session = db_session()

def getTiposFase(fase=None):
    """Devuelve los tipos de item de una fase, recibe el id de la fase
    """
    init_db()
    res = session.query(TipoItem).filter(TipoItem.defase==fase).order_by(TipoItem.id)
    shutdown_session()
    return res

def getTipoItemId(id=None):
    """
    Devuelve un tipo de item por su id
    """
    init_db()
    tipoitem = session.query(TipoItem).filter(TipoItem.id==id).first()
    shutdown_session()
    return tipoitem

def getTipoItemNombre(nombre=None,fase=None):
    """
    Devuelve un tipo de item por su nombre, recibe el nombre y el id de la fase
    
    """
    if(nombre and fase):
        init_db()
        res=session.query(TipoItem).filter(TipoItem.nombre==nombre).filter(TipoItem.defase==fase).first()
        shutdown_session()
        return res
        
        
def comprobarTipoItem(nombre=None, fase=None):
    """
    Comprueba si ya existe un tipo de item con ese nombre en esa fase, recibe el nombre y el id de la fase
    """
    a=getTipoItemNombre(nombre,fase)
    if a == None:
        return False
    else:
        if flask.session['tipoitemid']!=a.id:
            return True

def crearTipoItem(nom=None, com=None, fa=None, usr=None):
    """Crea un tipo de item, recibe el nombre y el comentario del tipo de item y el id de la fase
    """
    init_db()
    fecha = datetime.today()
    titem = TipoItem(nombre=nom,comentario=com, defase=fa,fechaCreacion=fecha,fechaModificacion=fecha,usuarioCreador=usr)
    session.add(titem)
    session.commit()
    shutdown_session()
    
    
def editarTipoItem(idti=None,nom=None, com=None, fa=None, usr=None):
    """
    Edita un tipo de item, recibe el id, nombre y comentario del tipo de item y el id de la fase
    """
    init_db()
    f = getTipoItemId(idti)
    f.nombre=nom
    f.comentario=com
    f.defase=fa
    f.fechaModificiacion = datetime.today()
    f.usuario_modificador_id = usr
    session.merge(f)
    session.commit()
    shutdown_session()


def eliminarTipoItem(idti=None):
    """
    Elimina un tipo de item, recibe el id del tipo de item a eliminarse
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
    Devuelve una lista de tipos de item de una fase de tamanio "tam_pagina" de la pagina "pagina", 
    la pagina empieza en 0, recibe ademas el id de la fase y el filtro
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
    """Devuelve una lista de tipos de item de una fase filtrados, recibe el id de la fase y el filtro
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
    """Devuelve todos los tipos de items que existen
    """
    init_db()
    query=session.query(TipoItem)
    shutdown_session()
    return query 
    
def getAllTiposItemPaginados(pagina=None,tam_pagina=None, filtro=None):
    """Devuelve todos los tipos de items que existen paginados y opcionamente filtrados, recibe la pagina,
    el tamanio de la pagina y el filtro
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
    """Devuelve todos los tipos de items resultantes del filtro, recibe el valor por el cual se quiere filtrar
    """
    if(filtro):
        query=session.query(TipoItem).join(Fase).join(Proyecto).filter(TipoItem.nombre.ilike("%"+filtro+"%") | Proyecto.nombre.ilike("%"+filtro+"%") | Fase.nombre.ilike("%"+filtro+"%"))
        return query
