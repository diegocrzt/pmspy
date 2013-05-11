'''
Created on 18/04/2013

@author: Natalia Valdez
'''

from initdb import db_session, init_db
from entidad import Fase
import proyectoControlador

session = db_session()

def getFases(p=None):
    """Obtener fases
    """
    fases = session.query(Fase).filter(Fase.delproyecto==p).order_by(Fase.numero)
    return fases


def crearFase(nom=None, num=None, fechainicio=None, fechafin=None, fechamod=None, estado=None, proy=None):
    """Crea una fase

    """
    fa = Fase(nombre=nom,numero=num, fechaInicio=fechainicio, fechaFin=fechafin,fechaUltMod=fechamod, estado="Abierta", delproyecto=proy)
    session.add(fa)
    session.commit()
    fa.proyecto.cantFase=fa.proyecto.cantFase+1
    session.merge(fa.proyecto)
    session.commit()
   
def getFase(numero=None, proy=None):
    """
    recupera una fase por su numero y proyecto id
    """
    if(numero and proy):
            res=session.query(Fase).filter(Fase.numero==numero).filter(Fase.delproyecto==proy).first()
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
        fa=getFaseId(fase)
        fa.proyecto.cantFase=fa.proyecto.cantFase-1
        session.query(Fase).filter(Fase.id==fase).delete()
        session.commit()
        
       
def getFaseId(id=None):
    """
    recupera una fase por su id
    """
    if(id):
            res=session.query(Fase).filter(Fase.id==id).first()
            return res      
         
def editarFase(id=None,nom=None, numero=None, fechaini=None, fechafin=None):
    """
    permite editar una fase existente
    """
    f = getFaseId(id)
    f.nombre=nom
    f.numero= numero
    f.fechaInicio=fechaini
    f.fechaFin=fechafin
    session.merge(f)
    session.commit()
    
def getFasesPaginadas(pagina=None,tam_pagina=None, p=None):
    """
    Devuelve una lista de fases de tamanio tam_pagina de la pagina pagina, la pagina empieza en 0
    """
    query = session.query(Fase).filter(Fase.delproyecto==p).order_by(Fase.id)
    if pagina and tam_pagina:
        query = query.offset(pagina*tam_pagina)
    return query.limit(tam_pagina)

