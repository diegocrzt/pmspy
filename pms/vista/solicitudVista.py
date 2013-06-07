import flask.views
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, getUsuarioById, editarUsuario, comprobarUsuario, usuarioIsLider
from pms.modelo.proyectoControlador import getProyectosFiltrados, getProyectosPaginados, getCantProyectos, comprobarProyecto, crearProyecto, getProyectos, eliminarProyecto, getProyectoId, inicializarProyecto, getProyecto
from pms.modelo.peticionControlador import crearPeticion
from pms.modelo.itemControlador import getVersionesItemParaSolicitud
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
        
        
        #ls=getSolicitudes(flask.session['proyectoid'])
        l=[1,2,3]
        return flask.render_template('admSolicitud.html',solicitudes=l, infopag="1 de 1", buscar=False)
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
    acciones=[]
    def getItemsSolicitud(self):
        self.iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
        self.acciones=[]
        aux=[]
        aux.append("Editar")
        aux.append(True)
        self.acciones.append(aux)
        aux=[]
        aux.append("Eliminar")
        aux.append(False)
        self.acciones.append(aux)
        aux=[]
        aux.append("Crear Relacion")
        aux.append(False)
        self.acciones.append(aux)
        aux=[]
        aux.append("Eliminar Relacion")
        aux.append(False)
        self.acciones.append(aux)
        
    @pms.vista.required.login_required
    def get(self):
        
        self.getItemsSolicitud()
        return flask.render_template('crearSolicitud.html', versiones=self.iversiones, acciones=self.acciones)
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
        crearPeticion(flask.session['proyectoid'],flask.request.form['comentario'],flask.session['username'],ag,acc )
        
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
                
        l=[]#lista de acciones para pasarle a la funcion que crea la solicitud
        acciones=[]
        aux=[]
        aux.append("Editar")
        if "Editar"in flask.request.form:
            l.insert(0, True)
            aux.append(True)
        else:
            l.insert(0, False)
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Eliminar")
        if "Eliminar" in flask.request.form:
            l.insert(1, True)
            aux.append(True)
        else:
            l.insert(1, False)
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Crear Relacion")
        if "Crear Relacion" in flask.request.form:
            l.insert(2, True)
            aux.append(True)
        else:
            l.insert(2, False)
            aux.append(False)
        acciones.append(aux)
        
        aux=[]
        aux.append("Eliminar Relacion")
        if "Eliminar Relacion" in flask.request.form:
            l.insert(3, True)
            aux.append(True)
        else:
            l.insert(3, False)
            aux.append(False)
        acciones.append(aux)
        
        error=False
        if len(ag)==0:
            flask.flash(u"Debe seleccionar al menos un Item", "item")
            error=True
        if not True in l:
            flask.flash(u"Debe seleccionar al menos una Accion", "accion")
            error=True
        if flask.request.form['comentario']=="":
            flask.flash(u"El campo no puede estar vacio","comentario")
            error=True
        if error:
            return flask.render_template('editarSolicitud.html', versiones=items, acciones=acciones)
        #editarSolicitud(flask.session['solicitudid'], ag, l, flask.request.form['comentario'])
        flask.flash(u"EDICION EXITOSA","text-success")
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
    iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
    """for i in i versiones:
        if i[0] in soli.items:
            i[1]=True
    acc=[]
    aux=[]
    aux.append("Editar")
    if soli.acciones%10==1:
        aux.append(True)
    else:
        aux.append(False)"""
    
     
    return flask.render_template('editarSolicitud.html') 

@app.route('/admsolicitud/eliminar/<s>')
@pms.vista.required.login_required       
def eSolicitud(s=None): 
    """
    Funcion que despliega la Vista de Eliminar Solicitud, llama a eliminarSolicitud.html 
    responde al boton de 'Eliminar' de Administrar Solicitud
    recibe el id de la Solicitud a eliminarce
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    #soli=getSolicitud(s)
    flask.session['solicitudid']=s
    return flask.render_template('eliminarSolicitud.html')   

@app.route('/admsolicitud/consultar/<s>')
@pms.vista.required.login_required
def consultarSolicitud(s=None):
    """
    Funcion que despliega pagina de consulta de Solicitud llama a consultarSolicitud.html
    responde al boton de 'Consultar' de Administrar Solicitud
    recibe el id de la solicitud a consultar
    """
    #soli=getSolicitud(s)
    return flask.render_template('consultarSolicitud.html')
 
