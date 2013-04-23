'''
Created on 05/04/2013

@author: mpoletti
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
            flask.session.pop('usuarioid',None)
            flask.session.pop('proyectoid', None)
            flask.session.pop('faseid',None)
            flask.session.pop('proyectonombre',None)
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
        Muestra un mensaje pidiendo que el usuario inicie sesion
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
        Muestra un mensaje pidiendo que el usuario inicie sesion
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
    @admin_required
    @login_required
    def get(self):
        return flask.render_template('crearUsuario.html')
    @admin_required
    @login_required
    def post(self):
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
    @admin_required
    @login_required
    def get(self):
        return flask.render_template('crearProyecto.html')
    @admin_required
    @login_required
    def post(self):
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
    @login_required
    def get(self):
        return flask.redirect(flask.url_for('admfase'))
    @login_required
    def post(self):
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
    @login_required  
    def get(self):
        return flask.render_template('inicializarProyecto.html')
    @login_required
    def post(self):
        inicializarProyecto(flask.session['proyectoid'])
        return flask.redirect('/admfase/'+str(flask.session['proyectoid'])) 
        
    
@app.route('/admusuario/eliminarusuario/<username>')
@admin_required
@login_required
def eUsuario(username=None): 
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
        p=getProyectoId(proyecto)
        if p.estado!="Inicializado":  
            eliminarProyecto(proyecto)
            p=getProyectos()
            return flask.render_template('admProyecto.html',proyectos=p)
        else:
            flask.flash("El Proyecto seleccionado no se puede eliminar porque ya fue inicializado")
            return flask.redirect(flask.url_for('admproyecto'))

@app.route('/admfase/<p>')
@login_required
def admFase(p=None):  
    if request.method == "GET":
        if(getProyectoId(p).lider==flask.session['usuarioid']):
            flask.session['proyectoid']=p
            flask.session['proyectonombre']=getProyectoId(p).nombre
            f=getFases(p)
            return flask.render_template('admFase.html',fases=f)
        else:
            return flask.redirect(flask.url_for('admproyecto'))
    else:
        return flask.redirect(flask.url_for('admproyecto'))

@app.route('/admfase/eliminarfase/<fase>')
@login_required
def eFase(fase=None): 
        fas=getFaseId(fase)
        fas.numero
        fas.id
        flask.session['proyectoid']=fas.proyecto
        p=getProyectoId(fas.proyecto)
        if(p.lider == flask.session['usuarioid']):
            eliminarFase(fase, p.id)
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
        else:
            return flask.redirect(flask.url_for('admproyecto'))
    
@app.route('/admfase/editarfase/<f>', methods=["POST", "GET"])
@login_required
def edFase(f=None):
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

app.debug = True 
run_simple("localhost", 5000, app, use_reloader=True, use_debugger=True, use_evalex=True)

