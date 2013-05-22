from entidad import Proyecto, Peticion, Voto, Usuario, Item, VersionItem
from initdb import db_session, init_db, shutdown_session
from pms.modelo.proyectoControlador import getProyectoId
session = db_session()

def crearPeticion(proyecto=None,idv=None,comentario=None, idusuario=None):
    
    init_db()
    peticion=Peticion(proyecto,idv,comentario,"Pendiente", idusuario)
    session.add(peticion)
    session.commit()
    shutdown_session()
    

    
    
    
    
    