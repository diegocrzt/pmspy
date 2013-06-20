'''
Created on 14/04/2013

@author: mpoletti
@author: synchro, Natalia Valdez
@author: mpoletti
'''
from entidad import Proyecto, Usuario
from initdb import db_session, init_db, shutdown_session
import faseControlador
import miembroControlador
from sqlalchemy import or_
from pms.modelo import controllerHelper
session = db_session()

def getProyectos():
    """Devuelve todos los proyectos de la base de datos
    """
    init_db()
    proyectos = session.query(Proyecto).all()
    shutdown_session()
    return proyectos

def crearProyecto(nom=None, cant=None, fechainicio=None, fechafin=None, fechamod=None, lider=None, estado=None):
    """Crea un proyecto
    
    """
    init_db()
    session = db_session()
    pro = Proyecto(nombre=nom, cantFase=cant, fechaInicio=fechainicio, fechaFin=fechafin, fechaUltMod=fechamod, delider=lider, estado="Pendiente")
    session.add(pro)
    session.commit()
    shutdown_session()
   
def getProyecto(nombre=None):
    """
    Recupera un proyecto por su nombre
    """
    if(nombre):
        init_db()
        res = session.query(Proyecto).filter(Proyecto.nombre == nombre).first()
        shutdown_session()
        return res
       
       
def getProyectoId(idp=None):
    """
    Recupera un proyecto por su id
    """
    if(idp):
        init_db()
        res = session.query(Proyecto).filter(Proyecto.id == idp).first()
        shutdown_session()
        return res
def comprobarProyecto(nombre=None):
    """
    Comprueba si un proyecto ya existe
    """
    a = getProyecto(nombre)
    if a == None:
        return False
    else:
        return True
   
def eliminarProyecto(proyecto=None):
    """
    Elimina un proyecto
    """
    if(proyecto):
        p = getProyectoId(proyecto)
        for f in p.fases:
            faseControlador.eliminarFase(f.id)
            p.cantFase = p.cantFase - 1
        
        for m in p.miembros:
            miembroControlador.eliminarMiembro(m)
            
        for s in p.solicitudes:
            controllerHelper.eliminarPeticion(s.id)
            
        init_db()  
        session.query(Proyecto).filter(Proyecto.id == proyecto).delete()
        session.commit()
        shutdown_session()

def actualizarCantFases(idp=None, aumentar=None):
    """
    Actualiza la cantidad de fases de un proyecto
    """
    init_db()
    p = getProyectoId(idp)
    if aumentar:
        p.cantFase = p.cantFase + 1
    else:
        p.cantFase = p.cantFase - 1
    session.merge(p)
    session.commit()
    shutdown_session()

def inicializarProyecto(p):
    """ 
    Inicializa el proyecto estableciendo su estado a Iniciado
    """
    init_db()
    proy = getProyectoId(p)
    n = 1
    for f in proy.fases:
        f.numero = n
        session.merge(f)
        n = n + 1
    proy = getProyectoId(p)
    proy.estado = "Iniciado"
    session.merge(proy)
    session.commit()
    shutdown_session()
    
def getProyectosPaginados(pagina=None, tam_pagina=None, filtro=None):
    """
    Devuelve una lista de proyectos de tamanio tam_pagina de la pagina pagina, la pagina empieza en 0
    """
    init_db()
    if  filtro:
        query = getProyectosFiltrados(filtro)
    else:
        query = session.query(Proyecto).order_by(Proyecto.id)
    if pagina and tam_pagina:
        query = query.offset(pagina * tam_pagina)
    shutdown_session()
    return query.limit(tam_pagina)

def getCantProyectos(filtro=None):
    """Devuelve la cantidad de proyecto existentes en la base de datos
    """
    init_db()
    if (filtro):
        p = getProyectosFiltrados(filtro).count()
    else:
        p = session.query(Proyecto).count()
    shutdown_session()
    return p

def getProyectosFiltrados(filtro=None):
    """Devuelve una lista de proyectos por nombre, estado, id, y cantFases
    """
    if (filtro):
        init_db()
        if(filtro.isdigit()):
            query = session.query(Proyecto).filter(or_(Proyecto.id == filtro, Proyecto.cantFase == filtro, Proyecto.nombre.ilike("%" + filtro + "%"), Proyecto.estado.ilike("%" + filtro + "%")))
        else:
            query = session.query(Proyecto).join(Usuario).filter(Usuario.nombre.ilike("%" + filtro + "%") | Proyecto.nombre.ilike("%" + filtro + "%") | Proyecto.estado.ilike("%" + filtro + "%"))
        shutdown_session()
        return query
    
    
def controlFProyecto(idp):
    p=getProyectoId(idp)
    bandera=False
    for f in p.fases:
        if f.estado!="Cerrada":
            bandera=True
    for s in p.solicitudes:
        if s.estado=="EnVotacion":
            bandera=True
    if bandera==True:
        return False
    else:
        return True
    
def finalizarProyecto(idp=None):
    p=getProyectoId(idp)
    p.estado="Finalizado"    
    init_db()
    session.merge(p)
    session.commit()
    shutdown_session()
    