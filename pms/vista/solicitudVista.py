import flask.views
from flask import request
from pms.modelo.entidad import VersionItem
from pms.modelo.usuarioControlador import  getUsuarioById
from pms.modelo.proyectoControlador import getProyectoId
from pms.modelo.peticionControlador import getMiembro, contarVotos, getMiembros, agregarVoto, enviarPeticion, crearPeticion, getPeticion, eliminarPeticion, editarPeticion, getVersionesItemParaSolicitud, cambiarVotos, tSolicitud, getPeticionesVotacion
from datetime import datetime
from pms.modelo.relacionControlador import hijos
import pms.vista.required
from pms import app
from pms.vista.paginar import calculoDeSiguiente, calculoDeAnterior, calculoPrimeraPag
TAM_PAGINA=5


class AdmSolicitud(flask.views.MethodView):
    """
    Gestiona y Ejecuta la Vista de Administrar Solicitudes
    """
    @pms.vista.required.login_required
    def get(self):
        """
        Ejecuta el template admSolicitud.html
        """
        global TAM_PAGINA
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        
        if getMiembro(flask.session['proyectoid'],flask.session['usuarioid']):
            p=getProyectoId(flask.session['proyectoid'])
            ls=p.solicitudes
        else:
            ls=getUsuarioById(flask.session['usuarioid']).peticiones
        return flask.render_template('admSolicitud.html',solicitudes=ls, infopag="Pagina 1 de 1", buscar=False)
   
        
class Crearsolicitud(flask.views.MethodView):
    """
    Vista de Crear Solicitud
    """
    iversiones=[]
    def getItemsSolicitud(self):
        """Carga el atributo iversiones con las versiones de los items sobre los que se puede realizar una solicitud
        """
        self.iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
        
        
    @pms.vista.required.login_required
    def get(self):
        """
        Devuelve la vista de crear solicitud, llama a crearSolicitud.html, responde al boton Crear Solicitud de admSolicitud
        """
        acciones=[]
        acciones.insert(0, ["Editar",True])
        acciones.insert(1,["Eliminar",False])
        acciones.insert(2,["Crear Relacion",False])
        acciones.insert(3,["Eliminar Relacion",False])
        self.getItemsSolicitud()
        return flask.render_template('crearSolicitud.html', versiones=self.iversiones, acciones=acciones)
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Crear Solicitud
        """
        self.getItemsSolicitud()
        ag=[]#lista items para pasarle a la funcion que crea la solicitud
        items=[]
        for u in self.iversiones:
            aux=[]
            aux.append(u[0])
            if u[0].nombre in flask.request.form:
                check=True
                ag.append(u[0])
            else:
                check=False
            aux.append(check)
            items.append(aux)
                
        acc=0#lista de acciones para pasarle a la funcion que crea la solicitud
        acciones=[]
        aux=[]
        aux.append("Editar")
        if "Editar"in flask.request.form:
            acc=1
            aux.append(True)
        else:
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Eliminar")
        if "Eliminar" in flask.request.form:
            acc=acc+10
            aux.append(True)
        else:
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Crear Relacion")
        if "Crear Relacion" in flask.request.form:
            acc=acc+100
            aux.append(True)
        else:
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Eliminar Relacion")
        if "Eliminar Relacion" in flask.request.form:
            acc=acc+1000
            aux.append(True)
        else:
            aux.append(False)
        acciones.append(aux)
        
        error=False
        if len(ag)==0:
            flask.flash(u"Debe seleccionar al menos un Item", "item")
            error=True
        if acc==0:
            flask.flash(u"Debe seleccionar al menos una Accion", "accion")
            error=True
        if flask.request.form['comentario']=="":
            flask.flash(u"El campo no puede estar vacio","comentario")
            error=True
        if error:
            return flask.render_template('crearSolicitud.html', versiones=items, acciones=acciones)
        crearPeticion(flask.session['proyectoid'],flask.request.form['comentario'],flask.session['usuarioid'],ag,acc )
        
        flask.flash(u"CREACION EXITOSA","text-success")
        return flask.redirect(flask.url_for('admsolicitud'))
    
class EditarSolicitud(flask.views.MethodView):
    """
    Gestiona la Vista de Editar Tipo de Item
    """
    @pms.vista.required.login_required
    def get(self):
        """
        Esta funcion solo evita errores de url no encontrado para el caso en que se introduzca el url /admsolicitud/editar/
        el cual no devuelve ningun resultado, para ello se redirecciona a la vista de Solicitudes de Cambio
        """
        return flask.redirect('/admsolicitud/'+str(flask.session['proyectoid'])) 

    @pms.vista.required.login_required
    def post(self):
        """
        Funcion que ejecuta la edicion del la solicitud
        """
        iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
        soli=getPeticion(flask.session['solicitudid'])
        ag=[]#lista items para pasarle a la funcion que crea la solicitud
        items=[]
        for i in soli.items:
            iversiones.append([i.item,True])
        for u in iversiones: 
            aux=[]
            aux.append(u[0])
            if u[0].nombre in flask.request.form:
                check=True
                ag.append(u[0])
            else:
                check=False
            aux.append(check)
            items.append(aux)
        acc=0#lista de acciones para pasarle a la funcion que crea la solicitud
        acciones=[]
        aux=[]
        aux.append("Editar")
        if "Editar"in flask.request.form:
            acc=1
            aux.append(True)
        else:
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Eliminar")
        if "Eliminar" in flask.request.form:
            acc=acc+10
            aux.append(True)
        else:
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Crear Relacion")
        if "Crear Relacion" in flask.request.form:
            acc=acc+100
            aux.append(True)
        else:
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Eliminar Relacion")
        if "Eliminar Relacion" in flask.request.form:
            acc=acc+1000
            aux.append(True)
        else:
            aux.append(False)
        acciones.append(aux)
        
        error=False
        if len(ag)==0:
            flask.flash(u"Debe seleccionar al menos un Item", "item")
            error=True
        if acc==0:
            flask.flash(u"Debe seleccionar al menos una Accion", "accion")
            error=True
        if flask.request.form['comentario']=="":
            flask.flash(u"El campo no puede estar vacio","comentario")
            error=True
        if error:
            return flask.render_template('editarSolicitud.html', s=soli, versiones=items, acciones=acciones)
        editarPeticion(flask.session['solicitudid'],flask.request.form['comentario'][:100], ag, acc)
        flask.flash(u"EDICION EXITOSA","text-success")
        return flask.redirect(flask.url_for('admsolicitud'))

class EliminarSolicitud(flask.views.MethodView):
    """
    Gestiona la Vista de Eliminar Solicitud
    """
    @pms.vista.required.login_required
    def get(self):
        """Esta funcion solo evita errores de url no encontrado para el caso en que se introduzca el url /admsolicitud/eliminar/
        el cual no devuelve ningun resultado, para ello se redirecciona a la vista de Solicitudes de Cambio"""
        return flask.redirect('/admsolicitud/'+str(flask.session['proyectoid'])) 

    @pms.vista.required.login_required
    def post(self):
        """
        Funcion que ejecuta la eliminacion de la solicitud
        """
        eliminarPeticion(flask.session['solicitudid'])
        flask.flash(u"ELIMINACION EXITOSA","text-success")
        return flask.redirect(flask.url_for('admsolicitud'))
        
@app.route('/admsolicitud/editar/<s>')
@pms.vista.required.login_required       
def edSolicitud(s=None): 
    """
    Funcion que llama a la Vista de Editar Solicitud responde al boton de 'Editar' de Administrar Solicitud
    recibe el de la solicitud a editarse
    """
    #soli=getSolicitud(s)
    flask.session['solicitudid']=s
    
    soli=getPeticion(s)
    acc=[]
    acc.insert(0, ["Editar",soli.acciones%10==1])
    acc.insert(1,["Eliminar",soli.acciones%100>=10])
    acc.insert(2,["Crear Relacion",soli.acciones%1000>=100])
    acc.insert(3,["Eliminar Relacion",soli.acciones%10000>=1000])
    iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
    l=[]
    c=0
    for i in iversiones:
        l.insert(c,[i[0],False])
        c=c+1
    for i in soli.items:
        l.insert(c, [i.item,True])
        c=c+1
     
    return flask.render_template('editarSolicitud.html',s=soli, versiones=l,acciones=acc) 

@app.route('/admsolicitud/eliminar/<s>')
@pms.vista.required.login_required       
def eSolicitud(s=None): 
    """
    Funcion que despliega la Vista de Eliminar Solicitud, llama a eliminarSolicitud.html 
    responde al boton de 'Eliminar' de Administrar Solicitud
    recibe el id de la Solicitud a eliminarce
    """
    
    soli=getPeticion(s)
    acc=[]
    acc.insert(0, ["Editar",soli.acciones%10==1])
    acc.insert(1,["Eliminar",soli.acciones%100>=10])
    acc.insert(2,["Crear Relacion",soli.acciones%1000>=100])
    acc.insert(3,["Eliminar Relacion",soli.acciones%10000>=1000])
    
    flask.session['solicitudid']=s
    return flask.render_template('eliminarSolicitud.html',s=soli, acciones=acc)

@app.route('/admsolicitud/consultar/<s>')
@pms.vista.required.login_required
def consultarSolicitud(s=None):
    """
    Funcion que despliega pagina de consulta de Solicitud llama a consultarSolicitud.html
    responde al boton de 'Consultar' de Administrar Solicitud
    recibe el id de la solicitud a consultar
    """
    soli=getPeticion(s)
    acc=[]
    acc.insert(0, ["Editar",soli.acciones%10==1])
    acc.insert(1,["Eliminar",soli.acciones%100>=10])
    acc.insert(2,["Crear Relacion",soli.acciones%1000>=100])
    acc.insert(3,["Eliminar Relacion",soli.acciones%10000>=1000])
    p=getProyectoId(flask.session['proyectoid'])
    if soli.cantVotos==0 or soli.estado=="EnVotacion":
        miembros=p.miembros
        m=[]
        for mi in miembros:
            vot=False
            for v in soli.votos:
                if v.user_id==mi.user_id:
                    m.append([v.usuario,True])
                    vot=True
            if not vot:
                m.append([getUsuarioById(mi.user_id),False])
    else:
        m=[]
        for v in soli.votos:
            m.append(v.usuario,v.valor)
    for a in m:
        print a[0].nombre
    h=[]
    for i in soli.items:
        hi=hijos(i.item.id)
        for item in hi:
            h.append(item)
    h.sort(cmp=numeric_compare, key=None, reverse=False)
    
    return flask.render_template('consultarSolicitud.html', s=soli, acciones=acc, consultar=True, miembros=m, arbol=h)

@app.route('/admsolicitud/enviar/<s>',methods=['POST', 'GET'])
@pms.vista.required.login_required
def enviarSolicitud(s=None):
    """
    Funcion que despliega pagina de enviar Solicitud llama a consultarSolicitud.html
    responde al boton de 'Enviar' de Administrar Solicitud
    recibe el id de la solicitud a enviar
    """
    if request.method == "GET":
        flask.session['solicitudid']=s
        soli=getPeticion(s)
        acc=[]
        acc.insert(0, ["Editar",soli.acciones%10==1])
        acc.insert(1,["Eliminar",soli.acciones%100>=10])
        acc.insert(2,["Crear Relacion",soli.acciones%1000>=100])
        acc.insert(3,["Eliminar Relacion",soli.acciones%10000>=1000])
        h=[]
        for i in soli.items:
            hi=hijos(i.item.id)
            for item in hi:
                h.append(item)
        h.sort(cmp=numeric_compare, key=None, reverse=False)
        return flask.render_template('consultarSolicitud.html', s=soli, acciones=acc, consultar=False, arbol=h)
    if request.method == "POST":
        enviarPeticion(flask.session['solicitudid'])
        flask.flash(u"ENVIO EXITOSO","text-success")
        return flask.redirect(flask.url_for('admsolicitud'))
    
@app.route('/admsolicitud/votar/<s>',methods=['POST', 'GET'])
@pms.vista.required.login_required
def votarEnSoliciutud(s=None):
    """Funcion que gestion la vista de votar y ejecuta la funcion de votar en solicitud, recibe el id de la solicitud, responde al boton de votar en admSolicitud
    """
    if request.method == "GET":
        flask.session['solicitudid']=s
        soli=getPeticion(s)
        acc=[]
        if soli.acciones%10==1:
            acc.append("Editar")
        if soli.acciones%100>=10:
            acc.append("Eliminar")
        if soli.acciones%1000>=100:
            acc.append("Crear Relacion")
        if soli.acciones%10000>=1000:
            acc.append("Eliminar Relacion")
        p=getProyectoId(flask.session['proyectoid'])
        miembros=p.miembros
        m=[]
        
        for mi in miembros:
            vot=False
            for v in soli.votos:
                if v.user_id==mi.user_id:
                    m.append([getUsuarioById(mi.user_id),True])
                    vot=True
            if not vot:
                m.append([getUsuarioById(mi.user_id),False])
        for a in m:
            print a[0].nombre
        h=[]
        for i in soli.items:
            hi=hijos(i.item.id)
            for item in hi:
                h.append(item)
        h.sort(cmp=numeric_compare, key=None, reverse=False)
        #sorted(h, key=lambda VersionItem: VersionItem.item.tipoitem.fase.numero , reverse=True)
        return flask.render_template('votarSolicitud.html', s=soli, acciones=acc, miembros=m, arbol=h)
    if request.method == "POST":
        voto=None
        if "Aprobar" in flask.request.form:
            voto=True
        if "Rechazar" in flask.request.form:
            voto=False
         
        agregarVoto(flask.session['usuarioid'],s,voto)
        cantidadm= len(getMiembros(flask.session['proyectoid']))
        soli=getPeticion(s)
        if soli.cantVotos>=cantidadm:
            contarVotos(soli.id)
        
        flask.flash(u"VOTACION EXITOSA","text-success")
        return flask.redirect(flask.url_for('admsolicitud'))
        
@app.route('/admsolicitud/terminar/<s>',methods=['POST', 'GET'])
@pms.vista.required.login_required
def terminarSolicitud(s=None):
    """
    Funcion que gestiona la vista de Terminar Solicitud, recibe el id de la solicitud, responde al boton Terminar de admEjecutarSolicitud
    """
    if request.method == "GET":
        flask.session['solicitudid']=s
        soli=getPeticion(s)
        proyecto=soli.proyecto
        fases=proyecto.fases
        soli=getPeticion(s)
        acc=[]
        acc.insert(0, ["Editar",soli.acciones%10==1])
        acc.insert(1,["Eliminar",soli.acciones%100>=10])
        acc.insert(2,["Crear Relacion",soli.acciones%1000>=100])
        acc.insert(3,["Eliminar Relacion",soli.acciones%10000>=1000])
        return flask.render_template('terminarSolicitud.html', s=soli, fases=fases, acciones=acc)
        
    if request.method == "POST":
        if "Aceptar" in flask.request.form:
            tSolicitud(flask.session['solicitudid'])
            flask.flash(u"Solicitud Termianda","text-success")
            return flask.redirect(flask.url_for('admsolicitud'))
        else:
            return flask.redirect(flask.url_for('admsolicitud'))
        
def numeric_compare(x, y):
        a=x.item.tipoitem.fase.numero
        b=y.item.tipoitem.fase.numero
        return  a-b