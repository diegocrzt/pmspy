'''
Created on 05/04/2013

@author: Martin Poletti
@author: Natalia Valdez
'''
import flask.views
import functools
from flask import request
from werkzeug.serving import run_simple
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, getUsuarioById, editarUsuario, comprobarUsuario, usuarioIsLider
from pms.modelo.proyectoControlador import comprobarProyecto, crearProyecto, getProyectos, eliminarProyecto, getProyectoId, inicializarProyecto
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase
from datetime import date, timedelta
from datetime import datetime
app = flask.Flask(__name__)
import os
app.secret_key = "bacon"
class Main(flask.views.MethodView):
    """
        Punto de entrada de la aplicacion
    """
    def get(self):
        """
           Devuelve la pagina index.html 
        """
        return flask.render_template('index.html')
    
    def post(self):
        """
            Verifica si el usuario ha iniciado sesion
        """
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            flask.session.pop('isAdmin',None)
            flask.session.pop('usuarioid',None)
            flask.session.pop('proyectoid', None)
            flask.session.pop('faseid',None)
            flask.session.pop('proyectonombre',None)
            flask.session.pop('proyectoiniciado', None)
            return flask.redirect(flask.url_for('index'))
        required = ['username', 'passwd']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('index'))
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
        if validar(username, passwd):
            flask.session['username'] = username          
            u = getUsuario(username)
            if u.isAdmin==True:
                flask.session['isAdmin']=u.isAdmin
            flask.session['usuarioid']=u.id
        else:
            flask.flash("Nombre de usuario no existe o clave incorrecta")
        return flask.redirect(flask.url_for('admproyecto'))

def login_required(method):
    """
    Controla que el usuario haya iniciado sesion para realizar la opercacion
    """
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in flask.session:
            return method(*args, **kwargs)
        else:
            flask.flash("Es necesario el logueo")
            return flask.redirect(flask.url_for('index'))
    return wrapper



def admin_required(method):
    """
        Controla que el usuario posea el rol de administrador
    """
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'isAdmin' in flask.session:
            if flask.session['isAdmin']:
                return method(*args, **kwargs)
            else:
                return flask.redirect(flask.url_for('admproyecto'))
        else:
            flask.flash("no tiene permiso de admin!")
            return flask.redirect(flask.url_for('admproyecto'))
    return wrapper

    
class AdmProyecto(flask.views.MethodView):
    """
    Gestiona y Ejecuta la Vista de Administrar Proyectos
    """
    @login_required
    def get(self):
        """
        Ejecuta el template admProyecto.html
        """
        p=getProyectos()
        return flask.render_template('admProyecto.html',proyectos=p)
    @login_required
    def post(self):
        """
        Ejecuta el template admProyecto.html
        """
        p=getProyectos()
        return flask.render_template('admProyecto.html',proyectos=p)

class Crearusuario(flask.views.MethodView):
    """
    Vista de Crear Usuario
    """
    @admin_required
    @login_required
    def get(self):
        return flask.render_template('crearUsuario.html')
    @admin_required
    @login_required
    def post(self):
        """
        Ejecuta la funcion de Crear Usuario
        """
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['usuario']
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect(flask.url_for('crearusuario'))
        if(flask.request.form['usuario']==""):
            flask.flash("El campo usuario no puede estar vacio")
            return flask.redirect(flask.url_for('crearusuario'))
        if(flask.request.form['clave']==""):
            flask.flash("El campo clave no puede estar vacio")
            return flask.redirect(flask.url_for('crearusuario'))
        
        if comprobarUsuario(flask.request.form['usuario']):
            flask.flash("El usuario ya existe")
            return flask.redirect(flask.url_for('crearusuario'))
        a = 'admin'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['admin']
        crearUsuario(flask.request.form['nombre'][:20], flask.request.form['usuario'][:20],flask.request.form['clave'][:20],a)
        return flask.redirect(flask.url_for('admusuario'))
    
    
class EliminarUsuario(flask.views.MethodView):
    """
    Vista de Eliminar Usuario
    """
    @admin_required
    @login_required
    def get(self):
        return flask.redirect(flask.url_for('admusuario'))
    @admin_required
    @login_required
    def post(self):
        return flask.redirect(flask.url_for('admusuario'))
    
class AdmUsuario(flask.views.MethodView):
    """
    Vista de Administrar Usuario
    """
    @admin_required
    @login_required
    def get(self):
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    @admin_required
    @login_required
    def post(self):
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    
class Editarusuario(flask.views.MethodView):
    """
    Vista de Editar Usuario
    """
    @admin_required
    @login_required
    def get(self):
        return flask.redirect(flask.url_for('admusuario'))
    @admin_required
    @login_required
    def post(self):
        """
        Ejecuta la funcion de Editar Usuario
        """
        clave=flask.request.form['clave']
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect('/admusuario/editarusuario/'+str(flask.session['usviejousername']))
        if(flask.request.form['usuario']==""):
            flask.flash("El campo usuario no puede estar vacio")
            return flask.redirect('/admusuario/editarusuario/'+str(flask.session['usviejousername']))
        a = 'admin'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['admin']
        if flask.session['usviejousername'] != flask.request.form['usuario']:
            if comprobarUsuario(flask.request.form['usuario']):
                flask.flash("El usuario ya esta usado")
                return flask.redirect('/admusuario/editarusuario/'+str(flask.session['usviejousername']))     
        if  flask.request.form['clave']=="":
            clave=None  
        editarUsuario(flask.session['usviejoid'], flask.request.form['nombre'][:20], flask.request.form['usuario'][:20],clave,a)
        return flask.redirect(flask.url_for('admusuario'))
    
class Crearproyecto(flask.views.MethodView):
    """
    Vista de Crear Proyecto
    """
    @admin_required
    @login_required
    def get(self):
        return flask.render_template('crearProyecto.html',u=getUsuarios())
    @admin_required
    @login_required
    def post(self):
        """
        Ejecuta la funcion de Crear Proyecto
        """
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['lider']
        flask.session['aux3']=flask.request.form['fechainicio']
        flask.session['aux4']=flask.request.form['fechafin']
        fechainicio=flask.request.form['fechainicio']
        fechafin=flask.request.form['fechafin']
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect(flask.url_for('crearproyecto'))
        if(flask.request.form['lider']==""):
            flask.flash("El campo lider no puede estar vacio")
            return flask.redirect(flask.url_for('crearproyecto'))
        if getUsuarioById(flask.request.form['lider'])==None:
            flask.flash("El usuario asignado como lider no existe")
            return flask.redirect(flask.url_for('crearproyecto'))
        if(flask.request.form['fechainicio']==""):
            fechainicio=datetime.today()
        else:
            fechainicio = datetime.strptime(fechainicio, '%Y-%m-%d')
        if(flask.request.form['fechafin']==""):
            flask.flash("El campo fecha fin no puede estar vacio")
            return flask.redirect(flask.url_for('crearproyecto'))
        else:
            fechafin = datetime.strptime(fechafin, '%Y-%m-%d')
        if fechafin <= fechainicio:
            flask.flash("incoherencia entre fechas de inicio y de fin")
            return flask.redirect(flask.url_for('crearproyecto'))
        if comprobarProyecto(flask.request.form['nombre']):
            flask.flash("El proyecto ya existe")
            return flask.redirect(flask.url_for('crearproyecto'))
        crearProyecto(flask.request.form['nombre'][:20], 0, fechainicio,fechafin, None, flask.request.form['lider'], None)
        return flask.redirect(flask.url_for('admproyecto'))

class Crearfase(flask.views.MethodView):
    """
    Gestiona la Vista de Crear Fase
    """
    @login_required
    def get(self):
        return flask.render_template('crearFase.html')
    @login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['numero']
        flask.session['aux3']=flask.request.form['fechainicio']
        flask.session['aux4']=flask.request.form['fechafin']
        fechainicio=flask.request.form['fechainicio']
        fechafin=flask.request.form['fechafin']
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect(flask.url_for('crearfase'))
        if(flask.request.form['numero']==""):
            flask.flash("El campo numero no puede estar vacio")
            return flask.redirect(flask.url_for('crearfase'))
        if(flask.request.form['fechainicio']==""):
            fechainicio=datetime.today()
        else:
            fechainicio = datetime.strptime(fechainicio, '%Y-%m-%d')
        if(flask.request.form['fechafin']==""):
            fechafin=datetime.today()+timedelta(days=15)
        else:
            fechafin = datetime.strptime(fechafin, '%Y-%m-%d')
        if fechafin <= fechainicio:
            flask.flash("incoherencia entre fechas de inicio y de fin")
            return flask.redirect(flask.url_for('crearfase'))
        if comprobarFase(flask.request.form['numero'],flask.session['proyectoid']):
            flask.flash("La fase ya existe")
            return flask.redirect(flask.url_for('crearfase'))
        crearFase(flask.request.form['nombre'][:20],flask.request.form['numero'], fechainicio, fechafin, None, None, flask.session['proyectoid'])
        return flask.redirect('/admfase/'+str(flask.session['proyectoid'])) 
    
class Editarfase(flask.views.MethodView):
    """
    Vista de Editar Fase
    """
    @login_required
    def get(self):
        return flask.redirect(flask.url_for('admfase'))
    @login_required
    def post(self):
        """
        Ejecuta la funcion de Editar Fase
        """
        fechainicio=flask.request.form['fechainicio']
        fechafin=flask.request.form['fechafin']
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid']))
        if(flask.request.form['numero']==""):
            flask.flash("El campo numero no puede estar vacio")
            return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid']))     
        if(flask.request.form['fechainicio']==""):
            fechainicio=datetime.today()
        else:
            fechainicio = datetime.strptime(fechainicio, '%Y-%m-%d')
        if(flask.request.form['fechafin']==""):
            fechafin=datetime.today()+timedelta(days=15)
        else:
            fechafin = datetime.strptime(fechafin, '%Y-%m-%d')
        if fechafin <= fechainicio:
            flask.flash("incoherencia entre fechas de inicio y de fin")
            return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid'])) 
        if str(flask.session['numerofase']) != str(flask.request.form['numero']):
            if comprobarFase(flask.request.form['numero'], flask.session['proyectoid']):
                flask.flash("El numero de fase ya esta usado")
                return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid']))
        editarFase(flask.session['faseid'], flask.request.form['nombre'][:20],flask.request.form['numero'], fechainicio,fechafin)
        return flask.redirect('/admfase/'+str(flask.session['proyectoid']))        
    
class Inicializarproyecto(flask.views.MethodView):
    """
    Vista de Inicializar Proyecto
    """  
    @login_required  
    def get(self):
        return flask.render_template('inicializarProyecto.html')
    @login_required
    def post(self):
        """
        Ejecuta la funcion de Inicializar Proyecto
        """
        inicializarProyecto(flask.session['proyectoid'])
        flask.session['proyectoiniciado']=True
        return flask.redirect('/admfase/'+str(flask.session['proyectoid'])) 

class Eliminarfase(flask.views.MethodView):
    """
    Vista de Eliminar Fase
    """
    
    @login_required  
    def get(self):
        if(flask.session['faseid']!=None):
            return flask.render_template('eliminarFase.html')
        else:
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
    @login_required
    def post(self):
        """
        Ejecuta la funcion de Eliminar Fase
        """
        if(flask.session['faseid']!=None):
            eliminarFase(flask.session['faseid'],flask.session['proyectoid'])
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
        else:
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))

class Eliminarproyecto(flask.views.MethodView):
    """
    Vista de Eliminar Proyecto
    """
    @login_required  
    def get(self):
        return flask.redirect(flask.url_for('admproyecto'))
    @login_required
    def post(self):
        """
        Ejecuta la funcion de Eliminar Proyecto
        """
        eliminarProyecto(flask.session['proyectoid'])
        flask.session.pop('proyectoid',None)
        return flask.redirect(flask.url_for('admproyecto'))

@app.route('/admusuario/eliminarusuario/<username>')
@admin_required
@login_required
def eUsuario(username=None): 
    """
    Funcion que llama a la Vista de Eliminar Usuario, responde al boton de 'Eliminar' de Administrar Usuario
    """
    if usuarioIsLider(username):
        flask.flash("El usuario seleccionado no se puede eliminar puesto que es lider de un o mas proyectos")
        return flask.redirect(flask.url_for('admusuario'))
    else:
        eliminarUsuario(username)
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    

@app.route('/admusuario/editarusuario/<u>', methods=["POST", "GET"])
@admin_required
@login_required
def edUsuario(u=None):
    """
    Funcion que llama a la Vista de Editar Usuario, responde al boton de 'Editar' de Administrar Usuario
    """
    if request.method == "GET":
        usuar=getUsuario(u)
        flask.session['usviejoid']=usuar.id
        flask.session['usviejousername']=usuar.nombredeusuario
        return flask.render_template('editarUsuario.html',u=usuar)
    else:
        return flask.render_template('admUsuario.html')
      

@app.route('/admproyecto/eliminarproyecto/<proyecto>')
@admin_required
@login_required
def eProyecto(proyecto=None):
    """
    Funcion que llama a la Vista de Eliminar Proyecto, responde al boton de 'Eliminar' de Administrar Proyecto
    """
    p=getProyectoId(proyecto)
    if p.estado!="Inicializado":  
        flask.session['proyectoid']=p.id
        return flask.render_template('eliminarProyecto.html',p=p)
    else:
        flask.flash("El Proyecto seleccionado no se puede eliminar porque ya fue inicializado")
        return flask.redirect(flask.url_for('admproyecto'))

@app.route('/admfase/<p>')
@login_required
def admFase(p=None):
    """
    Funcion que llama a la Vista de Administrar Fase, responde al boton de 'Selec>>' de Administrar Proyecto
    """  
    if request.method == "GET":
        if(getProyectoId(p).lider==flask.session['usuarioid']):
            flask.session.pop('faseid',None)
            flask.session['proyectoid']=p
            flask.session['proyectonombre']=getProyectoId(p).nombre
            f=getFases(p)
            if(getProyectoId(p).estado!="Iniciado"):
                flask.session['proyectoiniciado']=False
            else:
                flask.session['proyectoiniciado']=True
            tienefases=True
            if(getProyectoId(p).cantFase==0):
                tienefases=False
            return flask.render_template('admFase.html',fases=f, hay=tienefases)
        else:
            return flask.redirect(flask.url_for('admproyecto'))
    else:
        return flask.redirect(flask.url_for('admproyecto'))

@app.route('/admfase/eliminarfase/<fase>')
@login_required
def eFase(fase=None): 
    """
    Funcion que llama a la Vista de Eliminar Fase, responde al boton de 'Eliminar' de Administrar Fase
    """
    fas=getFaseId(fase)
    flask.session['faseid']=fas.id
    p=getProyectoId(fas.proyecto)
    if(p.lider == flask.session['usuarioid']):
        return flask.render_template('eliminarFase.html',f=fas)           
    else:
        return flask.redirect(flask.url_for('admproyecto'))
    
@app.route('/admfase/editarfase/<f>', methods=["POST", "GET"])
@login_required
def edFase(f=None):
    """
    Funcion que llama a la Vista de Editar Fase, responde al boton de 'Editar' de Administrar Fase
    """
    if request.method == "GET":
        fas=getFaseId(f)
        flask.session['numerofase']=fas.numero
        flask.session['faseid']=fas.id
        flask.session['proyectoid']=fas.proyecto
        p=getProyectoId(fas.proyecto)
        if(p.lider == flask.session['usuarioid']):
            return flask.render_template('editarFase.html',f=fas)
        else:
            return flask.redirect(flask.url_for('admproyecto'))
    else:
        return flask.render_template('admFase.html')

app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])

app.add_url_rule('/admproyecto/',
                 view_func=AdmProyecto.as_view('admproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/admusuario/crearusuario/',
                 view_func=Crearusuario.as_view('crearusuario'),
                 methods=["GET", "POST"])

app.add_url_rule('/admusuario/',
                 view_func=AdmUsuario.as_view('admusuario'),
                 methods=["GET", "POST"])

app.add_url_rule('/admusuario/editarusuario/',
                 view_func=Editarusuario.as_view('editusuario'),
                 methods=["GET", "POST"])

app.add_url_rule('/admproyecto/crearproyecto/',
                 view_func=Crearproyecto.as_view('crearproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/crearfase/',
                 view_func=Crearfase.as_view('crearfase'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/editarfase/',
                 view_func=Editarfase.as_view('editarfase'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/inicializarproyecto/',
                 view_func=Inicializarproyecto.as_view('inicializarproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/eliminarfase/',
                 view_func=Eliminarfase.as_view('eliminarfase'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/eliminarproyecto/',
                 view_func=Eliminarproyecto.as_view('eliminarproyecto'),
                 methods=["GET", "POST"])

app.debug = True 
run_simple("localhost", 5000, app, use_reloader=True, use_debugger=True, use_evalex=True)