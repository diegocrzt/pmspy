from entidad import Relacion
from initdb import db_session, init_db, shutdown_session
from faseControlador import getFaseId
from itemControlador import getVersionId
from proyectoControlador import getProyectoId
session = db_session()

def getRelacionesCAnte(ante_id=None):
    init_db()
    res = session.query(Relacion).filter(Relacion.ante_id==ante_id).all()
    shutdown_session()
    return res

def getRelacion(ante_id=None,post_id=None):
    init_db()
    res = session.query(Relacion).filter(Relacion.ante_id==ante_id).filter(Relacion.post_id==post_id).all()
    shutdown_session()
    return res

def crearRelacion(ante_id=None,post_id=None,t=None):
    
    ver=getVersionId(ante_id)
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
    init_db()
    session.query(Relacion).filter(Relacion.ante_id==ante_id).filter(Relacion.post_id==post_id).delete()
    session.commit()
    shutdown_session()

def comprobarRelacion(ante_id=None,post_id=None):
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
    def __init__(self, etiqueta, costo, dificultad,version,estado):
        self.entrantes = []
        self.salientes = []
        self.etiqueta = etiqueta
        self.costo =costo
        self.dificultad=dificultad
        self.version=version
        self.estado=estado
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
    proyecto = getProyectoId(pr)
    grafo=[]
    for fase in proyecto.fases:
        for tipo in fase.tipos:
            for item in tipo.instancias:
                for v in item.version:
                    if v.actual:
                        grafo.append(nodo(v.nombre,v.costo,v.dificultad,v.id,v.estado))
    for n in grafo:
        relaciones=getRelacionesCAnte(n.version)
        for r in relaciones:
            for n2 in grafo:
                if n2.version==r.post_id:
                    n.addSaliente(n2)
    return grafo

def buscarCiclo(grafo=None,n1=None,n2=None):
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
    grafo=crearGrafoProyecto(proyecto)
    nA=grafo[1]
    nB=grafo[1]
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
    for n in nA.entrantes:
        cantentrantes=cantentrantes+1
        if n.estado!="Aprobado" and n.estado!="Bloqueado":
            return False
    if fase.numero>1 and cantentrantes==0:
        return False
    return True

def copiarRelacionesEstable(idvieja=None,idnueva=None):
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
    ver=getVersionId(idvcambio)
    itm= ver.item
    fase=itm.tipoitem.fase
    proyecto=fase.proyecto
    grafo=crearGrafoProyecto(proyecto.id)
    desAprobarAdelanteG(idvcambio,grafo)
    
def desAprobarAdelanteG(idvcambio=None,grafo=None):
    ver=getVersionId(idvcambio)
    nA=grafo[0]
    for n in grafo:
        if int(n.version)==int(idvcambio):
            nA=n
    for n in nA.salientes:
        if n.estado=="Aprobado" or n.estado=="Bloqueado":
            desAprobar(n.version)
            desAprobarAdelanteG(n.version,grafo)
            
    
def desAprobar(idv=None):
    init_db()
    ver=getVersionId(idv)
    ver.estado="Revision"
    session.merge(ver)
    session.commit()
    shutdown_session()