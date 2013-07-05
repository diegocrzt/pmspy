import flask.views
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase,actualizarFecha
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.entidad import Atributo,TipoItem, Rol, Relacion
from pms.modelo.relacionControlador import hijos, comprobarRelacion, crearRelacion,comprobarAprobar,copiarRelacionesEstable,desAprobarAdelante, desAprobar,eliminarRelacion
from pms.modelo.itemControlador import getItemsFiltrados, getItemsPaginados, copiarValores, getItemsTipo,getItemId, comprobarItem, crearItem, crearValor, editarItem,eliminarItem,getItemEtiqueta,getVersionId,getVersionItem, ejEliminarItem
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
        
        actualizarItemsSolicitud(flask.session['solicitudid'])
        flask.flash(u"EDICION EXITOSA","text-success")
        
        return flask.redirect('/admsolicitud/ejecutar/'+str(flask.session['solicitudid'])) 
    
    
@app.route('/admsolicitud/ejecutar/asignarpadre/<vid>')
@pms.vista.required.login_required
def aEjecutarAP(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    flask.session['hijo']=vid
    v=getVersionId(vid)
    flask.session['itemnombre']=v.nombre
    
    fase=getFaseId(v.item.tipoitem.fase.id)
    flask.session['fasenombre']=fase.nombre
    t=fase.tipos
    i=[]
    for ti in t:
        itms=ti.instancias
        for it in itms:
            aux=getVersionItem(it.id)
            if aux.estado!="Eliminado":
                if not comprobarRelacion(vid,aux.id):
                    if not comprobarRelacion(aux.id,vid):
                        i.append(aux)
    return flask.render_template('cRelPadreSolicitud.html',items=i)   


@app.route('/admsolicitud/ejecutar/asignarpadreb/<vid>')
@pms.vista.required.login_required
def auEjecutarAP(vid=None): 
    """
    Funcion que ejecuta la asignacion de un hijo a un item, responde al boton de 'Asignar' de Asiganar Hijo
    """
    flask.session.pop('itemnombre',None)
    if crearRelacion(vid,flask.session['hijo'],"P-H"):
        flask.flash(u"Relacion creada con exito")
        return flask.redirect('/admsolicitud/ejecutar/'+str(flask.session['solicitudid']))
    else:
        flask.flash(u"La relacion que se intenta crear produce un conflicto y ha sido denegada")
        return flask.redirect('/admsolicitud/ejecutar/asignarpadre/'+str(flask.session['hijo']))
    
    
@app.route('/admsolicitud/ejecutar/asignarante/<vid>')
@pms.vista.required.login_required
def aEjecutarAA(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    flask.session['hijo']=vid
    v=getVersionId(vid)
    flask.session['itemnombre']=v.nombre
    fase=getFaseId(v.item.tipoitem.fase.id)
    if fase.numero>1:
        fase=getFaseId(fase.id-1)
        flask.session['fasenombre']=fase.nombre
        t=fase.tipos
        i=[]
        for ti in t:
            itms=ti.instancias
            for it in itms:
                aux=getVersionItem(it.id)
                if aux.estado!="Eliminado":
                    if not comprobarRelacion(vid,aux.id):
                        if not comprobarRelacion(aux.id,vid):
                            i.append(aux)
        return flask.render_template('cRelPadreSolicitud.html',items=i)   
    else:
        soli=getPeticion(flask.session['solicitudid'])
        flask.flash(u"No se puede asignar antecesor en la fase 1")
        return flask.render_template('admEjecutarSolicitud.html',s=soli)

@app.route('/admsolicitud/ejecutar/asignaranteb/<vid>')
@pms.vista.required.login_required
def auEjecutarAA(vid=None): 
    """
    Funcion que ejecuta la asignacion de un hijo a un item, responde al boton de 'Asignar' de Asiganar Hijo
    """
    flask.session.pop('itemnombre',None)
    if crearRelacion(vid,flask.session['hijo'],"A-S"):
        flask.flash(u"Relacion creada con exito")
        return flask.redirect('/admsolicitud/ejecutar/'+str(flask.session['solicitudid']))
    else:
        flask.flash(u"La relacion que se intenta crear produce un conflicto y ha sido denegada")
        return flask.redirect('/admsolicitud/ejecutar/asignarpadre/'+str(flask.session['hijo']))
    
    
class EjecutarEliminaritem(flask.views.MethodView):
    """
    Vista de Eliminar item
    """
    
    @pms.vista.required.login_required  
    def get(self):
        return flask.redirect('/admitem/'+str(flask.session['faseid'])) 
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Eliminar Item
        """
        if(flask.session['itemid']!=None):
            vvieja=getVersionItem(flask.session['itemid'])
            ejEliminarItem(vvieja.id)
            flask.flash(u"ELIMINACION EXITOSA","text-success")
            return flask.redirect('/admsolicitud/ejecutar/'+str(flask.session['solicitudid']))
        else:
            return flask.redirect('/admsolicitud/ejecutar/'+str(flask.session['solicitudid']))
        


    
    
@app.route('/admsolicitud/ejecutar/eliminaritem/<i>')
@pms.vista.required.login_required       
def EjecutarEItem(i=None): 
    """
    
    """
    ver=getVersionId(i)
    item=getItemId(ver.deitem)
    flask.session['itemid']=item.id
    tipo=getTipoItemId(item.tipo)
    atr=tipo.atributos
    val=[]
    for at in ver.atributosnum:
        val.append(at)
    for at in ver.atributosstr:
        val.append(at)
    for at in ver.atributosbool:
        val.append(at)
    for at in ver.atributosdate:
        val.append(at)
    padres=[]
    antecesores=[]
    for n in ver.ante_list:
        if n.tipo=="P-H":
            aux=getVersionId(n.ante_id)
            if aux.actual==True:
                padres.append(aux)
        else:
            aux=getVersionId(n.ante_id)
            if aux.actual==True:
                antecesores.append(aux)
    hijos=[]
    posteriores=[]
    for n in ver.post_list:
        if n.tipo=="P-H":
            aux=getVersionId(n.post_id)
            if aux.actual==True:
                hijos.append(aux)
        else:
            aux=getVersionId(n.post_id)
            if aux.actual==True:
                posteriores.append(aux)
    return flask.render_template('ejecutarEliminarItem.html',i=ver, atributos=atr, valores=val,padres=padres,antecesores=antecesores,hijos=hijos,posteriores=posteriores)   

@app.route('/admsolicitud/ejecutar/eliminarrel/<vid>')
@pms.vista.required.login_required
def ejEliminarRel(vid=None): 
    """
    Funcion que llama a la Vista de Eliminar Relacion
    """
    flask.session['idver']=vid
    version=getVersionId(vid)
    flask.session['itemnombre']=version.nombre
    entrantes=version.ante_list
    salientes=version.post_list
    padres=[]
    antecesores=[]
    for rel in entrantes:
        itm=getVersionId(rel.ante_id)
        if itm.actual:
            if rel.tipo=="P-H":
                padres.append(itm)
            else:
                antecesores.append(itm)
    hijos=[]
    sucesores=[]
    for rel in salientes:
        itm=getVersionId(rel.post_id)
        if itm.actual:
            if rel.tipo=="P-H":
                hijos.append(itm)
            else:
                sucesores.append(itm)
    return flask.render_template('ejEliminarRelacion.html',padres=padres,antecesores=antecesores,hijos=hijos,sucesores=sucesores)   
       

@app.route('/admsolicitud/ejecutar/eliminarrelb/<vid>')
@pms.vista.required.login_required
def ejEliminarRelb(vid=None): 
    """

    """
    flask.session.pop('itemnombre',None)
    eliminarRelacion(flask.session['idver'],vid)
    flask.flash(u"Relacion eliminada con exito")
    return flask.redirect('/admsolicitud/ejecutar/eliminarrel/'+str(flask.session['idver']))

@app.route('/admsolicitud/ejecutar/eliminarrelc/<vid>')
@pms.vista.required.login_required
def ejEliminarRelc(vid=None): 
    """

    """
    eliminarRelacion(vid,flask.session['idver'])
    flask.flash(u"Relacion eliminada con exito")
    return flask.redirect('/admsolicitud/ejecutar/eliminarrel/'+str(flask.session['idver']))


class EjCompletarAtributo(flask.views.MethodView):
    """
    Gestiona la Vista de Completar Atributo
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect('/admitem/'+str(flask.session['faseid']))

    @pms.vista.required.login_required
    def post(self):
        itm1=getVersionItem(flask.session['itemid'])
        editarItem(flask.session['itemid'],itm1.nombre,itm1.estado,itm1.costo,itm1.dificultad,flask.session['usuarioid'])
        itm=getVersionItem(flask.session['itemid'])
        tipo=getTipoItemId(flask.session['tipoitemid'])
        for at in tipo.atributos:
            if at.tipoDato=="Booleano":
                if at.nombre in flask.request.form:
                    crearValor(at.id,itm.id,flask.request.form[at.nombre])
                else:
                    crearValor(at.id,itm.id,False)
            else:
                crearValor(at.id,itm.id,flask.request.form[at.nombre])
        copiarRelacionesEstable(itm1.id,itm.id)
        actualizarItemsSolicitud(flask.session['solicitudid'])
        flask.flash(u"EDICION EXITOSA","text-success")
        return flask.redirect('/admsolicitud/ejecutar/'+str(flask.session['solicitudid']))    

@app.route('/admsolicitud/ejecutar/atributo/<i>')
@pms.vista.required.login_required       
def ejComplAtributosItem(i=None): 
    ver=getVersionId(i)
    item=getItemId(ver.deitem)
    tipo=getTipoItemId(item.tipo)
    atr=tipo.atributos
    flask.session['tipoitemid']=tipo.id
    flask.session['itemid']=item.id
    val=[]
    for at in ver.atributosnum:
        val.append(at)
    for at in ver.atributosstr:
        val.append(at)
    for at in ver.atributosbool:
        val.append(at)
    for at in ver.atributosdate:
        val.append(at)
    return flask.render_template('ejCompletarAtributo.html',atributos=atr,valores=val)