from entidad import Proyecto, Comite, Miembro, Peticion, Voto, Usuario, Item, VersionItem
from initdb import db_session, init_db, shutdown_session
from pms.modelo.proyectoControlador import getProyectoId
from pms.modelo.usuarioControlador import getUsuarioById, getUsuarios



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
    shutdown_session()
    com=getComiteProyecto(proyecto)
    agregarUsuario(com.id,lider)
    
def agregarUsuario(comite=None,usuario=None):
    init_db()
    miembro=Miembro(comite,usuario)
    session.add(miembro)
    session.commit()
    shutdown_session()
    
def eliminarMiembro(user_id=None,comite_id=None):
    init_db()  
    session.query(Miembro).filter(Miembro.user_id==user_id).filter(Miembro.comite_id==comite_id).delete()
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


def agregarLista(agregar=None,comite=None):
    c=0
    quitar=[]
    for l in agregar:
        c=c+1
    if (c % 2)==0:
        mid=[]
        for m in comite.miembros:
            mid.append(m.user_id)
            for a in agregar:
                if a==m.user_id:
                    agregar.remove(m.user_id)
        us=getUsuarios()
        for a in agregar:
            agregarUsuario(comite.id,a)
        for q in quitar:
            eliminarMiembro(q,comite.id)
        return True
    else:
        return False


def crearPeticion(proyecto=None,idv=None,comentario=None):
    pr=getProyectoId(proyecto)
    comite=pr.comite
    init_db()
    peticion=Peticion(comite.id,idv,comentario,"Pendiente")
    session.add(peticion)
    session.commit()
    shutdown_session()
    

    
    
    
    
    