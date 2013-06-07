import flask.views
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase,actualizarFecha
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.rolControlador import getRolesFase, comprobarUser_Rol
from pms.modelo.entidad import Atributo,TipoItem, Rol, Relacion
from pms.modelo.relacionControlador import hijos, comprobarRelacion, crearRelacion,comprobarAprobar,copiarRelacionesEstable,desAprobarAdelante, desAprobar,eliminarRelacion
from pms.modelo.itemControlador import getItemsFiltrados, getItemsPaginados, peticionExiste, copiarValores, getItemsTipo,getItemId, comprobarItem, crearItem, crearValor, editarItem,eliminarItem,getItemEtiqueta,getVersionId,getVersionItem
from datetime import datetime
import pms.vista.required
from pms.modelo.rolControlador import getProyectosDeUsuario
from pms import app
from pms.vista.paginar import calculoDeSiguiente, calculoDeAnterior, calculoPrimeraPag
TAM_PAGINA=5

@app.route('/admsolicitud/ejecutar/<s>')
@pms.vista.required.login_required
def AdmEjecutarSolicitud(s=None):
    #soli=getSolicitud(s)
    flask.session['solicitudid']=s
    flask.session['faseid']=1
    items=[]
    items.append("a")
    items.append("b")
    return flask.render_template('admEjecutarSolicitud.html',items=items)

"""Fuciones de eliminar y crear relacion que si tienen que ser diferentes porque solo deben pasar los item de la solicitud
"""


