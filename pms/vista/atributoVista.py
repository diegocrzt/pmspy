import flask.views
from flask import request
import pms.vista.required
from pms import app
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo, getAtributoNombreTipo, getAtributoId, eliminarAtributo
from pms.modelo.entidad import Atributo
from pms.modelo.faseControlador import actualizarFecha
@app.route('/admatributo/<t>')
@pms.vista.required.login_required
def admAtributo(t=None):
    """
    Funcion que llama a la Vista de Administrar Tipo de Item, responde al boton de 'Selec>>' de Administrar Fase
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None) 
    if request.method == "GET":
        tipo=getTipoItemId(t)
        flask.session.pop('tipoitemid',None)
        flask.session.pop('tipoitemnombre',None)
        flask.session['tipoitemid']=tipo.id
        flask.session['tipoitemnombre']=tipo.nombre
        a=tipo.atributos
        return flask.render_template('admAtributo.html',atributos=a)
    else:
        return flask.redirect(flask.url_for('admproyecto'))
    
    
    
class Crearatributo(flask.views.MethodView):
    """
    Gestiona la Vista de Crear atributo
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.render_template('crearAtributo.html')
    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['tipoDato']
        error=False
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            error=True
        if(flask.request.form['tipoDato']==""):
            flask.flash(u"El Tipo de dato no puede estar vacio","tipo")
            error=True
        if error:
            return flask.render_template('crearAtributo.html')
        if comprobarAtributo(flask.request.form['nombre'],flask.session['tipoitemid']):
            flask.flash(u"El atributo ya existe","nombre")
            return flask.render_template('crearAtributo.html')
        crearAtributo(flask.request.form['nombre'][:20],flask.request.form['tipoDato'][:100],flask.session['tipoitemid'])
        idcreado=getAtributoNombreTipo(flask.request.form['nombre'][:20],flask.session['tipoitemid'])
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        actualizarFecha(flask.session['faseid'])
        flask.flash(u"CREACION EXITOSA","text-success")
        return flask.redirect('/admatributo/'+str(flask.session['tipoitemid'])) 
    
class Eliminaratributo(flask.views.MethodView):
    """
    Vista de Eliminar Atributo
    """
    
    @pms.vista.required.login_required  
    def get(self):
        return flask.redirect('/admatributo/'+str(flask.session['tipoitemid'])) 
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Eliminar Fase
        """
        if(flask.session['atributoid']!=None):
            eliminarAtributo(flask.session['atributoid'])
            actualizarFecha(flask.session['faseid'])
            flask.flash(u"ELIMINACION EXITOSA","text-success")
            return flask.redirect('/admatributo/'+str(flask.session['tipoitemid'])) 
        else:
            return flask.redirect('/admatributo/'+str(flask.session['tipoitemid'])) 
        


    
@app.route('/admatributo/eliminar/<atr>')
@pms.vista.required.login_required       
def eAtributo(atr=None): 
    """
    Funcion que llama a la Vista de Eliminar Atributo, responde al boton de 'Eliminar' de Administrar Atributo
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)
    atributo=getAtributoId(atr)
    flask.session['atributoid']=atributo.id
    return flask.render_template('eliminarAtributo.html',a=atributo)           
    