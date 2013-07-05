'''
Created on 14/05/2013

@author: Natalia Valdez
'''
from pms.modelo.entidad import LineaBase, Fase, Item
from datetime import datetime
from initdb import db_session, init_db, shutdown_session
from pms.modelo.itemControlador import getVersionId, getVersionItem
session = db_session()

def getLineaBaseId(lbid=None):
    """Devuelve una linea base, recibe el id de la linea base
    """
    if(id):
        init_db()
        query=session.query(LineaBase).filter(LineaBase.id==lbid).first()
        shutdown_session()
        return query
    
def getLineaBaseDeFase(faseid=None,numero=None):
    """Devuelve la linea base de una fase, recibe el id de la fase y el numero de linea base
    """
    if(faseid and numero):
        init_db()
        query=session.query(LineaBase).filter(LineaBase.fase_id==faseid).filter(LineaBase.numero==numero).first()
        shutdown_session()
        return query
    
def eliminarLB(idl=None):
    """Elimina la linea base, recibe el id de la linea base que se desea eliminar
    """
    if idl:
        linea=getLineaBaseId(idl)
        init_db()
        items=session.query(LineaBase).join(Item).filter(Item.linea_id==idl).count()
        if(items>0):
            for i in linea.items:
                i.linea_id=None
                v=getVersionItem(i.id)
                v.estado="Aprobado"
                session.merge(v)
                session.commit()
                session.merge(i)
                session.commit()
        session.delete(linea)
        session.commit()
        shutdown_session()

def crearLB(creadorid=None, comentario=None, faseid=None):
    """Crea una nueva linea base, recibe el id del creador de la lb, un comentario y el id de la fase
    """
    if(creadorid and faseid):
        init_db()
        fecha=datetime.today()
        n=session.query(LineaBase).join(Fase).filter(Fase.id==faseid).count()
        numero=n+1
        lb=LineaBase(creador_id=creadorid, fechaCreacion=fecha, numero=numero, fase_id=faseid, estado="Cerrada")
        session.add(lb)
        session.commit()
        linea=getLineaBaseDeFase(faseid, numero)
        return linea.id
        shutdown_session()
        
def aItemLB(idv=None, idlb=None):
    """Agrega un item a una linea base, recie el ide la de la version del item y el id de la linea base
    """
    if(idv and idlb):
        version=getVersionId(idv)
        init_db()
        item=version.item
        item.linea_id=idlb
        version.estado="Bloqueado"
        session.merge(version)
        session.commit()
        session.merge(item)
        session.commit()
        shutdown_session()
        return True
    return False
        
def quitarItemLB(idv=None):
    """Extrae un item de su linea base, recibe el id de la version del item
    """
    if(idv):
        version=getVersionId(idv)
        init_db()
        item=version.item
        item.linea_id=None
        version.estado="Aprobado"
        session.merge(version)
        session.merge(item)
        session.commit()
        shutdown_session()

def agregarComentarioLB(idlb=None, comentario=None):
    """Agrega el comentatio a la linea base, recibe el id de la linea base y el comentario
    """
    if(idlb and comentario):
        linea=getLineaBaseId(idlb)  
        linea.comentario=comentario
        init_db()
        session.merge(linea)
        session.commit()
        shutdown_session()
        
def comprobarBloquear(version=None):
    """Comprueba que un item pueda ser bloqueado, recibe el id de la version del item
    """
    anteriores=version.ante_list
    bandera=False
    for a in anteriores:
        ant=getVersionId(a.ante_id)
        if ant.estado!="Bloqueado" and ant.estado!="Eliminado" and ant.actual:
            return False
        if ant.estado=="Bloqueado" and ant.actual:
            bandera=True
    fase=version.item.tipoitem.fase
    if fase.numero>1 and bandera==False:
        return False
    return True    

def desBloquearAdelante(idvcambio=None):
    """Desbloquea el item y sus hijos, recibe el ide de la version del item a desbloquearse
    """
    ver=getVersionId(idvcambio)
    lista=[]
    lista.append(ver)
    for l in lista:
        ante=l.post_list
        for a in ante:
            lista.append(getVersionId(a.post_id))
        quitarItemLB(l.id)

def bloquearItem(idv=None):
    """Bloquea un item, recibe el id de la version del item
    """
    if(idv):
        version=getVersionId(idv)
        init_db()
        version.estado="Bloqueado"
        session.merge(version)
        session.commit()
        shutdown_session()
        return True
    return False

def cerrarLB(linea):
    """
    Establece el estado de la linea base a "Cerrada"
    """
    if linea:
        init_db()
        linea.estado="Cerrada"
        session.merge(linea)
        session.commit()
        shutdown_session()
    