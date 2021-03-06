from entidad import Proyecto, Peticion, Voto, LB_Ver, Miembro, ItemPeticion,LineaBase
from initdb import db_session, init_db, shutdown_session
from pms.modelo.proyectoControlador import getProyectoId
from pms.modelo.usuarioControlador import getUsuarios
from pms.modelo.itemControlador import getVersionId, getVersionItem, getItemVerNum
from pms.modelo.relacionControlador import calcularCyD, crearGrafoProyecto, desBloquearAdelante, desBloquear, setEnCambio
from datetime import datetime
from datetime import timedelta
session = db_session()

def getPeticionesVotacion(idp=None):
    """
    Retorna las peticiones en votacion
    """
    init_db()
    res=session.query(Peticion).filter(Peticion.proyecto_id==idp).filter(Peticion.estado=="Votacion").all()
    shutdown_session()
    return res

def getPeticion(id=None):
    """
    Retorna una peticion, recibe el id de la peticion
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
        ultimo=session.query(Peticion).filter(Peticion.proyecto_id==proyecto_id).order_by(Peticion.id.desc()).first()
        if ultimo:
            numero=ultimo.numero+1
        else:
            numero=1
        fechaCreacion=datetime.today()
        l=[]
        for i in items:
            l.append(i.id)
        cd=calcularCyD(l)
        #calcular costo y dificultad y mete en el crear de peticion!!1
        peticion=Peticion(numero,proyecto_id,comentario,"EnEdicion",usuario_id,0,len(items),cd[0],cd[1],fechaCreacion,None,acciones)
        ##------------
        session.add(peticion)
        session.commit()
        peticion=session.query(Peticion).filter(Peticion.proyecto_id==proyecto_id).filter(Peticion.numero==numero).first()
        if peticion:
            for i in items:
                a=agregarItem(i.id,peticion.id)
                 
        shutdown_session()
    
def editarPeticion(idp=None,comentario=None,items=None,acciones=None):
    """
    Permite editar un Peticion existente, recibe el id de la peticion, su comentario, una lista de items y las acciones
    """
    p = getPeticion(idp)
    if comentario:
        p.comentario=comentario
    if acciones:
        p.acciones=acciones
    if items:
        for i in items:
                if(getItemPeticion(i.id)==None):
                    agregarItem(i.id,p.id)
        for i in p.items:
            if not i.item in items:
                quitarItem(i.item.id)
                print "if not in items"
        l=[]
        for i in items:
            l.append(i.id)
        cd=calcularCyD(l)
        p.costoT=cd[0]
        p.dificultadT=cd[1]
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
        quitarItemDeCualquierSolicitud(l.item.id, u.id)
    for l in u.votos:
        quitarVoto(l.user_id,l.peticion_id)
    session.query(Peticion).filter(Peticion.id==u.id).delete()
    session.commit()
    shutdown_session()
def quitarItemDeCualquierSolicitud(idv=None, idp=None):
    """ Quita un item de una solicitud sin importar el estado de sicha solicitud
    """
    if idv and idp:
        init_db()
        v=session.query(ItemPeticion).filter(ItemPeticion.item_id==idv).filter(ItemPeticion.peticion_id==idp).first()
        if v:
            session.query(ItemPeticion).filter(ItemPeticion.item_id==v.item_id).filter(ItemPeticion.peticion_id==v.peticion_id).delete()
        session.commit()
        shutdown_session()
def getItemPeticion(idv=None):
    """Retorna un ItemPeticion de una peticion con estado "EnVotacion" o "Aprobada" de una version de item
    """
    init_db()
    res=session.query(ItemPeticion).filter(ItemPeticion.item_id==idv).filter(ItemPeticion.actual==True).first()
    shutdown_session()
    return res

def comprobarItemPeticion(idv=None):
    """Comprueba que el item no se encuentre en una peticion, retornar False si el item ya esta en una peticion
    """
    res=getItemPeticion(idv)
    if res==None:
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
    if idv and idp:
        ip=ItemPeticion(idp,idv,True)
        init_db()
        session.add(ip)
        session.commit()
        shutdown_session()
        return True
    return False

def quitarItem(idv=None):
    """Quita un Item de una peticion, recibe el id del item
    """ 
    init_db()
    v=getItemPeticion(idv)
    if v:
        session.query(ItemPeticion).filter(ItemPeticion.item_id==v.item_id).filter(ItemPeticion.peticion_id==v.peticion_id).delete()
    else:
        session.query(ItemPeticion).filter(ItemPeticion.item_id==idv).filter(ItemPeticion.actual==True).first()
    session.commit()
    shutdown_session()

def getVoto(idu=None,idp=None):
    """Retorna un voto, recibe el id del usuario y el id de la peticion
    """
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
    """Crea un voto, recibe el id del ususario que vota, el id de la peticion en la que vota y el valor de su voto (True o False)
    """
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
    """Elimina un voto, recibe el id del usuario y el id de la peticion
    """
    soli=getPeticion(idp)
    soli.cantVotos=soli.cantVotos-1
    init_db()
    session.query(Voto).filter(Voto.peticion_id==idp).filter(Voto.user_id==idu).delete()
    session.merge(soli)
    session.commit()
    shutdown_session()
    
def contarVotos(idp=None):
    """Cuentas los votos de una peticion y la rechaza o aprueba, recibe el id de la peticion
    """
    soli=getPeticion(idp)
    votos=0
    for v in soli.votos:
        if v.valor==True:
            votos=votos+1
    init_db()
    c=(soli.cantVotos+1)/2 #cantidad necesaria para aprobar
    if votos>=c:
        soli.estado="Aprobada"
        l=[]
        for i in soli.items:
            l.append(i.item_id)
        
        desBloquearAdelante(l)
        actualizarItemsSolicitud(soli.id)
        for i in soli.items:
            setEnCambio(i.item.id)
    else:
        soli.estado="Rechazada"
        for i in soli.items:
            res=getItemPeticion(i.item.id)
            res.actual=False
            session.merge(res)
    session.merge(soli)
    session.commit()
    shutdown_session()
    
def cambiarVotos(idp=None):
    """
    Cambia a false el campo actual de los votos para que no se tome en cuenta en futuras operaciones
    """
    soli=getPeticion(idp)
    init_db()
    for v in soli.votos:
        v.actual=False
        session.merge(v)
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
    Devuelve un usuario que sea miembro de un poryecto, recive el id del usuario y el proyecto
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
    """Retorna una lista de items que no se encuentran en una peticion en votacion, en edicion o aprobada y que estan en estado Bloqueado o Conflicto
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
                    if (v.estado=="Bloqueado" or v.estado=="Conflicto"):#controlar si se encuentra en una solicitud
                        if comprobarItemPeticion(v.id):
                                aux.append(v)
                                aux.append(False)
                                l.append(aux)
        return l

def opercionHabilitada(s=None, op=None):
    """Retorna True si la solicitud de id s contiene la operacion que se le pasa en op
    """
    if s and op:
        if op=="Editar":
            return s.acciones%10==1
        elif op=="Eliminar":
            return s.acciones%100>=10
        elif op=="Crear Relacion":
            return s.acciones%1000>=100
        elif op=="Eliminar Relacion":
            return s.acciones%10000>=1000
        else:
            return False

def actualizarItemsSolicitud(s=None):
    """
    Actualiza las versiones de los items que se encuentran en la solicitud de id s, recorre los items de la solicitud(que en relidad son las versiones de los items) 
    y revisa que la version que se tiene es la actual del item en cuestion
    """
    if s :
        soli=getPeticion(s)
        for i in soli.items:
            idi=i.item.item.id
            nuevav=getVersionItem(idi)
            if nuevav.id!=i.item.id:
                quitarItem(i.item.id)
                a=agregarItem(nuevav.id, soli.id)
            
def reiniciarVotacion(ids=None):
    """
    Reinicia una votacion, recibe el id de la peticion
    """
    peticion=getPeticion(ids)
    peticion.cantVotos=0
    init_db()
    session.query(Voto).filter(Voto.peticion_id==ids).delete()
    session.commit()
    session.merge(peticion)
    session.commit()
    shutdown_session()
    
def compararPeticion(ids=None):
    """
    Comprueba que el costo y la dificultad de una peticion no hayan sido alterados
    """
    peticion=getPeticion(ids)
    aux=peticion.items
    l=[]
    for a in aux:
        l.append(a.item.id) 
    r=calcularCyD(l)
    if r[0]!=peticion.costoT or r[1]!=peticion.dificultadT:
        reiniciarVotacion(peticion.id)
        return True
    else:
        return False
    
def buscarSolicitud(idv=None):
    """
    Comprubea que la modificacion de un item no altera una solicitud en estado de votacion
    """
    ver=getVersionId(idv)
    itm= ver.item
    fase=itm.tipoitem.fase
    proyecto=fase.proyecto
    grafo=crearGrafoProyecto(proyecto.id)
    cola=[]
    for n in grafo:
        if int(n.version)==int(idv):
            n.marca=True
            cola.append(n)
    for c in cola:
        for s in c.entrantes:
            s.marca=True
            cola.append(s)
            if not comprobarItemPeticion(s.version):
                compararPeticion(getItemPeticion(s.version).peticion_id)

def tSolicitud(ids=None):
    """
    Termina una Solicitud, recibe el id de la solicitud
    """
    soli=getPeticion(ids)
    init_db()
    soli.estado="Terminada"
    session.merge(soli)
    session.commit()
    for i in soli.items:
        i.actual=False
        session.merge(i)
        session.commit()
        ver=i.item
        if ver.estado=="EnCambio":
            ver.estado="Aprobado"
            session.merge(ver)
            session.commit()
        elif ver.estado=="Eliminado":
            it=ver.item
            it.linea_id=None
            session.merge(it)
            session.commit()
    shutdown_session()
    
def getLBPeticion(ids=None):
    """
    Retorna las lineas base que van a ser o estan quebradas como consecuencia de la solicitud, recibe el id de la solicitud
    """
    soli=getPeticion(ids)
    lineas=[]
    if soli.estado=="Terminada" or soli.estado=="Aprobada":
        for i in soli.items:
            v=i.item
            while not v.lalinea:
                v=getItemVerNum(v.item.id,v.version-1)
            init_db()
            l=session.query(LB_Ver).filter(LB_Ver.ver_id==v.id).first()
            shutdown_session()
            lineas.append(l.linea) 
    else: 
        for i in soli.items:
            it=i.item.item
            lineas.append(it.lineabase)
    return lineas   

def getItemsAfectados2(ids=None):
    """
    Retorna un diccionario con todos los items afectados por la solicitud y los relacionados con estos
    """
    soli=getPeticion(ids)
    items={}
    lineas={}
    colaitems=[]
    for i in soli.items:
        v=i.item
        colaitems.append(v)
    
    if soli.estado=="Aprobada" or soli.estado=="Terminada":
        for i in soli.items:
            v=i.item
            while not v.lalinea:
                v=getItemVerNum(v.item.id,v.version-1)
            init_db()
            lv=session.query(LB_Ver).filter(LB_Ver.ver_id==v.id).first()
            ll=session.query(LineaBase).filter(LineaBase.id==lv.lb_id).first()
            lineas[ll.id]=ll
            shutdown_session()
            if not(ll.id in lineas):
                for vaux in ll.vers:
                    vn=getVersionId(vaux.ver_id)
                    colaitems.append(vn)
    for i in colaitems:
        if not(i.id in items):
            items[i.id]=i
            itm=i.item
            if itm.lineabase:
                lb=itm.lineabase
                for n in lb.items:
                    nv=getVersionItem(n.id)
                    colaitems.append(nv)
            for x in i.ante_list:
                if x.ante.actual==True:
                    colaitems.append(x.ante)
            for w in i.post_list:
                if w.post.actual==True:
                    colaitems.append(w.post)
    return items

def getItemsAfectados(ids=None):
    """
    Retorna un diccionario con los items afectados por una solicitud de cambio, recibe el id de la solicitud de cambio
    """
    soli=getPeticion(ids)
    items={}
    lineas={}
    colaitems=[]
    for i in soli.items:
        v=i.item
        colaitems.append(v)
    
    if soli.estado=="Aprobada" or soli.estado=="Terminada":
        for i in soli.items:
            v=i.item
            while not v.lalinea:
                v=getItemVerNum(v.item.id,v.version-1)
            init_db()
            lv=session.query(LB_Ver).filter(LB_Ver.ver_id==v.id).first()
            ll=session.query(LineaBase).filter(LineaBase.id==lv.lb_id).first()
            lineas[ll.id]=ll
            shutdown_session()
            if not(ll.id in lineas):
                for vaux in ll.vers:
                    vn=getVersionId(vaux.ver_id)
                    colaitems.append(vn)
    for i in colaitems:
        if not(i.id in items):
            items[i.id]=i
            itm=i.item
            if itm.lineabase:
                lb=itm.lineabase
                for n in lb.items:
                    nv=getVersionItem(n.id)
                    colaitems.append(nv)
            for w in i.post_list:
                if w.post.actual==True:
                    colaitems.append(w.post)
    return items
                
