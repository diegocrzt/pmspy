import flask.views
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase,actualizarFecha
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.entidad import Atributo,TipoItem, Rol, Relacion
from pms.modelo.relacionControlador import hijos, comprobarRelacion, crearRelacion,comprobarAprobar,copiarRelacionesEstable,desAprobarAdelante, desAprobar,eliminarRelacion
from pms.modelo.itemControlador import getItemsFiltrados, getItemsPaginados, peticionExiste, copiarValores, getItemsTipo,getItemId, comprobarItem, crearItem, crearValor, editarItem,eliminarItem,getItemEtiqueta,getVersionId,getVersionItem
from pms.modelo.peticionControlador import contarVotos, getMiembros, agregarVoto, enviarPeticion, crearPeticion, getPeticion, eliminarPeticion, editarPeticion, getVersionesItemParaSolicitud
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
    
    return flask.render_template('admEjecutarSolicitud.html',s=soli)

"""Fuciones de eliminar y crear relacion que si tienen que ser diferentes porque solo deben pasar los item de la solicitud
"""

@app.route('/admsolicitud/ejecutar/editaritem/<i>')
@pms.vista.required.login_required
def edItemSolicitud(i=None):
    iversion=getVersionId(i)
    flask.session['itemid']=i
    return flask.render_template('editarItem.html')
    
    
    
    
