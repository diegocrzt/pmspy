import flask.views
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, getUsuarioById, editarUsuario, comprobarUsuario, usuarioIsLider
from pms.modelo.proyectoControlador import getProyectosFiltrados, getProyectosPaginados, getCantProyectos, comprobarProyecto, crearProyecto, getProyectos, eliminarProyecto, getProyectoId, inicializarProyecto, getProyecto
from datetime import datetime
import pms.vista.required
from pms.modelo.rolControlador import getProyectosDeUsuario
from pms import app
from pms.vista.paginar import calculoDeSiguiente, calculoDeAnterior, calculoPrimeraPag
TAM_PAGINA=5
class AdmProyecto(flask.views.MethodView):
    """
    Gestiona y Ejecuta la Vista de Administrar Proyectos
    """
    @pms.vista.required.login_required
    def get(self):
        """
        Ejecuta el template admProyecto.html
        """
        global TAM_PAGINA
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        
        flask.session['filtro']=""

        if flask.session['cambio']:
            flask.session['cambio']=False
            p=getProyectosPaginados(flask.session['pagina']-1,TAM_PAGINA, flask.session['filtro'])
            infopag=flask.session['infopag']
        else:
            flask.session['pagina']=1
            p=getProyectosPaginados(flask.session['pagina']-1,TAM_PAGINA)
            infopag=calculoPrimeraPag(getCantProyectos())
        lp=getProyectosDeUsuario(flask.session['usuarioid'])
        return flask.render_template('admProyecto.html',proyectos=p, infopag=infopag, buscar=False, lp=lp)
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta el template admProyecto.html
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

    
class Crearproyecto(flask.views.MethodView):
    """
    Vista de Crear Proyecto
    """
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
    def get(self):
        return flask.render_template('crearProyecto.html',u=getUsuarios())
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Crear Proyecto
        """
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=int(flask.request.form['lider'])
        flask.session['aux3']=flask.request.form['fechainicio']
        flask.session['aux4']=flask.request.form['fechafin']
        fechainicio=flask.request.form['fechainicio']
        fechafin=flask.request.form['fechafin']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.redirect(flask.url_for('crearproyecto'))
        if comprobarProyecto(flask.request.form['nombre']):
            flask.flash(u"El proyecto ya existe","nombre")
            return flask.redirect(flask.url_for('crearproyecto'))
        if(flask.request.form['fechainicio']==""):
            fechainicio=datetime.today()
        else:
            fechainicio = datetime.strptime(fechainicio, '%Y-%m-%d')
        if(flask.request.form['fechafin']==""):
            flask.flash(u"El campo fecha fin no puede estar vacio","fechafin")
            return flask.redirect(flask.url_for('crearproyecto'))
        else:
            fechafin = datetime.strptime(fechafin, '%Y-%m-%d')
        if fechafin <= fechainicio:
            flask.flash(u"Incoherencia entre fechas de inicio y de fin","fecha")
            return flask.redirect(flask.url_for('crearproyecto'))
        
        crearProyecto(flask.request.form['nombre'][:20], 0, fechainicio,fechafin, None, flask.request.form['lider'], None)
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        p=getProyecto(flask.request.form['nombre'][:20])
        flask.flash(u"CREACION EXITOSA","text-success")
        return flask.redirect(flask.url_for('admproyecto'))
    
class Inicializarproyecto(flask.views.MethodView):
    """
    Vista de Inicializar Proyecto
    """  
    @pms.vista.required.login_required  
    def get(self):
        return flask.render_template('inicializarProyecto.html')
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Inicializar Proyecto
        """
        inicializarProyecto(flask.session['proyectoid'])
        flask.session['proyectoiniciado']=True
        return flask.redirect('/admfase/'+str(flask.session['proyectoid']))     
    
class Eliminarproyecto(flask.views.MethodView):
    """
    Vista de Eliminar Proyecto
    """
    @pms.vista.required.login_required  
    def get(self):
        return flask.redirect(flask.url_for('admproyecto'))
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Eliminar Proyecto
        """
        eliminarProyecto(flask.session['proyectoid'])
        flask.session.pop('proyectoid',None)
        return flask.redirect(flask.url_for('admproyecto')) 
    
@app.route('/admproyecto/eliminarproyecto/<proyecto>')
@pms.vista.required.admin_required
@pms.vista.required.login_required
def eProyecto(proyecto=None):
    """
    Funcion que llama a la Vista de Eliminar Proyecto, responde al boton de 'Eliminar' de Administrar Proyecto
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)
    p=getProyectoId(proyecto)
    if p.estado!="Inicializado":  
        flask.session['proyectoid']=p.id
        return flask.render_template('eliminarProyecto.html',p=p)
    else:
        flask.flash("El Proyecto seleccionado no se puede eliminar porque ya fue inicializado")
        return flask.redirect(flask.url_for('admproyecto'))    
    
@app.route('/admproyecto/nextproyecto/')
@pms.vista.required.login_required       
def nextPageP():
    flask.session['cambio']=True
    cantP=getCantProyectos()
    flask.session['infopag']=calculoDeSiguiente(cantP)
    return flask.redirect(flask.url_for('admproyecto'))  

@app.route('/admproyecto/prevproyecto/')
@pms.vista.required.login_required       
def prevPageP():
    flask.session['cambio']=True
    flask.session['infopag']=calculoDeAnterior(getCantProyectos())
    return flask.redirect(flask.url_for('admproyecto'))  
 
    