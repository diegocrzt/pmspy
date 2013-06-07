from entidad import Proyecto, Peticion, Voto, Usuario, Item, VersionItem, Miembro, ItemPeticion
from initdb import db_session, init_db, shutdown_session
from pms.modelo.proyectoControlador import getProyectoId
from pms.modelo.usuarioControlador import getUsuarios
session = db_session()



def getPeticion(id=None):
    """
    recupera un usuario por su nombre de usuario
    """
    init_db()
    res=session.query(Peticion).filter(Peticion.id==id).first()
    shutdown_session()
    return res

def getItemPeticion(idv=None):
    """
    
    """
    init_db()
    res=session.query(ItemPeticion).filter(ItemPeticion.item_id==idv).first()
    shutdown_session()
    return res

    
def crearPeticion(numero,proyecto_id,comentario,estado,usuario_id,cantVotos,cantItems,costoT,dificultadT,fechaCreacion,fechaEnvio):
    """
    Crea una Peticion, recibe el id del proyecto, el id de la version del item sobre el cual se solicita la peticion, un comentario y el id del usuario que solicita la peticioin
    """
    init_db()
    peticion=Peticion(numero,proyecto_id,comentario,estado,usuario_id,cantVotos,cantItems,costoT,dificultadT,fechaCreacion,fechaEnvio)
    session.add(peticion)
    session.commit()
    shutdown_session()
    
def editarPeticion(idp,comentario,estado,usuario_id,cantVotos,cantItems,costoT,dificultadT,fechaCreacion,fechaEnvio):
    """
    permite editar un usuario existente
    """
    init_db()
    p = getPeticion(idp)
    p.comentario=comentario
    p.estado=estado
    p.usuario_id=usuario_id
    p.cantVotos=cantVotos
    p.cantItems=cantItems
    p.costoT=costoT
    p.difultadT=dificultadT
    p.fechaCreacion=fechaCreacion
    p.fechaEnvio=fechaEnvio
    session.merge(p)
    session.commit()
    shutdown_session()
    
def eliminarPeticion(id=None):
    init_db()
    u=getPeticion(id)
    session.query(Peticion).filter(Peticion.id==u.id).delete()
    session.commit()
    shutdown_session()
    
def comprobarItemPeticion(idv=None):
    res=getItemPeticion(idv)
    if res==None:
        return True
    else:
        return False
    
def agregarItem(idv=None,idp=None,costo=None,dificultad=None):
    r=comprobarItemPeticion(idv)
    if r==True:
        init_db()
        ipeticion=ItemPeticion(idv,idp,costo,dificultad)
        session.add(ipeticion)
        shutdown_session()
        return True
    else:
        return False
    
def quitarItem(id=None):
    init_db()
    session.query(ItemPeticion).filter(ItemPeticion.item_id==id).delete()
    session.commit()
    shutdown_session()

def getVoto(idu=None,idp=None):
    init_db()
    res=session.query(Voto).filter(Voto.user_id==idu).filter(Voto.peticion_id==idp).first()
    shutdown_session()
    return res

def comprobarVoto(idu=None,idp=None):
    res=getVoto(idu,idp)
    if res==None:
        return True
    else:
        return False

def agregarVoto(idu=None,idp=None,valor=None):
    if comprobarVoto(idu,idp):
        init_db()
        v=Voto(idu,idp,valor)
        session.add(v)
        shutdown_session()
        return True
    else:
        return False
    
    

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
    
    
    
    
    