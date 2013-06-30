from entidad import Relacion, Peticion, ItemPeticion
from initdb import db_session, init_db, shutdown_session
from faseControlador import getFaseId, abrirFase
from itemControlador import getVersionId, getVersionItem, editarItem, copiarValores, getItemId
from lineaBaseControlador import getLineaBaseId
from proyectoControlador import getProyectoId
session = db_session()

def getRelacionesCAnte(ante_id=None):
    """
    Devuelve una lista que contenga a la version designada como parametro
    """
    init_db()
    res = session.query(Relacion).filter(Relacion.ante_id==ante_id).all()
    shutdown_session()
    return res

def getRelacion(ante_id=None,post_id=None):
    """
    Devuelve una relacion dados los id del item anterior y el posterior
    """
    init_db()
    res = session.query(Relacion).filter(Relacion.ante_id==ante_id).filter(Relacion.post_id==post_id).all()
    shutdown_session()
    return res

def crearRelacion(ante_id=None,post_id=None,t=None):
    """
    Crea una nueva relacion que tiene como dados los id de el item anterior y el posterior
    """
    ver=getVersionId(ante_id)
    aux=getVersionId(post_id)
    if aux.estado=="Bloqueado":
        return False
    if aux.estado=="Aprobado":
        return False
    itm=ver.item
    tipo=itm.tipoitem
    fase=tipo.fase
    proyecto=fase.proyecto
    if pruebaArista(ante_id,post_id,proyecto.id):
        init_db()
        rel = Relacion(ante_id=ante_id, post_id=post_id,tipo=t)
        session.add(rel)
        session.commit()
        shutdown_session()
        return True
    else:
        return False
    
def eliminarRelacion(ante_id=None,post_id=None):
    """
    Elimina una relacion dados los id de los participantes
    """
    init_db()
    session.query(Relacion).filter(Relacion.ante_id==ante_id).filter(Relacion.post_id==post_id).delete()
    session.commit()
    shutdown_session()

def comprobarRelacion(ante_id=None,post_id=None):
    """
    Comprueba si ya existe una relacion entre dos items
    """
    init_db()
    if int(ante_id) != int(post_id):   
        res = session.query(Relacion).filter(Relacion.ante_id==ante_id).filter(Relacion.post_id==post_id).first()
        if res:
            shutdown_session()
            return True
        else:
            shutdown_session()
            return False
    else:
        shutdown_session()
        return True

class nodo():
    """
    clase utilizada para reperesentar los nodos de un grafo
    """
    def __init__(self, nombre, costo, dificultad,version,estado, item, ver):
        self.entrantes = []
        self.salientes = []
        self.nombre = nombre
        self.costo =costo
        self.dificultad=dificultad
        self.version=version
        self.estado=estado
        self.item=item
        self.ver=ver
        self.marca=False
    def addEntrante(self, nodo):
        self.entrantes.append(nodo)
        nodo.salientes.append(self)
    def addSaliente(self, nodo):
        self.salientes.append(nodo)
        nodo.entrantes.append(self)
    def addBidirec(self, nodo):
        self.salientes.append(nodo)
        self.entrantes.append(nodo)
        nodo.salientes.append(self)
        nodo.entrantes.append(self)

def crearGrafoProyecto(pr=None):
    """
    Crea un grafo que reperesenta los items y sus relaciones dado el id de un proyecto 
    """
    proyecto = getProyectoId(pr)
    grafo=[]
    for fase in proyecto.fases:
        for tipo in fase.tipos:
            for item in tipo.instancias:
                for v in item.version:
                    if v.actual:
                        grafo.append(nodo(v.nombre,v.costo,v.dificultad,v.id,v.estado, v.item, v.version))
    for n in grafo:
        relaciones=getRelacionesCAnte(n.version)
        for r in relaciones:
            for n2 in grafo:
                if n2.version==r.post_id:
                    n.addSaliente(n2)
    return grafo

def buscarCiclo(grafo=None,n1=None,n2=None):
    """
    Detecta si se produce un ciclo en un grafo buscando un camino desde el nodo n1 hasta el n2
    """
    for n in grafo:
        n.marca=False
    listanodos=[]
    listanodos.append(n2)

    for n in listanodos:
        if n==n1:
            return True
        else:
            for vecino in n.salientes:
                if vecino.marca==False:
                    vecino.marca=True
                    listanodos.append(vecino)
                    
    for n in grafo:
        n.marca=False
        
    return False
    
def pruebaArista(idvinicio=None,idvfin=None,proyecto=None):
    """
    Realiza la comprobacion de que la arista a ser insertada no genere un ciclo en el grafo
    """
    grafo=crearGrafoProyecto(proyecto)
    nA=grafo[0]
    nB=grafo[0]
    for n in grafo:
        if int(n.version)==int(idvinicio):
            nA=n
    for n2 in grafo:
        if int(n2.version)==int(idvfin):
            nB=n2
    if buscarCiclo(grafo,nA,nB):
        return False
    else:
        return True
    
def comprobarAprobar(idv=None):
    """
    Comprueba que un item en estado de Revision o Activo pueda ser Aprobado
    """
    ver=getVersionId(idv)
    itm= ver.item
    fase=itm.tipoitem.fase
    proyecto=fase.proyecto
    grafo=[]
    grafo1=crearGrafoProyecto(proyecto.id)
    for g in grafo1:
        grafo.append(g)
    nA=grafo[0]
    cantentrantes=0
    for n in grafo:
        if int(n.version)==int(idv):
            nA=n
    bandera=False
    for n in nA.entrantes:
        cantentrantes=cantentrantes+1
        if n.estado!="Aprobado" and n.estado!="Bloqueado" and n.estado!="Eliminado" :
            return False
        if n.estado=="Aprobado" or n.estado=="Bloqueado":
            bandera=True
    if fase.numero>1 and bandera==False:
        return False
    return True

def copiarRelacionesEstable(idvieja=None,idnueva=None):
    """
    Copia relaciones de una version de un item a otra sin hacer los controles de ciclos por que se asume que las relaciones no causaran ninguna inconcistencia
    """
    init_db()
    res = session.query(Relacion).filter(Relacion.ante_id==idvieja).all()
    for r in res:
        rel = Relacion(ante_id=idnueva, post_id=r.post_id,tipo=r.tipo)
        session.add(rel)
        session.commit()
    res = session.query(Relacion).filter(Relacion.post_id==idvieja).all()
    for r in res:
        rel = Relacion(ante_id=r.ante_id, post_id=idnueva,tipo=r.tipo)
        session.add(rel)
        session.commit()
    shutdown_session()
    
def desAprobarAdelante(idvcambio=None):
    """
    Revierte el estado de todos los items que tengan relacion de dependencia con el item seleccionados a un estado de Revision desde un estado Aprobado
    """
    ver=getVersionId(idvcambio)
    itm= ver.item
    fase=itm.tipoitem.fase
    proyecto=fase.proyecto
    grafo=crearGrafoProyecto(proyecto.id)
    desAprobarAdelanteG(idvcambio,grafo)
    
def desAprobarAdelanteG(idvcambio=None,grafo=None):
    """
    Funcione recursiva que prueba la reversion de estado de un nodo a Revision y  continua con todos sus dependientes
    """
    ver=getVersionId(idvcambio)
    nA=grafo[0]
    for n in grafo:
        if int(n.version)==int(idvcambio):
            nA=n
    for n in nA.salientes:
        if n.estado=="Aprobado":
            desAprobar(n.version)
            desAprobarAdelanteG(n.version,grafo)
            
    
def desAprobar(idv=None):
    """
    Revierte el estado de un item de Aprobado a Revision
    """
    init_db()
    ver=getVersionId(idv)
    ver.estado="Revision"
    session.merge(ver)
    session.commit()
    shutdown_session()
    
def hijos(vid=None):
    ver=getVersionId(vid)
    itm= ver.item
    fase=itm.tipoitem.fase
    proyecto=fase.proyecto
    grafo=crearGrafoProyecto(proyecto.id)
    nA=grafo[0]
    for n in grafo:
        if int(n.version)==int(vid):
            nA=n
    aux=[]
    aux=hijosRecursivo(nA, grafo)
    return aux

def hijosRecursivo(nA, grafo):
    l=[]
    for n in nA.salientes:
        aux=hijosRecursivo(n,grafo)
        for e in aux:
            l.append(e)
    l.append(nA)
    return l

def calcularCyD(listaItems):
    """
    recibe una lista de los id de la version de los items, aunque sea solo uno que sea iterable de alguna forma
    """
    ver=getVersionId(listaItems[0])
    itm= ver.item
    fase=itm.tipoitem.fase
    proyecto=fase.proyecto
    grafo=crearGrafoProyecto(proyecto.id)
    cola=[]
    for n in grafo:
        for l in listaItems:
            if int(n.version)==int(l):
                cola.append(n)
                n.marca=True
    costo=0
    dificultad=0
    for c in cola:
        costo=costo+c.costo
        dificultad=dificultad+c.dificultad
        for nex in c.salientes:
            if nex.marca==False:
                cola.append(nex)
                nex.marca=True
    res=[]
    res.append(costo)
    res.append(dificultad)
    return res

def romperLB(idv):
    ver=getVersionId(idv)
    if ver.estado=="Bloqueado":
        itm=ver.item
        lb=itm.lineabase
        if lb.estado=="Cerrada":
            lb.estado="Quebrada"
            init_db()
            session.merge(lb)
            session.commit()
            shutdown_session()
            for i in lb.items:
                iv=getVersionItem(i.id)
                editarItem(i.id,iv.nombre,"Aprobado",iv.costo,iv.dificultad,iv.usuario_modificador_id)
                version=getVersionItem(i.id)
                copiarValores(iv.id,version.id)
                copiarRelacionesEstable(iv.id,version.id)
            return True
        else:
            return False
    else:
        return False
    

def desBloquearAdelante(lista=None):
    """
    Revierte el estado de todos los items que tengan relacion de dependencia con el item seleccionados a un estado de Revision desde un estado Aprobado
    """
    idvcambio=lista[0]
    ver=getVersionId(idvcambio)
    itm= ver.item
    fase=itm.tipoitem.fase
    proyecto=fase.proyecto
    grafo=crearGrafoProyecto(proyecto.id)
    for l in lista:
        romperLB(l)
    for l in lista:
        setEnCambio(l)
    for l in lista:
        desBloquearAdelanteG(l,grafo)
def desBloquearAdelante2(lista=None):
    """
    Revierte el estado de todos los items que tengan relacion de dependencia con el item seleccionados a un estado de Revision desde un estado Aprobado
    """
    
    idvcambio=lista[0]
    ver=getVersionId(idvcambio)
    itm= ver.item
    fase=itm.tipoitem.fase
    proyecto=fase.proyecto
    grafo=crearGrafoProyecto(proyecto.id)
    for l in lista:
        desBloquear(l)
    for l in lista:
        desBloquearAdelanteG(l,grafo)
    
def desBloquearAdelanteG(idvcambio=None,grafo=None):
    """
    Funcione recursiva que prueba la reversion de estado de un nodo a Revision y  continua con todos sus dependientes
    """
    ver=getVersionId(idvcambio)
    if ver.item.lineabase!=None:
        print ver.nombre 
        if ver.item.lineabase.estado=="Cerrada":
            abrirLB(ver.item.lineabase.id)
        if ver.item.tipoitem.fase.estado!="Abierta":
            abrirFase(ver.item.tipoitem.fase.id)
    nA=grafo[0]
    for n in grafo:
        if int(n.version)==int(idvcambio):
            nA=n
    for n in nA.salientes:
        if n.estado=="Bloqueado": 
            desBloquear(n.version)
            desBloquearAdelanteG(n.version,grafo)
        elif n.estado=="Aprobado":
            desBloquearAdelanteG(n.version,grafo)
            
    
def desBloquear(idv=None):
    """
    Revierte el estado de un item de Aprobado a Revision
    """
    ver=getVersionId(idv)
    if ver.estado=="Bloqueado":
        init_db()
        ver.estado="Conflicto"
        session.merge(ver)
        session.commit()
        shutdown_session()
    
def setEnCambio(idv=None):
    """
    Revierte el estado de un item de Aprobado a Revision
    """
    init_db()
    ver=getVersionId(idv)
    ver.estado="EnCambio"
    session.merge(ver)
    session.commit()
    shutdown_session()
    
def abrirLB(idlb=None):
    linea=getLineaBaseId(idlb)
    init_db()
    linea.estado="Abierta"
    session.merge(linea)
    session.commit()
    shutdown_session()
    l=[]
    bandera=False
    for i in linea.items:
        v=getVersionItem(i.id)
        if v.estado=="Bloqueado":
            bandera=True
            l.append(v.id)
    if bandera==True:
        desBloquearAdelante2(l)
        
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
                return True
        return False
    
def getPeticion(id=None):
    """
    Retorna una peticion, recibe el id de la peticion
    """
    init_db()
    res=session.query(Peticion).filter(Peticion.id==id).first()
    shutdown_session()
    return res

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
    
def getItemPeticion(idv=None):
    """Retorna un ItemPeticion de una peticion con estado "EnVotacion" o "Aprobada" de una version de item
    """
    init_db()
    res=session.query(ItemPeticion).filter(ItemPeticion.item_id==idv).filter(ItemPeticion.actual==True).first()
    shutdown_session()
    return res