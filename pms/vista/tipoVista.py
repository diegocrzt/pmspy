import flask.views
from flask import request
import pms.vista.required
from pms import app
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase

@app.route('/admtipo/<f>')
@pms.vista.required.login_required
def admTipo(f=None):
    """
    Funcion que llama a la Vista de Administrar Tipo de Item, responde al boton de 'Selec>>' de Administrar Fase
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)  
    if request.method == "GET":
        fase=getFaseId(f)
        flask.session.pop('faseid',None)
        flask.session['faseid']=fase.id
        flask.session['fasenombre']=fase.nombre
        t=fase.tipos
        return flask.render_template('admTipo.html',tipos=t)
    else:
        return flask.redirect(flask.url_for('admfase'))