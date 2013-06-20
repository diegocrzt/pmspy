import flask.views
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase,actualizarFecha
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.entidad import Atributo,TipoItem, Rol, Relacion
from pms.modelo.relacionControlador import hijos, comprobarRelacion, crearRelacion,comprobarAprobar,copiarRelacionesEstable,desAprobarAdelante, desAprobar,eliminarRelacion
from pms.modelo.itemControlador import getItemsFiltrados, getItemsPaginados, peticionExiste, copiarValores, getItemsTipo,getItemId, comprobarItem, crearItem, crearValor, editarItem,eliminarItem,getItemEtiqueta,getVersionId,getVersionItem
from pms.modelo.peticionControlador import actualizarItemsSolicitud, contarVotos, getMiembros, agregarVoto, enviarPeticion, crearPeticion, getPeticion, eliminarPeticion, editarPeticion, getVersionesItemParaSolicitud
from datetime import datetime
import pms.vista.required
from pms.modelo.rolControlador import getProyectosDeUsuario
from pms import app
from pms.vista.paginar import calculoDeSiguiente, calculoDeAnterior, calculoPrimeraPag
TAM_PAGINA=5

@app.route('/admsolicitud/ejecutar/<s>')
@pms.vista.required.login_required
def AdmEjecutarSolicitud(s=None):
    soli=getPeticion(s)
    flask.session['solicitudid']=s
    #r=actualizarItemsSolicitud(flask.session['solicitudid'])
    return flask.render_template('admEjecutarSolicitud.html',s=soli)

"""Fuciones de eliminar y crear relacion que si tienen que ser diferentes porque solo deben pasar los item de la solicitud
"""

@app.route('/admsolicitud/ejecutar/editaritem/<i>')
@pms.vista.required.login_required
def edItemSolicitud(i=None):
    iversion=getVersionId(i)
    flask.session['itemid']=iversion.deitem
    return flask.render_template('editarItemSolicitud.html', i=iversion)
    
class EditarItemSolicitud(flask.views.MethodView):
    """
    Gestiona la Vista de Editar Tipo de Item
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect('/admsolicitud/ejecutar/'+str(flask.session['solicitudid'])) 

    @pms.vista.required.login_required
    def post(self):
        v=getVersionItem(flask.session['itemid'])
        
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['costo']
        flask.session['aux3']=flask.request.form['dificultad']
        
        faseid=v.item.tipoitem.fase.id
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.render_template('editarItemSolicitud.html',i=v)
        if(flask.request.form['costo']==""):
            flask.flash(u"El campo costo no puede estar vacio","costo")
            return flask.render_template('editarItemSolicitud.html',i=v)
        if(flask.request.form['dificultad']==""):
            flask.flash(u"El campo dificultad no puede estar vacio","dificultad")
            return flask.render_template('editarItemSolicitud.html',i=v)
        if comprobarItem(flask.request.form['nombre'],faseid):
            flask.flash(u"El item ya existe", "nombre")
            return flask.render_template('editarItemSolicitud.html',i=v)
        
        editarItem(flask.session['itemid'],flask.request.form['nombre'],"EnCambio",flask.request.form['costo'],flask.request.form['dificultad'])
        item=getItemId(flask.session['itemid'])
        version=getVersionItem(item.id)
        copiarValores(v.id,version.id)
        copiarRelacionesEstable(v.id,version.id)
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        #desAprobarAdelante(version.id)
        
        actualizarFecha(faseid)
        r=actualizarItemsSolicitud(flask.session['solicitudid'])
        if r:
            flask.flash(u"EDICION EXITOSA","text-success")
        else:
            flask.flash(u"error","text-warning")
        return flask.redirect('/admsolicitud/ejecutar/'+str(flask.session['solicitudid'])) 
    
    
