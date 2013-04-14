'''
Created on 05/04/2013

@author: Martin Poletti
'''
from entidad import Usuario
from initdb import db_session, init_db

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
        if res.clave == passwd:
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
    user = Usuario(nombre=nom, nombredeusuario=usua, clave=contrase, isAdmin=admin)
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
        
def getUsuarioById(idd=None):
    """
    recupera un usuario por su id
    """
    if(idd):
            res=session.query(Usuario).filter(Usuario.idd==idd).first()
            return res
        
def editarUsuario(id=None,nom=None, usua=None, contrase=None, admin=None):
    """
    permite editar un usuario existente
    """
    init_db()
    print "id en editar"
    print id
    u = getUsuarioById(id)
    u.nombre=nom
    u.nombredeusuario=usua
    u.clave=contrase
    u.isAdmin=admin
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
    a=getUsuario(user)
    a=getUsuarioById(ident)
    if a == None:
        return False
    else:
        return True

    