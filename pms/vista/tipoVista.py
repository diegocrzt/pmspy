import flask.views
from flask import request
import pms.vista.required
from pms import app
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.entidad import Atributo
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
    flask.session['aux1']=""
    flask.session['aux2']=""
    flask.session['aux3']=""
    flask.session['aux4']="" 
    if request.method == "GET":
        fase=getFaseId(f)
        flask.session.pop('faseid',None)
        flask.session.pop('fasenombre',None)
        flask.session['faseid']=fase.id
        flask.session['fasenombre']=fase.nombre
        t=fase.tipos
        return flask.render_template('admTipo.html',tipos=t)
    else:
        return flask.redirect(flask.url_for('admfase'))
    
    
    
class Creartipo(flask.views.MethodView):
    """
    Gestiona la Vista de Crear tipo
    """
    @pms.vista.required.login_required
    def get(self,atributos=None):
        atributos=[]
        return flask.render_template('crearTipo.html',atributos=atributos)
    @pms.vista.required.login_required
    def post(self,atributos=None):
        if 'CrearA' in flask.request.form :
            print "pruebaaaa"
            flask.session['aux3']=flask.request.form['nombreatributo']
            flask.session['aux4']=flask.request.form['tipodato']
            if(flask.request.form['nombreatributo']==""):
                flask.flash("El campo nombre de atributo no puede estar vacio")
                return flask.render_template('crearTipo.html',atributos=atributos)
            if(flask.request.form['tipodato']==""):
                flask.flash("El campo tipo de dato del atributo no puede estar vacio")
                return flask.render_template('crearTipo.html',atributos=atributos)
            if comprobarAtributo(flask.request.form['nombre'],flask.session['faseid']):
                flask.flash("El atributo ya existe")
                return flask.render_template('crearTipo.html',atributos=atributos)
            at=Atributo(flask.request.form['nombreatributo'],flask.request.form['tipodato'],None)
            atributos.append(at)
            flask.session.pop('aux3',None)
            flask.session.pop('aux4',None)
            return flask.render_template('crearTipo.html',atributos=atributos)
        else:
            flask.session['aux1']=flask.request.form['nombre']
            flask.session['aux2']=flask.request.form['comentario']
            if(flask.request.form['nombre']==""):
                flask.flash("El campo nombre no puede estar vacio")
                return flask.render_template('crearTipo.html',atributos=atributos)
            if comprobarTipoItem(flask.request.form['nombre'],flask.session['faseid']):
                flask.flash("El tipo ya existe")
                return flask.render_template('crearTipo.html',atributos=atributos)
            crearTipoItem(flask.request.form['nombre'][:20],flask.request.form['comentario'][:100],flask.session['faseid'])
            idcreado=getTipoItemNombre(flask.request.form['nombre'][:20],flask.session['faseid'])
            for at in atributos:
                crearAtributo(at.nombre,at.tipoDato,flask.session['faseid'])
            flask.session.pop('aux1',None)
            flask.session.pop('aux2',None)
            flask.session.pop('aux3',None)
            flask.session.pop('aux4',None)
            return flask.redirect('/admfase/'+str(flask.session['faseid'])) 