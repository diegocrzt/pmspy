'''
Created on 14/04/2013

@author: mpoletti

'''
from entidad import Fase, Usuario, Rol, User_Rol
from initdb import db_session, init_db
from tipoItemControlador import getTiposFase
from atributoControlador import getAtributosTipo, getAtributoId
from usuarioControlador import getUsuario,getUsuarioById,getUsuarios
from faseControlador import getFase, getFaseId, getFases



session = db_session()

def getRolesFase(fase=None):
    """Obtener tipos de items
    """
    init_db()
    res = session.query(Rol).filter(Rol.fase_id==fase).all()
    return res

def getRolNombre(nombre=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    res = session.query(Rol).filter(Rol.nombre==nombre).first()
    return res

def getRolId(id=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    res = session.query(Rol).filter(Rol.id==id).first()
    return res


def getRolUser(idr=None,idu=None):
    """
    recupera un tipo por su id
    
    """
    init_db()
    res = session.query(User_Rol).filter(User_Rol.usuario_id==idu).filter(User_Rol.rol_id==idr).first()
    return res

def getRelRol(idr=None):
    init_db()
    res = session.query(User_Rol).filter(User_Rol.rol_id==idr).all()
    return res
        
        
def comprobarRol(nombre=None, fase=None):
    """
    valida si ya existe un item con ese nombre en esa fase
    """
    roles=getRolesFase(fase)
    for r in roles:
        if(r.nombre==nombre):
            return True

    return False                
    
def comprobarUser_Rol(idr=None,idu=None):
    res=getRolUser(idr,idu)
    if res==None :
        return True
    else:
        return False

def crearRol(fa=None,nom=None,codi=None,codt=None,codlb=None):
    """Crea un tipo de item

    """
    init_db()
    session = db_session()
    rol = Rol(fase_id=fa, nombre=nom,codigoItem=codi,codigoTipo=codt,codigoLB=codlb)
    session.add(rol)
    session.commit()
    
def editarRol(idr=None,nom=None,codi=None,codt=None,codlb=None):
    """
    permite editar un tipo de item existente
    """
    init_db()
    rol=getRolId(idr)
    rol.nombre=nom
    rol.codigoItem=codi
    rol.codigoTipo=codt
    rol.codigoLB=codlb
    session.merge(rol)
    session.commit()



def eliminarRol(idr=None):
    """
    elimina un tipo de item
    """
    if(idr):
        init_db()
        session.query(User_Rol).filter(User_Rol.rol_id==idr).delete()
        session.query(Rol).filter(Rol.id==idr).delete()
        session.commit()
        
def crearUser_Rol(idr=None, idu=None):
    rel = User_Rol(usuario_id=idu,rol_id=idr)
    session.add(rel)
    session.commit()
    
def eliminarUser_Rol(idr=None, idu=None):
    session.query(User_Rol).filter(User_Rol.rol_id==idr).filter(User_Rol.usuario_id==idu).delete()
    session.commit()

        
