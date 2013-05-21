from entidad import Proyecto, Comite, Miembro, Peticion, Voto, Usuario, Item, VersionItem
from initdb import db_session, init_db, shutdown_session
from pms.modelo.proyectoControlador import getProyectoId



session = db_session()

def getComiteProyecto(proyecto=None):
    init_db()
    res = session.query(Comite).filter(Comite.proyecto_id==proyecto).first()
    shutdown_session()
    return res

def crearComite(proyecto=None):
    """
    Crea un nuevo comite
    """
    init_db()
    lider=getProyectoId(proyecto).lider.id
    comite=Comite(proyecto)
    session.add(comite)
    session.commit()
    com=getComiteProyecto(proyecto)
    shutdown_session()
    agregarUsuario(com.id,lider)
    
def agregarUsuario(comite=None,usuario=None):
    init_db()
    miembro=Miembro(comite,usuario)
    session.add(miembro)
    session.commit()
    shutdown_session()
    
def comprobarMiembros(comite):
    init_db()
    res = session.query(Miembro).filter(Miembro.comite_id==comite).all()
    shutdown_session()
    c=0
    for i in res:
        c=c+1
    if (c%2)==0:
        return True
    else:
        return False


def agregarLista(lista=None,comite=None):
    c=0
    for l in lista:
        c=c+1
    if (c % 2)==0:
        for l in lista:
            agregarUsuario(comite.id,l.id)
        return "usuarios agregados con exito"
    else:
        return "No se pueden agregar usuarios impares"
    
def crearPeticion(proyecto=None,idv=None,comentario=None):
    pr=getProyectoId(proyecto)
    comite=pr.comite
    init_db()
    peticion=Peticion(comite.id,idv,comentario,"Pendiente")
    session.add(peticion)
    session.commit()
    shutdown_session()
    

    
    
    
    
    