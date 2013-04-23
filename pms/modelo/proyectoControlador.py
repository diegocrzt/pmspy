'''
Created on 14/04/2013

@author: mpoletti
@author: synchro, Natalia Valdez
@author: mpoletti
'''
from entidad import Proyecto
from initdb import db_session, init_db
import faseControlador

session = db_session()

def getProyectos():
    """Obtener proyectos
    """
    init_db()
    proyectos = session.query(Proyecto).all()
    return proyectos

def crearProyecto(nom=None, cant=None, fechainicio=None, fechafin=None, fechamod=None, lider=None, estado=None):
    """Crea un proyecto

    """
    init_db()
    session = db_session()
    pro = Proyecto(nombre=nom,cantFase=cant, fechaInicio=fechainicio, fechaFin=fechafin,fechaUltMod=fechamod, lider=lider, estado="Pendiente")
    session.add(pro)
    session.commit()
   
def getProyecto(nombre=None):
    """
    recupera un proyecto por su nombre
    
    """
    if(nombre):
            res=session.query(Proyecto).filter(Proyecto.nombre==nombre).first()
            return res
       
       
def getProyectoId(idp=None):
    """
    recupera un proyecto por su id
    """
    if(idp):
            res=session.query(Proyecto).filter(Proyecto.id==idp).first()
            return res
def comprobarProyecto(nombre=None):
    """
    comprueba si un proyecto ya existe
    """
    a=getProyecto(nombre)
    if a == None:
        return False
    else:
        return True
   
def eliminarProyecto(proyecto=None):
    """
    elimina un proyecto
    """
    if(proyecto):
        fases=faseControlador.getFases(proyecto)
        for f in fases:
            faseControlador.eliminarFase(f.id, proyecto)
        print "sale del eliminar Fase"            
        session.query(Proyecto).filter(Proyecto.id==proyecto).delete()
        session.commit()

def actualizarCantFases(idp=None, aumentar=None):
    """
    actualiza la cantidad de fases de un proyecto
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
    inicializa el proyecto
    """
    fases=faseControlador.getFases(p)
    n=1
    for f in fases:
        f.numero=n
        session.merge(f)
        n=n+1        
    proy=getProyectoId(p)
    proy.estado="Iniciado"
    session.merge(proy)
    session.commit()
    
