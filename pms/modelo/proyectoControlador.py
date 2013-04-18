'''
Created on 14/04/2013

@author: mpoletti
@author: synchro, Natalia Valdez
@author: mpoletti
'''
from entidad import Proyecto
from initdb import db_session, init_db

session = db_session()

def getProyectos():
    """Obtener proyectos
    """ 
    init_db()
    proyectos = session.query(Proyecto).all()
    return proyectos

def crearProyecto(nom=None, cant=None, fechainicio=None, fechafin=None, fechamod=None, lider=None):
    """Crea un proyecto

    """
    init_db()
    session = db_session()
    pro = Proyecto(nombre=nom,cantFase=cant, fechaInicio=fechainicio, fechaFin=fechafin,fechaUltMod=fechamod, lider=lider)
    session.add(pro)
    session.commit()
    
def getProyecto(nombre=None):
    """
    recupera un proyecto por su nombre de usuario
    """
    if(nombre):
            res=session.query(Proyecto).filter(Proyecto.nombre==nombre).first()
            return res


def getProyectoId(id=None):
    """
    recupera un proyecto por su nombre de usuario
    """
    if(id):
            res=session.query(Proyecto).filter(Proyecto.id==id).first()
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
        session.query(Proyecto).filter(Proyecto.nombre==proyecto).delete()
        session.commit()
