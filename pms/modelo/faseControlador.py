'''
Created on 18/04/2013

@author: Natalia Valdez
'''

from initdb import db_session, init_db, shutdown_session
from entidad import Fase
from datetime import timedelta
from datetime import datetime
from entidad import Rol, User_Rol

session = db_session()

def getFases(p=None):
    """Devuelve todas las fases de un proyecto, recibe el id del proyecto del que se quiere obtener las fases
    """
    init_db()
    fases = session.query(Fase).filter(Fase.delproyecto==p).order_by(Fase.numero)
    shutdown_session()
    return fases


def crearFase(nom=None, num=None, fechainicio=None, fechafin=None, fechamod=None, estado=None, proy=None):
    """ Crea una fase nueva, recibe los atributos necesarios para su creacion, nombre, numero, fecha de inicio, 
        fecha de fin, fecha de ultima modificacion, estado, proyecto al que pernece
    """
    init_db()
    fa = Fase(nombre=nom,numero=num, fechaInicio=fechainicio, fechaFin=fechafin,fechaUltMod=fechamod, estado="Abierta", delproyecto=proy)
    session.add(fa)
    session.commit()
    fa.proyecto.cantFase=fa.proyecto.cantFase+1
    session.merge(fa.proyecto)
    session.commit()
    shutdown_session()
   
def getFase(numero=None, proy=None):
    """Devuelve una fase por su numero y el id del proyecto al que pertenece
    """
    if(numero and proy):
        init_db()
        res=session.query(Fase).filter(Fase.numero==numero).filter(Fase.delproyecto==proy).first()
        shutdown_session()
        return res

def comprobarFase(numero=None, proy=None):
    """
    Comprueba si una fase ya existe, recibe el numero de la fase y el id del proyecto
    """
    a=getFase(numero, proy)
    if a == None:
        return False
    else:
        return True
   
def eliminarFase(fase=None):
    """
    Elimina una fase, recibe el id de la fase a eliminarse
    """
    if(fase):
        
        fa=getFaseId(fase)
        fa.proyecto.cantFase=fa.proyecto.cantFase-1
        for r in fa.roles:
            session.query(User_Rol).filter(User_Rol.rol_id==r.id).delete()
            session.query(Rol).filter(Rol.id==r.id).delete()
        init_db()
        session.query(Fase).filter(Fase.id==fase).delete()
        session.commit()
        shutdown_session()
        
       
def getFaseId(id=None):
    """
    Devuelve una fase por su id
    """
    if(id):
        init_db()
        res=session.query(Fase).filter(Fase.id==id).first()
        shutdown_session()
        return res      
         
def editarFase(id=None,nom=None, numero=None, fechaini=None, fechafin=None):
    """
    Edita una fase existente, recibe el id, nombre, numero, fecha de inicio, fecha de fin de la fase
    """
    init_db()
    f = getFaseId(id)
    f.nombre=nom
    f.numero= numero
    f.fechaInicio=fechaini
    f.fechaFin=fechafin
    session.merge(f)
    session.commit()
    shutdown_session()
    
def getFasesPaginadas(pagina=None,tam_pagina=None, p=None):
    """
    Devuelve una lista de fases de tamanio tam_pagina de la pagina pagina, la pagina empieza en 0
    """
    init_db()
    query = session.query(Fase).filter(Fase.delproyecto==p).order_by(Fase.id)
    if pagina and tam_pagina:
        query = query.offset(pagina*tam_pagina)
    shutdown_session()
    return query.limit(tam_pagina)

def controlCerrarFase(idf=None):
    """Verifica que una fase se pueda cerrar, osea que todos sus items se encuentren en una linea base(bloqueados), recibe el id de la fase
    """
    f = getFaseId(idf)
    cont=0
    for t in f.tipos:
        for i in t.instancias:
            for v in i.version:
                cont=cont+1
                if (v.actual and (v.estado!="Bloqueado" and v.estado!="Eliminado")):
                    return False
    if cont>0:
        return True
    else:
        return False

def cerrarFase(idf=None):
    """Cierra una fase, recibe el id de la fase
    """
    init_db()
    f = getFaseId(idf)
    f.estado="Cerrada"
    session.merge(f)
    session.commit()
    shutdown_session()
    
def actualizarFecha(idf=None):
    """Actualiza la fecha de ultima modificacion de la fase, recibe el id de la fase
    """
    init_db()
    f=getFaseId(idf)
    f.fechaUltMod=datetime.today()
    session.merge(f)
    session.commit()
    shutdown_session()
    actualizarFechaProyecto(f.proyecto)
    
def abrirFase(idf=None):
    init_db()
    f=getFaseId(idf)
    f.estado="Abierta"
    session.merge(f)
    session.commit()
    shutdown_session()
    
def actualizarFechaProyecto(pro=None):
    """Actualiza la fecha de modificacion del proyecto pro
    """
    if pro:
        init_db()
        pro.fechaUltMod=datetime.today()
        session.merge(pro)
        session.commit()
        shutdown_session()