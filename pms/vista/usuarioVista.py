import flask.views
from flask import request
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, getUsuarioById, editarUsuario, comprobarUsuario, usuarioIsLider
import pms.vista.required
from pms import app
class AdmUsuario(flask.views.MethodView):
    """
    Vista de Administrar Usuario
    """
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
    def get(self):
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
    def post(self):
        b=getUsuarios()
        return flask.render_template('admUsuario.html',usuarios=b)
    
    
class Eliminarusuario(flask.views.MethodView):
    """
    Vista de Eliminar Usuario
    """
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect(flask.url_for('admusuario'))
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
    def post(self):
        eliminarUsuario(flask.session['usuarioeliminar'])
        b=getUsuarios()
        flask.session.pop('usuarioeliminar',None)
        return flask.render_template('admUsuario.html',usuarios=b)
 
 
    
class Editarusuario(flask.views.MethodView):
    """
    Vista de Editar Usuario
    """
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect(flask.url_for('admusuario'))
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
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

class Crearusuario(flask.views.MethodView):
    """
    Vista de Crear Usuario
    """
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
    def get(self):
        return flask.render_template('crearUsuario.html')
    @pms.vista.required.admin_required
    @pms.vista.required.login_required
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
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        return flask.redirect(flask.url_for('admusuario'))  
    
@app.route('/admusuario/eliminarusuario/<username>')
@pms.vista.required.admin_required
@pms.vista.required.login_required
def eUsuario(username=None): 
    """
    Funcion que llama a la Vista de Eliminar Usuario, responde al boton de 'Eliminar' de Administrar Usuario
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)
    if usuarioIsLider(username):
        flask.flash("El usuario seleccionado no se puede eliminar puesto que es lider de un o mas proyectos")
        return flask.redirect(flask.url_for('admusuario'))
    else:
        user=getUsuario(username)
        flask.session['usuarioeliminar']=user.nombre
        return flask.render_template('eliminarUsuario.html',u=user)

    

@app.route('/admusuario/editarusuario/<u>', methods=["POST", "GET"])
@pms.vista.required.admin_required
@pms.vista.required.login_required
def edUsuario(u=None):
    """
    Funcion que llama a la Vista de Editar Usuario, responde al boton de 'Editar' de Administrar Usuario
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)
    if request.method == "GET":
        usuar=getUsuario(u)
        flask.session['usviejoid']=usuar.id
        flask.session['usviejousername']=usuar.nombredeusuario
        return flask.render_template('editarUsuario.html',u=usuar)
    else:
        return flask.render_template('admUsuario.html')
      
      