import flask.views
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, getUsuarioById, editarUsuario, comprobarUsuario, usuarioIsLider


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
