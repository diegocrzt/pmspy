'''
Created on 05/04/2013

@author: Martin Poletti, Natalia Valdez
'''
from entidad import Usuario, Proyecto
from initdb import db_session, init_db
import hashlib

session = db_session()

def validar(username=None, passwd=None):
    """
    valida un usuario para el login
    """
    init_db()
    res = session.query(Usuario).filter(Usuario.nombredeusuario==username).first()
    print res
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
    res = session.query(Usuario).all()
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
    
def eliminarUsuario(username=None):
    """
    elimina un usuario
    """
    if(username):
        session.query(Usuario).filter(Usuario.nombredeusuario==username).delete()
        session.commit()
            
def getUsuario(username=None):
    """
    recupera un usuario por su nombre de usuario
    """
    if(username):
            res=session.query(Usuario).filter(Usuario.nombredeusuario==username).first()
            return res
        
def getUsuarioById(idu=None):
    """
    recupera un usuario por su id
    """
    if(idu):
            res=session.query(Usuario).filter(Usuario.id==idu).first()
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
    res=session.query(Proyecto).filter(Proyecto.lider==u.id).first()
    return res
