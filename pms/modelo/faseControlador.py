'''
Created on 18/04/2013

@author: Natalia Valdez
'''

from initdb import db_session, init_db
from entidad import Fase

session = db_session()

def getFases(p=None):
    """Obtener fases
    """ 
    init_db()
    fases = session.query(Fase).filter(Fase.proyecto==p).order_by(Fase.numero)
    return fases


def crearFase(nom=None, num=None, fechainicio=None, fechafin=None, fechamod=None, estado=None, proy=None):
    """Crea un proyecto

    """
    init_db()
    session = db_session()
    fa = Fase(nombre=nom,numero=num, fechaInicio=fechainicio, fechaFin=fechafin,fechaUltMod=fechamod, estado="Abierta", proyecto=proy)
    session.add(fa)
    session.commit()
    
def getFase(numero=None, proy=None):
    """
    recupera un proyecto por su numero
    """
    if(numero and proy):
            res=session.query(Fase).filter(Fase.numero==numero).filter(Fase.proyecto==proy).first()
            return res

def comprobarFase(numero=None, proy=None):
    """
    comprueba si una fase ya existe
    """
    a=getFase(numero, proy)
    if a == None:
        return False
    else:
        return True
    
def eliminarFase(fase=None, proy=None):
    """
    elimina una fase
    """
    if(fase and proy):
        session.query(Fase).filter(Fase.id==fase).delete()
        session.commit()
        
def getFaseId(id=None):
    """
    recupera una fase por su nombre de usuario
    """
    if(id):
            res=session.query(Fase).filter(Fase.id==id).first()
            return res      
          
def editarFase(id=None,nom=None, numero=None, fechaini=None, fechafin=None):
    """
    permite editar una fase existente
    """
    init_db()
    f = getFaseId(id)
    f.nombre=nom
    f.numero= numero
    f.fechaInicio=fechaini
    f.fechaFin=fechafin
    session.merge(f)
    session.commit()