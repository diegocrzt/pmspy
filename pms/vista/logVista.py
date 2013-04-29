import flask.views
from pms.modelo.usuarioControlador import validar, getUsuario

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
        flask.session['aux1']=flask.request.form['username']
        incompleto=False
        required = False
        if flask.request.form['username']=="":
            flask.flash(u"El nombre de usuario es necesario.","usuario")
            required=True
        if flask.request.form['passwd']=="":
            flask.flash(u"La clave es necesaria.","clave")
            required=True
        if required:
            return flask.redirect(flask.url_for('index'))
        """for r in required:
            print "for"
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                incompleto=True
                print "if"
                return flask.redirect(flask.url_for('index'))"""
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
        if(incompleto==False):
            if validar(username, passwd):
                flask.session['username'] = username          
                u = getUsuario(username)
                if u.isAdmin==True:
                    flask.session['isAdmin']=u.isAdmin
                flask.session['usuarioid']=u.id
            else:
                flask.flash(u"Nombre de usuario no existe o clave incorrecta","incorrecto")
        return flask.redirect(flask.url_for('admproyecto'))
