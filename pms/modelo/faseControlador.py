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
    fa = Fase(nombre=nom,numero=num, fechaInicio=fechainicio, fechaFin=fechafin,fechaUltMod=fechamod, estado=estado, proyecto=proy)
    session.add(fa)
    session.commit()
    
def getFase(numero=None):
    """
    recupera un proyecto por su numero
    """
    if(numero):
            res=session.query(Fase).filter(Fase.numero==numero).first()
            return res

def comprobarFase(numero=None):
    """
    comprueba si una fase ya existe
    """
    a=getFase(numero)
    if a == None:
        return False
    else:
        return True
    
def eliminarFase(fase=None):
    """
    elimina una fase
    """
    if(fase):
        session.query(Fase).filter(Fase.numero==fase).delete()
        session.commit()
        
        
