import flask.views
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, getUsuarioById, editarUsuario, comprobarUsuario, usuarioIsLider
from pms.modelo.proyectoControlador import getProyectosFiltrados, getProyectosPaginados, getCantProyectos, comprobarProyecto, crearProyecto, getProyectos, eliminarProyecto, getProyectoId, inicializarProyecto, getProyecto
from pms.modelo.peticionControlador import agregarMiembro
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
    #iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
    @pms.vista.required.login_required
    def get(self):
        iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
        acciones=[]
        aux=[]
        aux.append("Editar")
        aux.append(True)
        acciones.append(aux)
        aux=[]
        aux.append("Eliminar")
        aux.append(False)
        acciones.append(aux)
        aux=[]
        aux.append("Crear Relacion")
        aux.append(False)
        acciones.append(aux)
        aux=[]
        aux.append("Eliminar Relacion")
        aux.append(False)
        acciones.append(aux)
        return flask.render_template('crearSolicitud.html', versiones=iversiones, acciones=acciones)
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Crear Proyecto
        """
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=int(flask.request.form['lider'])
        flask.session['aux3']=flask.request.form['fechainicio']
        flask.session['aux4']=flask.request.form['fechafin']
        ag=[]
        iversiones=getVersionesItemParaSolicitud(flask.session['proyectoid'])
        for u in iversiones:
            if u.nombredeusuario in flask.request.form:
                if flask.request.form[u.nonombredeusuariombre]:
                    ag.append(u)
        if len(ag)!=0:
            a=True
        
        flask.flash(u"CREACION EXITOSA","text-success")
        return flask.redirect(flask.url_for('admproyecto'))
