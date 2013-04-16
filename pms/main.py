'''
Created on 05/04/2013

@author: synchro
'''
import flask.views
import functools
from flask import request
from werkzeug.serving import run_simple
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, editarUsuario, comprobarUsuario

app = flask.Flask(__name__)




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
        
    """
    @login_required
    def get(self):
        return flask.render_template('admProyecto.html')
    @login_required
    def post(self):
        return flask.render_template('admProyecto.html')

class Crearusuario(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('crearUsuario.html')
    @login_required
    def post(self):
        required = ['nombre','usuario', 'clave']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('index'))
        if comprobarUsuario(flask.request.form['usuario']):
            flask.flash("El usuario ya existe")
            return flask.redirect(flask.url_for('crearusuario'))
        a = 'admin'
        if a not in flask.request.form:
            a=False
        else:
            a=True
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


@app.route('/admusuario/eliminarusuario/<username>')
def eUsuario(username=None):
        eliminarUsuario(username)
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    

@app.route('/admusuario/editarusuario/<u>', methods=["POST", "GET"])
def edUsuario(u=None):
    
    if request.method == "GET":
        usuario=getUsuario(u)
        return flask.render_template('editarUsuario.html',u=usuario)
    else:
        return flask.render_template('admUsuario.html')


app.debug = True
run_simple("localhost", 5000, app, use_reloader=True, use_debugger=True, use_evalex=True)