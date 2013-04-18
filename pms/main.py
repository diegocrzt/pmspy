'''
Created on 05/04/2013

@author: synchro
'''
import flask.views
import functools
from flask import request
from werkzeug.serving import run_simple
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, editarUsuario, comprobarUsuario
from pms.modelo.proyectoControlador import comprobarProyecto, crearProyecto, getProyectos, eliminarProyecto
from pms.modelo.faseControlador import getFases

app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "bacon"

#users = {'jake':'bacon'}
#comentario

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
        else:
            flask.flash("Username doesn't exist or incorrect password")
        return flask.redirect(flask.url_for('admproyecto'))

def login_required(method):
    """
        holaaaaaaaa
        
        Muestra un mensaje pidiendo que el usuario inicie sesion
    """
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in flask.session:
            return method(*args, **kwargs)
        else:
            flask.flash("A login is required to see the page!")
            return flask.redirect(flask.url_for('index'))
    return wrapper

    
class AdmProyecto(flask.views.MethodView):
    """
    Administrar Proyectos
    """
    @login_required
    def get(self):
        p=getProyectos()
        return flask.render_template('admProyecto.html',proyectos=p)
    @login_required
    def post(self):
        p=getProyectos()
        return flask.render_template('admProyecto.html',proyectos=p)

class Crearusuario(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('crearUsuario.html')
    @login_required
    def post(self):
        '''required = ['nombre','usuario', 'clave']
        
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))'''
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
        crearUsuario(flask.request.form['nombre'], flask.request.form['usuario'],flask.request.form['clave'],a)
        return flask.redirect(flask.url_for('admusuario'))
    
    
class EliminarUsuario(flask.views.MethodView):
    @login_required
    def get(self):
        b=getUsuarios()
        for u in b:
            print u.nombre
            print u.clave
        return flask.redirect(flask.url_for('admusuario'))
    @login_required
    def post(self):
        return flask.redirect(flask.url_for('admusuario'))
    
class AdmUsuario(flask.views.MethodView):
    @login_required
    def get(self):
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    @login_required
    def post(self):
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    
class Editarusuario(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.redirect(flask.url_for('admusuario'))
    @login_required
    def post(self):
        required = ['nombre','usuario', 'clave']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('index'))
        a = 'admin'
        if a not in flask.request.form:
            a=False
        else:
            a=True
        print "aca esta el id:  "
        print flask.request.form['id']
        editarUsuario(flask.request.form['id'], flask.request.form['nombre'], flask.request.form['usuario'],flask.request.form['clave'],a)
        return flask.redirect(flask.url_for('admusuario'))
    
class Crearproyecto(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('crearProyecto.html')
    @login_required
    def post(self):
        
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect(flask.url_for('crearproyecto'))
        if(flask.request.form['lider']==""):
            flask.flash("El campo lider no puede estar vacio")
            return flask.redirect(flask.url_for('crearproyecto'))

        if comprobarProyecto(flask.request.form['nombre']):
            flask.flash("El proyecto ya existe")
            return flask.redirect(flask.url_for('crearproyecto'))
        crearProyecto(flask.request.form['nombre'],0, flask.request.form['fechainicio'],flask.request.form['fechafin'], None, flask.request.form['lider'])
        return flask.redirect(flask.url_for('admproyecto'))

class AdmFase(flask.views.MethodView):
    """
    Administrar fases de un proyecto
    """
    @login_required
    def get(self):
        #f=getFases()
        return flask.render_template('admFase.html'''',fases=f''')
    @login_required
    def post(self):
        #f=getFases()
        return flask.render_template('admFase.html' ''',fases=f''')

    
    
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


@app.route('/admusuario/eliminarusuario/<username>')
@login_required
def eUsuario(username=None): 
        eliminarUsuario(username)
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    

@app.route('/admusuario/editarusuario/<u>', methods=["POST", "GET"])
@login_required
def edUsuario(u=None):
    if request.method == "GET":
        usuario=getUsuario(u)
        return flask.render_template('editarUsuario.html',u=usuario)
    else:
        return flask.render_template('admUsuario.html')


@app.route('/admproyecto/eliminarproyecto/<proyecto>')
@login_required
def eProyecto(proyecto=None): 
        eliminarProyecto(proyecto)
        p=getProyectos()
        return flask.render_template('admProyecto.html',proyectos=p)

@app.route('/admfase/<p>')
@login_required
def admFase(p=None): 
    if request.method == "GET":
        f=getFases(p)
        return flask.render_template('admFase.html',fases=f)
    else:
        return flask.render_template('admProyecto.html')

app.debug = True 
run_simple("localhost", 5050, app, use_reloader=True, use_debugger=True, use_evalex=True)
