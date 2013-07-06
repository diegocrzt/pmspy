'''
Created on 14/04/2013

@author: mpoletti
@author: Natalia Valdez
'''
import flask
from entidad import Rol, User_Rol
from initdb import db_session, init_db, shutdown_session
from faseControlador import getFaseId

session = db_session()

def getRolesFase(fase=None):
    """Devuelve los roles de una fase, recibe el id de la fase
    """
    init_db()
    res = session.query(Rol).filter(Rol.fase_id==fase).all()
    shutdown_session()
    return res

def getRolNombre(nombre=None):
    """
    Devuelve un rol por su nombre, recibe el nombre
    """
    init_db()
    res = session.query(Rol).filter(Rol.nombre==nombre).first()
    shutdown_session()
    return res

def getRolId(id=None):
    """
    Devuelve un rol por su id, recibe el id
    """
    init_db()
    res = session.query(Rol).filter(Rol.id==id).first()
    shutdown_session()
    return res


def getRolUser(idr=None,idu=None):
    """
    Devuelve un rol de un ususairo, recibe el id del rol y el id del usuario
    """
    init_db()
    res = session.query(User_Rol).filter(User_Rol.usuario_id==idu).filter(User_Rol.rol_id==idr).first()
    shutdown_session()
    return res

def getRelRol(idr=None):
    """Devuelve una relacion de rol y usuairo, recibe el id de la relacion
    """
    init_db()
    res = session.query(User_Rol).filter(User_Rol.rol_id==idr).all()
    shutdown_session()
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
    """
    Verifica si el usuario ya tiene asignado el rol, recibe el id del rol y el del usuario
    """
    res=getRolUser(idr,idu)
    if res==None :
        return True
    else:
        return False

def crearRol(fa=None,nom=None,codi=None,codt=None,codlb=None):
    """Crea un rol nuevo, recibe el id de la fase, el nombre, el codigo de permisos de item, el codifo de permisos de tipo de item
    y el codigo de permisos de linea base 
    """
    init_db()
    session = db_session()
    rol = Rol(fase_id=fa, nombre=nom,codigoItem=codi,codigoTipo=codt,codigoLB=codlb)
    session.add(rol)
    session.commit()
    shutdown_session()

def editarRol(idr=None,nom=None,codi=None,codt=None,codlb=None):
    """
    Edita un rol existente, recibe el id, el nombre, el codigo de permisos de item, el codifo de permisos de tipo de item
    y el codigo de permisos de linea base del rol
    """
    init_db()
    rol=getRolId(idr)
    rol.nombre=nom
    rol.codigoItem=codi
    rol.codigoTipo=codt
    rol.codigoLB=codlb
    session.merge(rol)
    session.commit()
    shutdown_session()



def eliminarRol(idr=None):
    """
    Elimina un rol, recibe el id del rol a eliminarse
    """
    if(idr):
        init_db()
        session.query(User_Rol).filter(User_Rol.rol_id==idr).delete()
        session.query(Rol).filter(Rol.id==idr).delete()
        session.commit()
        shutdown_session()
        
        
def crearUser_Rol(idr=None, idu=None):
    """Crea una relacion entre un usuairo y un rol, osea asignar un rol a un usuario, recibe el ide del rol y el id del usuario
    """
    init_db()
    rel = User_Rol(usuario_id=idu,rol_id=idr)
    session.add(rel)
    session.commit()
    shutdown_session()
    
def eliminarUser_Rol(idr=None, idu=None):
    """Elimina una relacion entre un rol y un usuario, osea desasigna un rol a un usuario, recibe el id del rol y el id del usuario
    """
    init_db()
    session.query(User_Rol).filter(User_Rol.rol_id==idr).filter(User_Rol.usuario_id==idu).delete()
    session.commit()
    shutdown_session()
    
def getRolesDeUsuarioEnFase(idu=None,idf=None):
    """Devuelve una lista de roles de un usuario en unafase. Recibe el id del usuario y el id de la fase
    """
    init_db()
    if idu and idf:
        res=getRolesFase(idf)
        roles=[]
        for r in res:
            if not comprobarUser_Rol(r.id,idu):
                roles.append(r)
        shutdown_session()
        return roles     
    
def tienePermiso(roles=None,permiso=""):
    """Verifica si en una lista de roles se posee un permiso, tambien verifica si la fase esta cerrada retornando false en caso de ser asi
    Recibe la lista de roles y el permiso que se desea verificar
    """
    posee=False
    permiso=permiso.lower()
    fase=getFaseId(flask.session['faseid'])
    if fase.estado=="Cerrada":
        return False
    if permiso:
        if permiso=="creart":
            for r in roles:
                aux=r.codigoTipo
                if(aux%10==1):
                    posee=True
        elif permiso=="editart":
            for r in roles:
                aux=r.codigoTipo
                if(aux%100>=10):
                    posee=True
        elif permiso=="eliminart":
            for r in roles:
                aux=r.codigoTipo
                if(aux>=100):
                    posee=True
        elif permiso=="crearlb":
            for r in roles:
                aux=r.codigoLB
                if(aux%10==1):
                    posee=True
        elif permiso=="eliminarlb":
            for r in roles:
                aux=r.codigoLB
                if(aux>=10):
                    posee=True
        elif permiso=="creari":
            for r in roles:
                aux=r.codigoItem
                if(aux%10==1):
                    posee=True
        elif permiso=="editari":
            for r in roles:
                aux=r.codigoItem
                if(aux%100>=10):
                    posee=True
        elif permiso=="eliminari":
            for r in roles:
                aux=r.codigoItem
                if(aux%1000>=100):
                    posee=True
        elif permiso=="aprobari":
            for r in roles:
                aux=r.codigoItem
                if(aux%10000>=1000):
                    posee=True
        elif permiso=="reviviri":
            for r in roles:
                aux=r.codigoItem
                if(aux%100000>=10000):
                    posee=True
        elif permiso=="reversionari":
            for r in roles:
                aux=r.codigoItem
                if(aux%1000000>=100000):
                    posee=True
        elif permiso=="asignarpadrei":
            for r in roles:
                aux=r.codigoItem
                if(aux%10000000>=1000000):
                    posee=True
        elif permiso=="asignarantecesori":
            for r in roles:
                aux=r.codigoItem
                if(aux>=10000000):
                    posee=True
    return posee

def getPermisosStringTipoItem(r=None):
    """Devuelve un string representativo de los permisos que posee el rol sobre tipos de items, recibe el rol
    """
    permi=""
    if(r):
        if(r.codigoTipo%10==1):
            permi="Cr"
        if(r.codigoTipo%100>=10):
            permi=permi+" Ed"
        if(r.codigoTipo>=100):
            permi=permi+ " El"
    return permi
def getPermisosStringItem(r=None):
    """Devuelve un string representativo de los permisos que posee el rol sobre items, recibe el rol
    """
    permi=""
    if(r):
        if(r.codigoItem%10==1):
            permi="Cr"
        if(r.codigoItem%100>=10):
            permi=permi+" Ed"
        if(r.codigoItem>=100):
            permi=permi+ " El"
        if(r.codigoItem%1000>=100):
            permi=permi+" Ap"
        if(r.codigoItem%10000>=1000):
            permi=permi+ " Rir"
        if(r.codigoItem%100000>=10000):
            permi=permi+ " Rar"
        if(r.codigoItem%1000000>=100000):
            permi=permi+ " Asp"
        if(r.codigoItem>=10000000):
            permi=permi+ " Asa"
        return permi
def getPermisosStringLB(r=None):
    """Devuelve un string representativo de los permisos que posee el rol sobre lineas base, recibe el rol
    """
    permi=""
    if(r):
        if(r.codigoLB%10==1):
            permi="Cr "
        if(r.codigoLB>=10):
            permi=permi+" El"
    return permi

def getProyectosDeUsuario(idu=None):
    """Devuele una lista de ids de proyectos en los que participa el usuario, recibe el id del usuario
    """
    init_db()
    roles=session.query(Rol).all()
    res=[]
    for r in roles:
        if not comprobarUser_Rol(r.id, idu):
            res.append(getFaseId(r.fase_id).proyecto.id)
    shutdown_session()
    return res

#if __name__=="__main__":

    
        
