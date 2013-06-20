import flask.views
from flask import request
from pms.modelo.usuarioControlador import  getUsuarioById
from pms.modelo.proyectoControlador import getProyectosFiltrados, getProyectosPaginados, getCantProyectos, comprobarProyecto, crearProyecto, getProyectos, eliminarProyecto, getProyectoId, inicializarProyecto, getProyecto
from pms.modelo.peticionControlador import getMiembro, contarVotos, getMiembros, agregarVoto, enviarPeticion, crearPeticion, getPeticion, eliminarPeticion, editarPeticion, getVersionesItemParaSolicitud, cambiarVotos, tSolicitud, getPeticionesVotacion
from datetime import datetime
import pms.vista.required
from pms.modelo.rolControlador import getProyectosDeUsuario
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
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta el template admSolicitud.html
        """
        if flask.request.form['fil']!="":
            infopag=""
            if 'buscar' in flask.request.form:
                flask.session['pagina']=1
                p=getProyectosPaginados(flask.session['pagina']-1,TAM_PAGINA, flask.request.form['fil'])
                flask.session['filtro']=flask.request.form['fil']
                if(p!=None):#Si devolvio algo
                    infopag=calculoPrimeraPag(getProyectosFiltrados(flask.session['filtro']).count())
            if 'sgte' in flask.request.form:
                infopag=calculoDeSiguiente(getCantProyectos(flask.session['filtro']))
                p=getProyectosPaginados(flask.session['pagina']-1,TAM_PAGINA, flask.session['filtro'])
            if 'anterior' in flask.request.form:
                infopag=calculoDeAnterior(getCantProyectos(flask.session['filtro']))
                p=getProyectosPaginados(flask.session['pagina']-1,TAM_PAGINA, flask.session['filtro'])
                    
            return flask.render_template('admProyecto.html',proyectos=p,infopag=infopag,buscar=True)
        else:
            return flask.redirect(flask.url_for('admproyecto'))
        
class Crearsolicitud(flask.views.MethodView):
    """
    Vista de Crear Solicitud
    """
    iversiones=[]
    def getItemsSolicitud(self):
        self.iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
        
        
    @pms.vista.required.login_required
    def get(self):
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
        return flask.redirect('/admsolicitud/'+str(flask.session['proyectoid'])) 

    @pms.vista.required.login_required
    def post(self):
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
    Gestiona la Vista de Editar Tipo de Item
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect('/admsolicitud/'+str(flask.session['proyectoid'])) 

    @pms.vista.required.login_required
    def post(self):
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
    return flask.render_template('consultarSolicitud.html', s=soli, acciones=acc, consultar=True)

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
        return flask.render_template('consultarSolicitud.html', s=soli, acciones=acc, consultar=False)
    if request.method == "POST":
        enviarPeticion(flask.session['solicitudid'])
        flask.flash(u"ENVIO EXITOSO","text-success")
        return flask.redirect(flask.url_for('admsolicitud'))
    
@app.route('/admsolicitud/votar/<s>',methods=['POST', 'GET'])
@pms.vista.required.login_required
def votarEnSoliciutud(s=None):
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
        return flask.render_template('votarSolicitud.html', s=soli, acciones=acc)
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
    if request.method == "GET":
        flask.session['solicitudid']=s
        soli=getPeticion(s)
        proyecto=soli.proyecto
        fases=proyecto.fases
        return flask.render_template('terminarSolicitud.html', s=soli, fases=fases)
        
    if request.method == "POST":
        if "Aceptar" in flask.request.form:
            tSolicitud(flask.session['solicitudid'])
            flask.flash(u"Solicitud Termianda","text-success")
            return flask.redirect(flask.url_for('admsolicitud'))
        else:
            return flask.redirect(flask.url_for('admsolicitud'))
