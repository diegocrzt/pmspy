import pydot
from entidad import Relacion, Proyecto
from proyectoControlador import getProyectoId
from itemControlador import getVersionItem
import config
from datetime import datetime

def graficarProyecto(idp=None):
    aux=str(datetime.today())
    nombre="grafos/"+aux+".png"
    nombre2="pms/static/grafos/"+aux+".png"
    graph = pydot.Dot(graph_type='digraph',rankdir="LR",size="4")
    proyecto=getProyectoId(idp)
    fases=proyecto.fases
    dibujo={}
    clusterfase={}
    lineas={}
    invisibles={}
    for f in fases:
        clusterfase[f.numero]=pydot.Cluster(str(f.numero),label='Fase '+str(f.numero))
        
    for f in fases:
        node1 = pydot.Node(str(f.numero)+"invi"+"1", color="white",fontcolor="white")
        node2 = pydot.Node(str(f.numero)+"invi"+"2", color="white",fontcolor="white")
        clusterfase[f.numero].add_node(node1)
        clusterfase[f.numero].add_node(node2)
        aa=[node1,node2]
        invisibles[f.numero]=aa
        for t in f.tipos:
            for i in t.instancias:
                g=getVersionItem(i.id) 
                if g.estado!="Eliminado":
                    if g.estado=="Aprobado":
                        color="green"
                    elif g.estado=="Bloqueado":
                        color="#8b8878"
                    elif g.estado=="Conflicto":
                        color="#ff0000"
                    elif g.estado=="Activo":
                        color="#ffff00"
                    elif g.estado=="EnCambio":
                        color="#0000ff"
                    elif g.estado=="Bloqueado":
                        color="#ff1122"
                    else:
                        color="#976856"
                    nodeg = pydot.Node(g.nombre+'\nC='+str(g.costo)+'\nD='+str(g.dificultad), style="filled", fillcolor=color)
                    dibujo[str(f.numero)+g.nombre]=nodeg
                    clusterfase[f.numero].add_node(nodeg)
        
        for l in f.lineas:
            if l.estado!="Quebrada":
                c=0
                aux=""
                for i in l.items:
                    vaux=getVersionItem(i.id)
                    if c==0:
                        aux=aux+"<"+vaux.nombre+"> "
                    else:
                        aux=aux+"|<"+vaux.nombre+"> "
                    c=c+1
                if l.estado=="Abierta":
                    col="red"
                else:
                    col="#8b8878"
                nodel = pydot.Node(str(f.numero)+"lb"+str(l.numero),label = aux,shape="record",color=col)
                clusterfase[f.numero].add_node(nodel)
                lineas[str(f.numero)+"lb"+str(l.numero)]=nodel
        
                        
    
    for f in fases:
        graph.add_subgraph(clusterfase[f.numero])
    for f in fases:
        aa=invisibles[f.numero]
        for t in f.tipos:
            for i in t.instancias:
                v=getVersionItem(i.id) 
                if v.estado!="Eliminado":
                    graph.add_edge(pydot.Edge(aa[0], dibujo[str(f.numero)+v.nombre],color="white",arrowsize="0"))
                    graph.add_edge(pydot.Edge( dibujo[str(f.numero)+v.nombre],aa[1],color="white",arrowsize="0"))
        if f.numero>1:
            a=invisibles[f.numero-1]
            b=invisibles[f.numero]
            graph.add_edge(pydot.Edge(a[1], b[0],color="white",arrowsize="0"))
    
    for f in fases:
        for t in f.tipos:
            for i in t.instancias:
                v=getVersionItem(i.id) 
                if v.estado!="Eliminado":
                    if v.item.lineabase!=None:
                        graph.add_edge(pydot.Edge(dibujo[str(f.numero)+v.nombre], lineas[str(f.numero)+"lb"+str(v.item.lineabase.numero)],headport=v.nombre,style="dotted"))
                    for n in v.post_list:
                        
                        s=n.post
                        if s.actual==True:
                            if n.tipo=="P-H":
                                graph.add_edge(pydot.Edge(dibujo[str(f.numero)+v.nombre], dibujo[str(s.item.tipoitem.fase.numero)+s.nombre]))
                            else:
                                if v.item.lineabase==None:
                                    graph.add_edge(pydot.Edge(dibujo[str(f.numero)+v.nombre], dibujo[str(s.item.tipoitem.fase.numero)+s.nombre],minlen="2"))
                                else:
                                    graph.add_edge(pydot.Edge(lineas[str(f.numero)+"lb"+str(v.item.lineabase.numero)],dibujo[str(s.item.tipoitem.fase.numero)+s.nombre],tailport=v.nombre,minlen="2"))
                
    anterior=None                    
    for f in fases:
        ax=invisibles[f.numero]
        if anterior!=None:
            bx=invisibles[anterior.numero]
            for l in anterior.lineas:
                if l.estado!="Quebrada":
                    graph.add_edge(pydot.Edge(lineas[str(anterior.numero)+"lb"+str(l.numero)], bx[0],color="white",arrowsize="0"))
        for l in f.lineas:
            if l.estado!="Quebrada":
                graph.add_edge(pydot.Edge( ax[1],lineas[str(f.numero)+"lb"+str(l.numero)],color="white",arrowsize="0"))
        anterior=f                            
    graph.write_png(nombre2)
    return nombre