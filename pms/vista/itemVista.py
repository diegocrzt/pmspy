import flask.views
from flask import request
import pms.vista.required
from pms import app
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.rolControlador import getRolesFase, comprobarUser_Rol
from pms.modelo.entidad import Atributo,TipoItem, Rol, Relacion
from pms.modelo.relacionControlador import comprobarRelacion, crearRelacion, comprobarAprobar,copiarRelacionesEstable
from pms.modelo.itemControlador import copiarValores, getItemsTipo,getItemId, comprobarItem, crearItem, crearValor, editarItem,eliminarItem,getItemEtiqueta,getVersionId,getVersionItem
from pms.modelo.rolControlador import getRolesDeUsuarioEnFase


@app.route('/admitem/<f>')
@pms.vista.required.login_required
def admItem(f=None):
    """
    Funcion que llama a la Vista de Administrar Item, responde al boton de 'Selec>>' de Administrar Fase
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None) 
    if request.method == "GET":
        fase=getFaseId(f)
        flask.session.pop('faseid',None)
        flask.session.pop('fasenombre',None)
        flask.session['faseid']=fase.id
        flask.session['fasenumero']=fase.numero
        flask.session['fasenombre']=fase.nombre
        roles = getRolesDeUsuarioEnFase(flask.session['usuarioid'], flask.session['faseid'])
        t=fase.tipos
        i=[]
        for ti in t:
            itms=ti.instancias
            for it in itms:
                aux=getVersionItem(it.id)
                if aux.estado!="Eliminado":
                    i.append(aux)
        flask.session.pop('itemid',None)
        return flask.render_template('admItem.html',items=i,roles=roles)
    else:
        return flask.redirect(flask.url_for('admfase'))
    
    
   
class CrearItem(flask.views.MethodView):
    """
    Gestiona la Vista de Crear item
    """
    @pms.vista.required.login_required
    def get(self):
        tipos=getTiposFase(flask.session['faseid'])
        return flask.render_template('crearItem.html',tipos=tipos)
    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['costo']
        flask.session['aux3']=flask.request.form['dificultad']
        flask.session['aux4']=flask.request.form['tipo']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.render_template('crearItem.html')
        if(flask.request.form['costo']==""):
            flask.flash(u"El campo costo no puede estar vacio","costo")
            return flask.render_template('crearItem.html')
        if(flask.request.form['dificultad']==""):
            flask.flash(u"El campo dificultad no puede estar vacio","dificultad")
            return flask.render_template('crearItem.html')
        if comprobarItem(flask.request.form['nombre'],flask.session['faseid']):
            flask.flash(u"El item ya existe", "nombre")
            return flask.render_template('crearItem.html')
        tipos=getTiposFase(flask.session['faseid'])
        c=1
        for t in tipos:
            for i in t.instancias:
                for v in i.version:
                    c=c+1
        etiqueta=str(flask.session['proyectoid'])+"-"+str(flask.session['faseid'])+"-"+str(c)
        crearItem(flask.request.form['tipo'],etiqueta,flask.request.form['nombre'],"activo",flask.request.form['costo'],flask.request.form['dificultad'])
        tipo=getTipoItemId(flask.request.form['tipo'])
        creado=getItemEtiqueta(etiqueta)
        version=getVersionItem(creado.id)
        for a in tipo.atributos:
            crearValor(a.id,version.id,None)
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        flask.flash(u"CREACION EXITOSA","text-success")
        return flask.redirect('/admitem/'+str(flask.session['faseid'])) 
    
class CompletarAtributo(flask.views.MethodView):
    """
    Gestiona la Vista de Completar Atributo
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect('/admitem/'+str(flask.session['faseid']))

    @pms.vista.required.login_required
    def post(self):
        itm1=getVersionItem(flask.session['itemid'])
        editarItem(flask.session['itemid'],itm1.nombre,itm1.estado,itm1.costo,itm1.dificultad)
        itm=getVersionItem(flask.session['itemid'])
        tipo=getTipoItemId(flask.session['tipoitemid'])
        for at in tipo.atributos:
            crearValor(at.id,itm.id,flask.request.form[at.nombre])
        copiarRelacionesEstable(itm1.id,itm.id)
        flask.flash(u"EDICION EXITOSA","text-success")
        return flask.redirect('/admitem/'+str(flask.session['faseid']))    

@app.route('/admitem/atributo/<i>')
@pms.vista.required.login_required       
def complAtributosItem(i=None): 
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
    return flask.render_template('completarAtributo.html',atributos=atr,valores=val) 

class EditarItem(flask.views.MethodView):
    """
    Gestiona la Vista de Editar Tipo de Item
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect('/admitem/'+str(flask.session['faseid'])) 

    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['costo']
        flask.session['aux3']=flask.request.form['dificultad']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.render_template('editarItem.html')
        if(flask.request.form['costo']==""):
            flask.flash(u"El campo costo no puede estar vacio","costo")
            return flask.render_template('editarItem.html')
        if(flask.request.form['dificultad']==""):
            flask.flash(u"El campo dificultad no puede estar vacio","dificultad")
            return flask.render_template('editarItem.html')
        if comprobarItem(flask.request.form['nombre'],flask.session['faseid']):
            flask.flash(u"El item ya existe", "nombre")
            return flask.render_template('editarItem.html')
        vvieja=getVersionItem(flask.session['itemid'])
        editarItem(flask.session['itemid'],flask.request.form['nombre'],"activo",flask.request.form['costo'],flask.request.form['dificultad'])
        item=getItemId(flask.session['itemid'])
        version=getVersionItem(item.id)
        copiarValores(vvieja.id,version.id)
        copiarRelacionesEstable(vvieja.id,version.id)
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        flask.flash(u"EDICION EXITOSA","text-success")
        return flask.redirect('/admitem/'+str(flask.session['faseid'])) 
    
@app.route('/admitem/editaritem/<t>')
@pms.vista.required.login_required       
def edItem(t=None): 
    ver=getVersionId(t)
    #item=getItemId(t)
    flask.session['itemid']=ver.deitem
    return flask.render_template('editarItem.html',i=ver) 

   
class Eliminaritem(flask.views.MethodView):
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
            eliminarItem(flask.session['itemid'])
            item=getItemId(flask.session['itemid'])
            version=getVersionItem(item.id)
            copiarValores(vvieja.id,version.id)
            copiarRelacionesEstable(vvieja.id,version.id)
            flask.flash(u"ELIMINACION EXITOSA","text-success")
            return flask.redirect('/admitem/'+str(flask.session['faseid'])) 
        else:
            return flask.redirect('/admitem/'+str(flask.session['faseid'])) 
        


    
    
@app.route('/admitem/eliminaritem/<i>')
@pms.vista.required.login_required       
def eItem(i=None): 
    """
    Funcion que llama a la Vista de Eliminar Item, responde al boton de 'Eliminar' de Administrar Item
    recibe el id del item a eliminarse
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
    return flask.render_template('eliminarItem.html',i=ver, atributos=atr, valores=val)   

@app.route('/admitem/consultaritem/<i>')
@pms.vista.required.login_required
def consultarItem(i=None):
    """
    Funcion que despliega pagina de consulta de item, llama a consultarItem.html
    recibe el id del item a consultar
    """
    ver=getVersionId(i)
    item=getItemId(ver.deitem)
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
    return flask.render_template('consultarItem.html',i=ver,atributos=atr,valores=val)   

@app.route('/admitem/asignarhijo/<vid>')
@pms.vista.required.login_required
def aHijo(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    flask.session['hijo']=vid
    fase=getFaseId(flask.session['faseid'])
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
    return flask.render_template('crearRelacionHijo.html',items=i)   


@app.route('/admitem/asignar/<vid>')
@pms.vista.required.login_required
def auHijo(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    if crearRelacion(vid,flask.session['hijo'],"P-H"):
        flask.flash(u"Relacion creada con exito")
        return flask.redirect('/admitem/asignarhijo/'+str(flask.session['hijo']))
    else:
        flask.flash(u"La relacion que se intenta crear produce un conflicto y ha sido denegada")
        return flask.redirect('/admitem/asignarhijo/'+str(flask.session['hijo']))
    
@app.route('/admitem/asignarantecesor/<vid>')
@pms.vista.required.login_required
def aAntecesor(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    flask.session['antecesor']=vid
    if flask.session['fasenumero']>1:
        fase=getFaseId(flask.session['faseid']-1)
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
        return flask.render_template('crearRelacionAntecesor.html',items=i)   
    else:
        return flask.redirect('/admitem/'+str(flask.session['faseid']))
       

@app.route('/admitem/asignarante/<vid>')
@pms.vista.required.login_required
def auAntecesor(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    if crearRelacion(vid,flask.session['antecesor'],"A-S"):
        flask.flash(u"Relacion creada con exito")
        return flask.redirect('/admitem/asignarantecesor/'+str(flask.session['antecesor']))
    else:
        flask.flash(u"La relacion que se intenta crear produce un conflicto y ha sido denegada")
        return flask.redirect('/admitem/asignarantecesor/'+str(flask.session['antecesor']))
    
@app.route('/admitem/reversionar/<iid>')
@pms.vista.required.login_required
def aReversionar(iid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    flask.session['itemid']=iid
    ver=getVersionId(iid)
    item=ver.item
    i=[]
    for v in item.version:
        i.append(v)
    return flask.render_template('reversionarItem.html',versiones=i)

@app.route('/admitem/reversionarb/<vid>')
@pms.vista.required.login_required
def bReversionar(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    vvieja=getVersionId(vid)
    item=vvieja.item
    editarItem(item.id,vvieja.nombre,"activo",vvieja.costo,vvieja.dificultad)
    version=getVersionItem(item.id)
    copiarValores(vvieja.id,version.id)
    for rel in vvieja.ante_list:
        crearRelacion(vvieja.id,version.id,rel.tipo)
    for rel in vvieja.post_list:
        crearRelacion(version.id,vvieja.id,rel.tipo)
    return flask.redirect('/admitem/reversionar/'+str(flask.session['itemid']))


@app.route('/admitem/revivir/<f>')
@pms.vista.required.login_required
def revivirItem(f=None):
    """
    Funcion que llama a la Vista de Revivir Item, responde al boton de 'Selec>>' de Administrar Fase
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None) 
    if request.method == "GET":
        fase=getFaseId(f)
        flask.session.pop('faseid',None)
        flask.session.pop('fasenombre',None)
        flask.session['faseid']=fase.id
        flask.session['fasenumero']=fase.numero
        flask.session['fasenombre']=fase.nombre
        t=fase.tipos
        i=[]
        for ti in t:
            itms=ti.instancias
            for it in itms:
                aux=getVersionItem(it.id)
                if aux.estado=="Eliminado":
                    i.append(aux)
        
        return flask.render_template('revivirItem.html',items=i)
    else:
        return flask.redirect(flask.url_for('admfase'))
    
@app.route('/admitem/revivirb/<vid>')
@pms.vista.required.login_required
def bRevivir(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    vvieja=getVersionId(vid)
    item=vvieja.item
    editarItem(item.id,vvieja.nombre,"activo",vvieja.costo,vvieja.dificultad)
    version=getVersionItem(item.id)
    copiarValores(vvieja.id,version.id)
    for rel in vvieja.ante_list:
        crearRelacion(vvieja.id,version.id,rel.tipo)
    for rel in vvieja.post_list:
        crearRelacion(version.id,vvieja.id,rel.tipo)
    return flask.redirect('/admitem/'+str(flask.session['faseid'])) 


@app.route('/admitem/aprobaritem/<vid>')
@pms.vista.required.login_required
def aprobarItem(vid=None): 
    """
    Funcion que llama a la Vista de Aprobar item
    """
    vvieja=getVersionId(vid)
    item=vvieja.item
    if comprobarAprobar(vid):
        editarItem(item.id,vvieja.nombre,"aprobado",vvieja.costo,vvieja.dificultad)
        version=getVersionItem(item.id)
        copiarValores(vvieja.id,version.id)
        copiarRelacionesEstable(vvieja.id,version.id)
        return flask.redirect('/admitem/'+str(flask.session['faseid'])) 
    else:
        return flask.redirect('/admitem/'+str(flask.session['faseid']))