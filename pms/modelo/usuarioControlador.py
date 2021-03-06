'''
Created on 05/04/2013

@author: Martin Poletti, Natalia Valdez
'''
from entidad import Usuario, Proyecto, User_Rol
from initdb import db_session, init_db, shutdown_session
import hashlib

session = db_session()

def validar(username=None, passwd=None):
    """
    valida un usuario para el login
    """
    init_db()
    res = session.query(Usuario).filter(Usuario.nombredeusuario==username).first()
    shutdown_session()
    if res == None:
        return False
    else:
        if res.clave == hashlib.sha1( passwd ).hexdigest():
            return True
        else:
            return False
        
def getUsuarios():
    """Obtener usuarios
    """ 
    init_db()
    res = session.query(Usuario).order_by(Usuario.id)
    shutdown_session()
    return res

def crearUsuario(nom=None, usua=None, contrase=None, admin=None):
    """Crea un usuario

    """
    init_db()
    session = db_session()
    clavecifra= hashlib.sha1( contrase ).hexdigest()
    user = Usuario(nombre=nom, nombredeusuario=usua, clave=clavecifra, isAdmin=admin)
    session.add(user)
    session.commit()
    shutdown_session()
    
def eliminarUsuario(username=None):
    """
    elimina un usuario
    """
    if(username):
        init_db()
        u=getUsuario(username)
        session.query(User_Rol).filter(User_Rol.usuario_id==u.id).delete()
        session.query(Usuario).filter(Usuario.nombredeusuario==username).delete()
        session.commit()
        shutdown_session()
    else:
        print "eliminar no anda"
            
def getUsuario(username=None):
    """
    recupera un usuario por su nombre de usuario
    """
    if(username):
        init_db()
        res=session.query(Usuario).filter(Usuario.nombredeusuario==username).first()
        shutdown_session()
        return res
        
def getUsuarioById(idu=None):
    """
    recupera un usuario por su id
    """
    if(idu):
        init_db()
        res=session.query(Usuario).filter(Usuario.id==idu).first()
        shutdown_session()
        return res
        
def editarUsuario(idu=None,nom=None, usua=None, contrase=None, admin=None):
    """
    permite editar un usuario existente
    """
    init_db()
    u = getUsuarioById(idu)
    u.nombre=nom
    u.nombredeusuario=usua
    u.isAdmin=admin
    if contrase!=None:
        u.clave=hashlib.sha1( contrase ).hexdigest()
    session.merge(u)
    session.commit()
    shutdown_session()
    
    
def comprobarUsuario(user=None):
    """
    comprueba si un usuario ya existe
    """
    a=getUsuario(user)
    if a == None:
        return False
    else:
        return True
    
def comprobarUsuarioB(ident=None,user=None):
    """
    comprueba sin usuario existe por id o por nombre d eusuario
    """
    a=getUsuarioById(ident)
    if a == None:
        return False
    else:
        return True

def usuarioIsLider(username=None):
    u=getUsuario(username)
    init_db()
    res=session.query(Proyecto).filter(Proyecto.delider==u.id).first()
    shutdown_session()
    return res
