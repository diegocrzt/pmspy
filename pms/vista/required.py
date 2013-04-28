import functools
import flask

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