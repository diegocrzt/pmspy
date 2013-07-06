'''
Created on 14/04/2013

@author: mpoletti

'''
import flask.views
from flask import request
from entidad import TipoItem, Item, VersionItem, ValorStr, ValorNum, ValorBoolean, ValorDate, Peticion
from initdb import db_session, init_db, shutdown_session
from tipoItemControlador import getTiposFase, getTipoItemId
from atributoControlador import getAtributoId
from faseControlador import getFaseId
from datetime import datetime
from sqlalchemy import or_
from pms.modelo.entidad import LineaBase

session = db_session()

def getItemsTipo(tipo=None):
    """Obtener tipos de items
    """
    init_db()
    res = session.query(Item).filter(Item.tipo == tipo).all()
    shutdown_session()
    return res

def getItemVerNum(id=None,v=None):
    """Obtener una version de un item
    """
    init_db()
    version = session.query(VersionItem).filter(VersionItem.deitem == id).filter(VersionItem.version == v).first()
    shutdown_session()
    return version

def getItemEtiqueta(etiqueta=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    item = session.query(Item).filter(Item.etiqueta == etiqueta).first()
    shutdown_session()
    return item

def getItemId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    item = session.query(Item).filter(Item.id == id).first()
    shutdown_session()
    return item

def getVersionId(id=None):
    """
        Recuera la version de un item a partir de su id
        @param id: Identificador de la un objeto VersionItem 
    
    """
    init_db()
    item = session.query(VersionItem).filter(VersionItem.id == id).first()
    shutdown_session()
    return item

def getVersionItem(idi=None):
    init_db()
    version = session.query(VersionItem).filter(VersionItem.deitem == idi).filter(VersionItem.actual == True).first()
    shutdown_session()
    return version
        
        
def comprobarItem(nombre=None, fase=None):
    """
    valida si ya existe un item con ese nombre en esa fase
    """
    tipos = getTiposFase(fase)
    for t in tipos:
        for i in t.instancias:
            for v in i.version:
                if(v.actual == True and (v.nombre == nombre) and getVersionItem(flask.session['itemid']).id != v.id):
                    return True
                else:
                    return False                
    

def crearItem(ti=None, etiq=None, nom=None, est=None, cos=None, dif=None, usr=None):
    """Crea un tipo de item

    """
    init_db()
    fecha_creacion = datetime.today()
    itm = Item(tipo=ti, etiqueta=etiq, fechaCreacion=fecha_creacion, usuario_creador_id=usr)
    session.add(itm)
    session.commit()
    i = getItemEtiqueta(etiq)
    ver = VersionItem(nombre=nom, version=0, estado=est, actual=True, costo=cos, dificultad=dif, fechaModificacion=fecha_creacion, deitem=i.id, usuario_modificador_id=usr)
    session.add(ver)
    session.commit()
    shutdown_session()
    
def editarItem(idi=None, nom=None, est=None, cos=None, dif=None, usr=None):
    """
    permite editar un tipo de item existente
    """
    init_db()
    v = getVersionItem(idi)
    v.actual = False
    session.merge(v)
    session.commit()
    if nom == None:
        nom = v.nombre
    if cos == None:
        cos = v.costo
    if est == None:
        est = v.estado
    if dif == None:
        dif = v.dificultad
    ver = VersionItem(nombre=nom, version=(v.version + 1), estado=est, actual=True, costo=cos, dificultad=dif, fechaModificacion=datetime.today(), deitem=idi, usuario_modificador_id=usr)
    session.add(ver)
    session.commit()
    shutdown_session()



def eliminarItem(idi=None, usr=None):
    """
    Elimina un item
    """
    if(idi):
        init_db()
        fecha_mod = datetime.today()
        v = getVersionItem(idi)
        v.actual = False
        session.merge(v)
        session.commit()
        ver = VersionItem(nombre=v.nombre, version=(v.version + 1), estado="Eliminado", actual=True, costo=v.costo, dificultad=v.dificultad, fechaModificacion=fecha_mod, deitem=idi, usuario_modificador_id=usr)
        session.add(ver)
        session.commit()
        shutdown_session()
        
def ejEliminarItem(idi=None):
    """
    Elimina un item, recibe su id
    """
    init_db()
    v = getVersionId(idi)
    v.estado="Eliminado"
    session.merge(v)
    session.commit()
    shutdown_session()
        
def crearValor(ida=None, idv=None, val=None):
    """
    Crea un atributo nuevo
    """
    atr = getAtributoId(ida)
    if atr.tipoDato == "Cadena":
        if val == None:
            val = ""
        v = ValorStr(atributo=ida, item=idv, valor=val)
        session.add(v)
        session.commit()
    elif atr.tipoDato == "Numerico":
        if val == None:
            val = 0
        v = ValorNum(atributo=ida, item=idv, valor=val)
        session.add(v)
        session.commit()
    elif atr.tipoDato == "Fecha":
        try:
            val = datetime.strptime(val,'%Y-%m-%d')
        except:
            val = None
        v = ValorDate(atributo=ida, item=idv, valor=val)
        session.add(v)
        session.commit()
    elif atr.tipoDato == "Booleano":
        if val == None:
            val = False
        v = ValorBoolean(atributo=ida, item=idv, valor=val)
        session.add(v)
        session.commit()
        
def copiarValores(idvante=None, idvnueva=None):
    """
    Copia los valores a una nueva version del item, recibe las dos versiones
    """
    version = getVersionId(idvante)
    for at in version.atributosnum:
        crearValor(at.atributo_id, idvnueva, at.valor)
    for at in version.atributosstr:
        crearValor(at.atributo_id, idvnueva, at.valor)
    for at in version.atributosbool:
        crearValor(at.atributo_id, idvnueva, at.valor)
    for at in version.atributosdate:
        crearValor(at.atributo_id, idvnueva, at.valor)
        


def getItemsPaginados(pagina=None, tam_pagina=None, fase=None, fil=None):
    """
    Retorna los items paginados, recibe la pagina, el tamanio de la pagina, la fase y el filtro de busqueda
    """
    i = []
    if fil:
        items = getItemsFiltrados(fase, fil)
        offset = pagina * tam_pagina
        c = 0
        of = 0
        for it in items:
            if it.estado != "Eliminado":
                of = of + 1
                if c == tam_pagina:
                    return i
                if of > offset:
                    i.append(it)
                    c = c + 1
    else:
        t = fase.tipos
        i = []
        offset = pagina * tam_pagina
        c = 0
        of = 0
        for ti in t:
            itms = ti.instancias
            for it in itms:
                aux = getVersionItem(it.id)
                if aux.estado != "Eliminado":
                    of = of + 1
                    if c == tam_pagina:
                        return i
                    if of > offset:
                        i.append(aux)
                        c = c + 1
    return i
def getItemsFiltrados(fase=None, filtro=None):
    """
    Retorna los items de una fase filtrados por un filtro
    """
    if fase and filtro:
        r = []
        if filtro.isdigit():
            query = session.query(Item).join(VersionItem).filter(VersionItem.actual == True).filter(or_(VersionItem.costo == filtro, VersionItem.dificultad == filtro, VersionItem.nombre.ilike("%" + filtro + "%")))
        
        else:
            query = session.query(Item).join(VersionItem).filter(VersionItem.actual == True).filter(VersionItem.nombre.ilike("%" + filtro + "%") | VersionItem.estado.ilike("%" + filtro + "%"))
        for q in query:
            t = getTipoItemId(q.tipo)
            if t.defase == fase.id:
                r.append(getVersionItem(q.id))
        tipos = session.query(TipoItem).filter(TipoItem.defase == fase.id).filter(TipoItem.nombre.ilike("%" + filtro + "%"))
        for t in tipos:
            for i in t.instancias:
                r.append(getVersionItem(i.id))
        return r
    
def getVitemTest(nombre=None):
    """
        Retorna La primera ocurrencia de version del item dado el nombre del item
        @param nombre: Nombre del item
        Funcion Helper 
    """
    if nombre:
        respuesta = session.query(VersionItem).filter(VersionItem.nombre == nombre).first()
        return respuesta
    
def dropItemTest(vitem):
    if vitem:
        init_db()
        verItem = session.query(VersionItem).filter(VersionItem.id == vitem).first()
        elitem = verItem.deitem
        lbase = verItem.item.lineabase
        while session.query(VersionItem).filter(VersionItem.deitem == elitem).first() != None:
            session.query(VersionItem).filter(VersionItem.deitem == elitem).delete()
        session.commit
        
        if lbase:
            session.query(LineaBase).filter(LineaBase.id == lbase.id).delete()
            session.commit

        session.query(Item).filter(Item.id == elitem).delete()
        session.commit
        shutdown_session
    


if __name__ == '__main__':
    fase = getFaseId(1)
    query = getItemsFiltrados(fase, "1")
    for q in query:
        print q.nombre + " tipo:" + str(q.item.tipo)