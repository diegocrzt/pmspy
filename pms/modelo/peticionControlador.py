from entidad import Proyecto, Peticion, Voto, Usuario, Item, VersionItem, Miembro
from initdb import db_session, init_db, shutdown_session
from pms.modelo.proyectoControlador import getProyectoId
from pms.modelo.usuarioControlador import getUsuarios
from pms.modelo.itemControlador import getVersionId, getVersionItem
from datetime import datetime
session = db_session()



def getPeticion(id=None):
    """
    recupera un usuario por su nombre de usuario
    """
    init_db()
    res=session.query(Peticion).filter(Peticion.id==id).first()
    shutdown_session()
    return res


#def crearPeticion(numero,proyecto_id,comentario,estado,usuario_id,cantVotos,cantItems,costoT,dificultadT,fechaCreacion,fechaEnvio):    
def crearPeticion(proyecto_id=None,comentario=None,usuario_id=None, items=None, acciones=None):
    """
    Crea una Peticion, recibe el id del proyecto, el id de la version del item sobre el cual se solicita la peticion, un comentario y el id del usuario que solicita la peticioin
    """
    if proyecto_id and comentario and usuario_id and items and acciones:
        init_db()
        ultimo=session.query(Peticion).order_by(Peticion.id.desc()).first()
        if ultimo:
            numero=ultimo.numero+1
        else:
            numero=1
        fechaCreacion=datetime.today()
        #calcular costo y dificultad
        peticion=Peticion(numero,proyecto_id,comentario,"EnEdicion",usuario_id,0,len(items),120,120,fechaCreacion,None,acciones)
        session.add(peticion)
        session.commit()
        peticion=session.query(Peticion).filter(Peticion.proyecto_id==proyecto_id).filter(Peticion.numero==numero).first()
        if peticion:
            print "---------------------------------------------"
            for i in items:
                a=agregarItem(i.id,peticion.id)
                 
        shutdown_session()
    
def editarPeticion(idp=None,comentario=None,items=None,acciones=None):
    """
    Permite editar un Peticion existente
    """
    p = getPeticion(idp)
    if comentario:
        p.comentario=comentario
    if acciones:
        p.acciones=acciones
    if items:
        for i in items:
            if comprobarItemPeticion(i.id):
                agregarItem(i.id,p.id)
        for i in p.items:
            if not i in items:
                quitarItem(i.id,p.id)
    p.cantItems=len(p.items)
    init_db()
    session.merge(p)
    session.commit()
    shutdown_session()
    
def eliminarPeticion(idp=None):
    """Elimina una Peticion, recibe el id de la peticion
    """
    init_db()
    u=getPeticion(idp)
    for l in u.items:
        quitarItem(l.id)
    for l in u.votos:
        quitarVoto(l.user_id,l.peticion_id)
    session.query(Peticion).filter(Peticion.id==u.id).delete()
    session.commit()
    shutdown_session()
    
def comprobarItemPeticion(idv=None):
    """Comprueba que el item no se encuentre en una peticion, retornar False si el item ya esta en una peticion
    """
    res=getVersionId(idv)
    if res.peticion_id==None:
        return True
    else:
        return False
def enviarPeticion(idp=None):
    """Envia una Peticion, recibe el id de la peticion, cambia el estado de la peticion a EnVotacion 
    """
    if idp:
        p = getPeticion(idp)
        init_db()
        p.estado="EnVotacion"
        p.fechaEnvio=datetime.today()
        session.merge(p)
        session.commit()
        shutdown_session()
        
def agregarItem(idv=None,idp=None,):
    """Agrega un Item a una peticion, recibe el id del item y de la peticion
    """
    r=comprobarItemPeticion(idv)
    if r==True:
       
        v=getVersionId(idv)
        init_db()
        v.peticion_id=idp
        session.merge(v)
        session.commit()
        shutdown_session()
        return True
    else:
        return False
    
def quitarItem(idv=None):
    """Quita un Item de una peticion, recibe el id del item
    """
    init_db()
    v=getVersionId(idv)
    v.peticion_id=None
    session.merge(v)
    session.commit()
    shutdown_session()

def getVoto(idu=None,idp=None):
    init_db()
    res=session.query(Voto).filter(Voto.user_id==idu).filter(Voto.peticion_id==idp).first()
    shutdown_session()
    return res

def comprobarVoto(idu=None,idp=None):
    """Comprueba que el usuario no haya votado aun en la solicitud, recibe el id del usuario y el id de la solicitud
    """
    res=getVoto(idu,idp)
    if res==None:
        return True
    else:
        return False

def agregarVoto(idu=None, idp=None,valor=None):
    if comprobarVoto(idu,idp):
        soli=getPeticion(idp)
        init_db()
        soli.cantVotos=soli.cantVotos+1
        v=Voto(idp,idu,valor)
        session.add(v)
        session.merge(soli)
        session.commit()
        shutdown_session()
        return True
    else:
        return False
    
def quitarVoto(idu=None,idp=None):
    soli=getPeticion(idp)
    soli.cantVotos=soli.cantVotos-1
    init_db()
    session.query(Voto).filter(Voto.peticion_id==idp).filter(Voto.user_id==idu).delete()
    session.merge(soli)
    session.commit()
    shutdown_session()
    
def contarVotos(idp=None):
    soli=getPeticion(idp)
    votos=0
    for v in soli.votos:
        if v.valor==True:
            votos=votos+1
    init_db()
    c=(soli.cantVotos+1)/2 #cantidad necesaria para aprobar
    print c
    if votos>=c:
        soli.estado="Aprobada"
    else:
        soli.estado="Rechazada"
    session.merge(soli)
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
    
def getVersionesItemParaSolicitud(idpro=None):
    """Retorna una lista de items que no es encuentran en una peticion y que estan en estado Bloqueado o Conflicto
    """
    if idpro:
        l=[]
        pro=getProyectoId(idpro)
        fases=pro.fases
        for f in fases:
            for t in f.tipos:
                for i in t.instancias:
                    v=getVersionItem(i.id)
                    aux=[]
                    if comprobarItemPeticion(v.id) and (v.estado=="Bloqueado" or v.estado=="Conflicto"):#controlar si se encuentra en una solicitud
                        aux.append(v)
                        aux.append(False)
                        l.append(aux)
        return l
        
  
    
