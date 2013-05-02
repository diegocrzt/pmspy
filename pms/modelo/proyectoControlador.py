'''
Created on 14/04/2013

@author: mpoletti
@author: synchro, Natalia Valdez
@author: mpoletti
'''
from entidad import Proyecto
from initdb import db_session, init_db
import faseControlador
from sqlalchemy import or_
session = db_session()

def getProyectos():
    """Devuelve todos los proyectos de la base de datos
    """
    init_db()
    proyectos = session.query(Proyecto).all()
    return proyectos

def crearProyecto(nom=None, cant=None, fechainicio=None, fechafin=None, fechamod=None, lider=None, estado=None):
    """Crea un proyecto
    
    """
    init_db()
    session = db_session()
    pro = Proyecto(nombre=nom,cantFase=cant, fechaInicio=fechainicio, fechaFin=fechafin,fechaUltMod=fechamod, delider=lider, estado="Pendiente")
    session.add(pro)
    session.commit()
   
def getProyecto(nombre=None):
    """
    Recupera un proyecto por su nombre
    """
    if(nombre):
            res=session.query(Proyecto).filter(Proyecto.nombre==nombre).first()
            return res
       
       
def getProyectoId(idp=None):
    """
    Recupera un proyecto por su id
    """
    if(idp):
            res=session.query(Proyecto).filter(Proyecto.id==idp).first()
            return res
def comprobarProyecto(nombre=None):
    """
    Comprueba si un proyecto ya existe
    """
    a=getProyecto(nombre)
    if a == None:
        return False
    else:
        return True
   
def eliminarProyecto(proyecto=None):
    """
    Elimina un proyecto
    """
    if(proyecto):
        p=getProyectoId(proyecto)
        for f in p.fases:
            faseControlador.eliminarFase(f.id)
            p.cantFase=p.cantFase-1   
        session.query(Proyecto).filter(Proyecto.id==proyecto).delete()
        session.commit()

def actualizarCantFases(idp=None, aumentar=None):
    """
    Actualiza la cantidad de fases de un proyecto
    """
    init_db()
    p = getProyectoId(idp)
    if aumentar:
        p.cantFase= p.cantFase+1
    else:
        p.cantFase = p.cantFase-1
    session.merge(p)
    session.commit()

def inicializarProyecto(p):
    """ 
    Inicializa el proyecto estableciendo su estado a Iniciado
    """
    proy=getProyectoId(p)
    n=1
    for f in proy.fases:
        f.numero=n
        session.merge(f)
        n=n+1
    proy=getProyectoId(p)
    proy.estado="Iniciado"
    session.merge(proy)
    session.commit()
    
def getProyectosPaginados(pagina=None,tam_pagina=None, filtro=None):
    """
    Devuelve una lista de proyectos de tamanio tam_pagina de la pagina pagina, la pagina empieza en 0
    """
    if  filtro:
        query=getProyectosFiltrados(filtro)
    else:
        query = session.query(Proyecto).order_by(Proyecto.id)
    if pagina and tam_pagina:
        query = query.offset(pagina*tam_pagina)
    return query.limit(tam_pagina)

def getCantProyectos(filtro=None):
    """Devuelve la cantidad de proyecto existentes en la base de datos
    """
    if (filtro):
        p=getProyectosFiltrados(filtro).count()
    else:
        p=session.query(Proyecto).count()
    return p

def getProyectosFiltrados(filtro=None):
    """Devuelve una lista de proyectos por nombre, estado, id, y cantFases
    """
    if (filtro):
        if(filtro.isdigit()):
            query=session.query(Proyecto).filter(or_(Proyecto.id==filtro, Proyecto.cantFase==filtro, Proyecto.nombre.ilike("%"+filtro+"%"), Proyecto.estado.ilike("%"+filtro+"%")))
        else:    
            query=session.query(Proyecto).filter(Proyecto.nombre.ilike("%"+filtro+"%") | Proyecto.estado.ilike("%"+filtro+"%"))
        return query
            
def main():
    f="piki"
    query=getProyectosFiltrados(f)
    str="holta"
    if query:
        print "query"
        for q in query:
            print q.nombre
    else:
        print query
        
if __name__ == "__main__":  
    main()   
    
    