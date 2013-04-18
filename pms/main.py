'''
Created on 05/04/2013

@author: mpoletti
'''
import flask.views
import functools
from pms.modelo.entidad import Usuario
from flask import request
from werkzeug.serving import run_simple
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, editarUsuario, comprobarUsuario

globusuario = None

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
            flask.session.pop('isAdmin',None)
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



def admin_required(method):
    """
        Muestra un mensaje pidiendo que el usuario inicie sesion
    """
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'isAdmin' in flask.session:
            return method(*args, **kwargs)
        else:
            flask.flash("no tiene permiso de admin!")
            return flask.redirect(flask.url_for('admproyecto'))
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
    @admin_required
    @login_required
    def get(self):
        return flask.render_template('crearUsuario.html')
    @admin_required
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
    @admin_required
    @login_required
    def get(self):
        b=getUsuarios()
        for u in b:
            print u.nombre
            print u.clave
        return flask.redirect(flask.url_for('admusuario'))
    @admin_required
    @login_required
    def post(self):
        return flask.redirect(flask.url_for('admusuario'))
    
class AdmUsuario(flask.views.MethodView):
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
    @admin_required
    @login_required
    def get(self):
        return flask.redirect(flask.url_for('admusuario'))
    @admin_required
    @login_required
    def post(self):
        global globusuario
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect('/admusuario/editarusuario/'+globusuario.nombredeusuario)
        if(flask.request.form['usuario']==""):
            flask.flash("El campo usuario no puede estar vacio")
            return flask.redirect('/admusuario/editarusuario/'+globusuario.nombredeusuario)
        if(flask.request.form['clave']==""):
            flask.flash("El campo clave no puede estar vacio")
            return flask.redirect('/admusuario/editarusuario/'+globusuario.nombredeusuario)
        a = 'admin'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['admin']
        print "aca imprimer el global!!!!"
        print globusuario.nombredeusuario
        if globusuario.nombredeusuario != flask.request.form['usuario']:
            if comprobarUsuario(flask.request.form['usuario']):
                flask.flash("El usuario ya esta usado")
                return flask.redirect('/admusuario/editarusuario/'+globusuario.nombredeusuario)     
            
        editarUsuario(globusuario.id, flask.request.form['nombre'], flask.request.form['usuario'],flask.request.form['clave'],a)
        return flask.redirect(flask.url_for('admusuario'))
    
    
    
@app.route('/admusuario/eliminarusuario/<username>')
@admin_required
@login_required
def eUsuario(username=None): 
        eliminarUsuario(username)
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    

@app.route('/admusuario/editarusuario/<u>', methods=["POST", "GET"])
@admin_required
@login_required
def edUsuario(u=None):
    global globusuario
    if request.method == "GET":
        globusuario=getUsuario(u)
        return flask.render_template('editarUsuario.html',u=globusuario)
    else:
        return flask.render_template('admUsuario.html')
    
    
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





app.debug = True 
run_simple("localhost", 5000, app, use_reloader=True, use_debugger=True, use_evalex=True)
