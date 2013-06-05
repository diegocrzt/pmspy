import flask.views
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, getUsuarioById, editarUsuario, comprobarUsuario, usuarioIsLider
from pms.modelo.proyectoControlador import getProyectosFiltrados, getProyectosPaginados, getCantProyectos, comprobarProyecto, crearProyecto, getProyectos, eliminarProyecto, getProyectoId, inicializarProyecto, getProyecto
from pms.modelo.peticionControlador import agregarMiembro
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
        return flask.render_template('admSolicitud.html',solicitudes=None, infopag="1 de 1", buscar=False)
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
