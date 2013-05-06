'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import Item, VersionItem, Atributo, ValorStr, ValorNum, ValorBoolean, ValorDate
from initdb import db_session, init_db
from tipoItemControlador import getTiposFase
from atributoControlador import getAtributosTipo, getAtributoId
from datetime import timedelta
from datetime import datetime


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

def getVersionId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    item = session.query(VersionItem).filter(VersionItem.id==id).first()
    return item

def getVersionItem(idi=None):
    init_db()
    version = session.query(VersionItem).filter(VersionItem.deitem==idi).filter(VersionItem.actual==True).first()
    return version
        
        
def comprobarItem(nombre=None, fase=None):
    """
    valida si ya existe un item con ese nombre en esa fase
    """
    tipos=getTiposFase(fase)
    for t in tipos:
        for i in t.instancias:
            for v in i.version:
                if(v.actual==True and (v.nombre==nombre)):
                    return True
                else:
                    return False                
    

def crearItem(ti=None,etiq=None,nom=None, est=None, cos=None, dif=None):
    """Crea un tipo de item

    """
    init_db()
    session = db_session()
    itm = Item(tipo=ti, etiqueta=etiq)
    session.add(itm)
    session.commit()
    i=getItemEtiqueta(etiq)
    ver=VersionItem(nombre=nom,version=0,estado=est,actual=True, costo=cos, dificultad=dif,deitem=i.id)
    session.add(ver)
    session.commit()
    
def editarItem(idi=None,nom=None, est=None, cos=None, dif=None):
    """
    permite editar un tipo de item existente
    """
    init_db()
    v = getVersionItem(idi)
    v.actual=False
    session.merge(v)
    session.commit()
    if nom== None:
        nom=v.nombre
    if cos== None:
        cos=v.costo
    if est== None:
        est=v.estado
    if dif== None:
        dif=v.dificultad
    ver=VersionItem(nombre=nom,version=(v.version+1),estado=est,actual=True,costo=cos, dificultad=dif,deitem=idi)
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
        ver=VersionItem(nombre=v.nombre,version=(v.version+1),estado="Eliminado",actual=True, costo=v.costo, dificultad = v.dificultad,deitem=idi)
        session.add(ver)
        session.commit()
        
def crearValor(ida=None,idv=None,val=None):
    atr=getAtributoId(ida)
    if atr.tipoDato =="Cadena":
        if val== None:
            val=""
        v= ValorStr(atributo=ida,item=idv,valor=val)
        session.add(v)
        session.commit()
    elif atr.tipoDato =="Numerico":
        if val== None:
            val=0
        v= ValorNum(atributo=ida,item=idv,valor=val)
        session.add(v)
        session.commit()
    elif atr.tipoDato =="Fecha":
        if val== None:
            val=datetime.today()
        v= ValorDate(atributo=ida,item=idv,valor=val)
        session.add(v)
        session.commit()
    elif atr.tipoDato =="Booleano":
        if val== None:
            val=False
        v= ValorBoolean(atributo=ida,item=idv,valor=val)
        session.add(v)
        session.commit()
        
def copiarValores(idvante=None,idvnueva=None):
    version=getVersionId(idvante)
    for at in version.atributosnum:
        crearValor(at.atributo_id,idvnueva,at.valor)
    for at in version.atributosstr:
        crearValor(at.atributo_id,idvnueva,at.valor)
    for at in version.atributosbool:
        crearValor(at.atributo_id,idvnueva,at.valor)
    for at in version.atributosdate:
        crearValor(at.atributo_id,idvnueva,at.valor)
    