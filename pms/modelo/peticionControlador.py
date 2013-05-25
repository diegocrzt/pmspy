from entidad import Proyecto, Peticion, Voto, Usuario, Item, VersionItem, Miembro
from initdb import db_session, init_db, shutdown_session
from pms.modelo.proyectoControlador import getProyectoId
from pms.modelo.usuarioControlador import getUsuarios
session = db_session()

def crearPeticion(proyecto=None,idv=None,comentario=None, idusuario=None):
    """
    Crea una Peticion, recibe el id del proyecto, el id de la version del item sobre el cual se solicita la peticion, un comentario y el id del usuario que solicita la peticioin
    """
    init_db()
    peticion=Peticion(proyecto,idv,comentario,"Pendiente", idusuario)
    session.add(peticion)
    session.commit()
    shutdown_session()
    
def getMiembros(idp=None):
    """
    Devuelve los usuarios que son miembros de el comite de un proyecto, recibe el id del proyecto
    """
    init_db()
    res= session.query(Miembro).filter(Miembro.proyecto_id==idp).all()
    shutdown_session()
    return res
    
def getMiembro(idp=None,idu=None):
    """
    devuelve un usuario que sea miembro de un poryecto, recive el id del usuario y el proyecto
    """
    init_db()
    res = session.query(Miembro).filter(Miembro.proyecto_id==idp).filter(Miembro.user_id==idu).first()
    shutdown_session()
    return res

def agregarMiembro(idp=None,idu=None):
    """
    Agrega un usuario a el comite de un proyecto, recibe el id del proyecto y del usuario, devuelve false si el usuario ya esta en el comite
    """
    if getMiembro(idp,idu)==None:
        init_db()
        m=Miembro(idp,idu)
        session.add(m)
        session.commit()
        shutdown_session()
        return True
    else:
        return False

def quitarMiembro(idp=None,idu=None):
    """
    Elimina un usuario a el comite de un proyecto, recibe el id del proyecto y del usuario, devuelve false si el usuario no esta en el comite
    """
    if getMiembro(idp,idu)!=None:
        init_db()
        session.query(Miembro).filter(Miembro.user_id==idu).filter(Miembro.proyecto_id==idp).delete()
        session.commit()
        shutdown_session()
        return True
    else:
        return False

def agregarListaMiembros(lista=None,idp=None):
    """
    Cambia el conjunto de usuarios que pertenecen al comite de un proyecto a el conjunto de usuarios que pertenecen a la lista pasada como parametro
    """
    c=0
    for l in lista:
        c=c+1
    if (c%2)!=0:
        usr=getUsuarios()
        for u in usr:
            quitarMiembro(idp,u.id)
        for l in lista:
            agregarMiembro(idp,l.id)
        return True
    else:
        return False 
    
    
    
    
    