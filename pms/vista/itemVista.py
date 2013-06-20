import flask.views
from flask import request
import pms.vista.required
from pms import app
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFase, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase,actualizarFecha
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.rolControlador import getRolesFase, comprobarUser_Rol
from pms.modelo.entidad import Atributo,TipoItem, Rol, Relacion
from pms.modelo.relacionControlador import hijos, comprobarRelacion, crearRelacion,comprobarAprobar,copiarRelacionesEstable,desAprobarAdelante, desAprobar,eliminarRelacion
from pms.modelo.itemControlador import getItemsFiltrados, getItemsPaginados, peticionExiste, copiarValores, getItemsTipo,getItemId, comprobarItem, crearItem, crearValor, editarItem,eliminarItem,getItemEtiqueta,getVersionId,getVersionItem, ejEliminarItem
from pms.modelo.rolControlador import getRolesDeUsuarioEnFase
from pms.modelo.peticionControlador import crearPeticion, buscarSolicitud
from pms.vista.paginar import calculoDeAnterior
from pms.vista.paginar import calculoDeSiguiente
from pms.vista.paginar import calculoPrimeraPag
from pms.modelo.usuarioControlador import getUsuarioById
TAM_PAGINA=5

@app.route('/admitem/<f>',methods=['POST', 'GET'])
@pms.vista.required.login_required
def admItem(f=None):
    """
    Funcion que llama a la Vista de Administrar Item, responde al boton de 'Selec>>' de Administrar Fase
    """
    if request.method == "GET":
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
            flask.session['filtro']=""
            
            cantidad=0
            t=fase.tipos
            for ti in t:
                cantidad=cantidad+len(ti.instancias)
            flask.session['cantidaditems']=cantidad       
            if flask.session['cambio']:
                flask.session['cambio']=False
                items=getItemsPaginados(flask.session['pagina']-1,TAM_PAGINA,fase)
                infopag=flask.session['infopag']
            else:
                flask.session['pagina']=1
                items=getItemsPaginados(flask.session['pagina']-1,TAM_PAGINA,fase)
                infopag=calculoPrimeraPag(cantidad)
            
            """t=fase.tipos
            i=[]
            for ti in t:
                itms=ti.instancias
                for it in itms:
                    aux=getVersionItem(it.id)
                    if aux.estado!="Eliminado":
                        i.append(aux)"""
            flask.session.pop('itemid',None)
            if fase.tipos:
                haytipos=True
            else:
                haytipos=False
            return flask.render_template('admItem.html',items=items,roles=roles, infopag=infopag, buscar=False, haytipos=haytipos)
        else:
            return flask.redirect(flask.url_for('admfase'))
    if request.method == "POST":
        if flask.request.form['fil']!="":
            global TAM_PAGINA
            flask.session['filtro']=flask.request.form['fil']
            cant=len(getItemsFiltrados(getFaseId(flask.session['faseid']),flask.session['filtro']))
            if 'buscar' in flask.request.form:
                flask.session['pagina']=1
                items=getItemsPaginados(flask.session['pagina']-1,TAM_PAGINA,getFaseId(flask.session['faseid']), flask.request.form['fil'])
                infopag=calculoPrimeraPag(cant)
            elif 'sgte' in flask.request.form:
                infopag=calculoDeSiguiente(cant)
                items=getItemsPaginados(flask.session['pagina']-1,TAM_PAGINA,getFaseId(flask.session['faseid']), flask.request.form['fil'])
            elif 'anterior' in flask.request.form:
                infopag=calculoDeAnterior(cant)
                items=getItemsPaginados(flask.session['pagina']-1,TAM_PAGINA,getFaseId(flask.session['faseid']), flask.request.form['fil'])
            roles = getRolesDeUsuarioEnFase(flask.session['usuarioid'], flask.session['faseid'])
            return flask.render_template('admItem.html',items=items,roles=roles, infopag=infopag, buscar=True)
        else:
            return flask.redirect('/admitem/'+str(flask.session['faseid']))
    
   
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
        flask.session['aux1']=flask.request.form['nombre'][:20]
        flask.session['aux2']=flask.request.form['costo']
        flask.session['aux3']=flask.request.form['dificultad']
        flask.session['aux4']=flask.request.form['tipo']
        if(flask.request.form['nombre'][:20]==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.render_template('crearItem.html')
        if(flask.request.form['costo']==""):
            flask.flash(u"El campo costo no puede estar vacio","costo")
            return flask.render_template('crearItem.html')
        if(flask.request.form['dificultad']==""):
            flask.flash(u"El campo dificultad no puede estar vacio","dificultad")
            return flask.render_template('crearItem.html')
        if comprobarItem(flask.request.form['nombre'][:20],flask.session['faseid']):
            flask.flash(u"El item ya existe", "nombre")
            return flask.render_template('crearItem.html')
        tipos=getTiposFase(flask.session['faseid'])
        c=1
        for t in tipos:
            for i in t.instancias:
                for v in i.version:
                    c=c+1
        etiqueta=str(flask.session['proyectoid'])+"-"+str(flask.session['faseid'])+"-"+str(c)
        crearItem(flask.request.form['tipo'],etiqueta,flask.request.form['nombre'][:20],"Activo",flask.request.form['costo'],flask.request.form['dificultad'],flask.session['usuarioid'])
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
        actualizarFecha(flask.session['faseid'])
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
        desAprobarAdelante(itm.id)
        flask.flash(u"EDICION EXITOSA","text-success")
        actualizarFecha(flask.session['faseid'])
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
        flask.session['aux1']=flask.request.form['nombre'][:20]
        flask.session['aux2']=flask.request.form['costo']
        flask.session['aux3']=flask.request.form['dificultad']
        if(flask.request.form['nombre'][:20]==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            v=getVersionItem(flask.session['itemid'])
            return flask.render_template('editarItem.html',i=v)
        if(flask.request.form['costo']==""):
            v=getVersionItem(flask.session['itemid'])
            flask.flash(u"El campo costo no puede estar vacio","costo")
            return flask.render_template('editarItem.html',i=v)
        if(flask.request.form['dificultad']==""):
            v=getVersionItem(flask.session['itemid'])
            flask.flash(u"El campo dificultad no puede estar vacio","dificultad")
            return flask.render_template('editarItem.html',i=v)
        if comprobarItem(flask.request.form['nombre'][:20],flask.session['faseid']):
            v=getVersionItem(flask.session['itemid'])
            flask.flash(u"El item ya existe", "nombre")
            return flask.render_template('editarItem.html',i=v)
        vvieja=getVersionItem(flask.session['itemid'])
        editarItem(flask.session['itemid'],flask.request.form['nombre'][:20],"Activo",flask.request.form['costo'],flask.request.form['dificultad'],flask.session['usuarioid'])
        item=getItemId(flask.session['itemid'])
        version=getVersionItem(item.id)
        copiarValores(vvieja.id,version.id)
        copiarRelacionesEstable(vvieja.id,version.id)
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        desAprobarAdelante(version.id)
        flask.flash(u"EDICION EXITOSA","text-success")
        buscarSolicitud(version.id)
        actualizarFecha(flask.session['faseid'])
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
            eliminarItem(flask.session['itemid'],flask.session['usuarioid'])
            item=getItemId(flask.session['itemid'])
            version=getVersionItem(item.id)
            copiarValores(vvieja.id,version.id)
            copiarRelacionesEstable(vvieja.id,version.id)
            desAprobarAdelante(version.id)
            flask.flash(u"ELIMINACION EXITOSA","text-success")
            actualizarFecha(flask.session['faseid'])
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
    return flask.render_template('consultarItem.html',i=ver,atributos=atr,valores=val,padres=padres,antecesores=antecesores,hijos=hijos,posteriores=posteriores)   

@app.route('/admitem/asignarhijo/<vid>')
@pms.vista.required.login_required
def aHijo(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    flask.session['hijo']=vid
    flask.session['itemnombre']=getVersionId(vid).nombre
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
    Funcion que ejecuta la asignacion de un hijo a un item, responde al boton de 'Asignar' de Asiganar Hijo
    """
    flask.session.pop('itemnombre',None)
    if crearRelacion(vid,flask.session['hijo'],"P-H"):
        flask.flash(u"Relacion creada con exito")
        if getVersionId(flask.session['hijo']).estado=="Aprobado":
            desAprobar(flask.session['hijo'])
            desAprobarAdelante(flask.session['hijo'])
        actualizarFecha(flask.session['faseid'])
        buscarSolicitud(flask.session['hijo'])
        return flask.redirect('/admitem/asignarhijo/'+str(flask.session['hijo']))
    else:
        flask.flash(u"La relacion que se intenta crear produce un conflicto y ha sido denegada")
        return flask.redirect('/admitem/asignarhijo/'+str(flask.session['hijo']))
    
@app.route('/admitem/asignarantecesor/<vid>')
@pms.vista.required.login_required
def aAntecesor(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Antecesor, responde al boton de 'Antecesor' de Administrar Item 
    """
    flask.session['antecesor']=vid
    if flask.session['fasenumero']>1:
        flask.session['itemnombre']=getVersionId(vid).nombre
        faseact=getFaseId(flask.session['faseid'])
        fase=getFase(faseact.numero-1, flask.session['proyectoid'])
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
    flask.session.pop('itemnombre',None)
    if crearRelacion(vid,flask.session['antecesor'],"A-S"):
        flask.flash(u"Relacion creada con exito")
        if getVersionId(flask.session['antecesor']).estado=="Aprobado":
            desAprobar(flask.session['antecesor'])
            desAprobarAdelante(flask.session['antecesor'])
        actualizarFecha(flask.session['faseid'])
        buscarSolicitud(flask.session['antecesor'])
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
    z=dict()
    for v in item.version:
        i.append(v)
        z[v.id]= getUsuarioById(v.usuario_modificador_id).nombre
    return flask.render_template('reversionarItem.html',versiones=i,usuarioMod=z)

@app.route('/admitem/reversionarb/<vid>')
@pms.vista.required.login_required
def bReversionar(vid=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    vvieja=getVersionId(vid)
    item=vvieja.item
    editarItem(item.id,vvieja.nombre,"Activo",vvieja.costo,vvieja.dificultad,usr=flask.session['usuarioid'])
    version=getVersionItem(item.id)
    copiarValores(vvieja.id,version.id)
    for rel in vvieja.ante_list:
        crearRelacion(rel.ante_id,version.id,rel.tipo)
    for rel in vvieja.post_list:
        crearRelacion(version.id,rel.post_id,rel.tipo)
    desAprobarAdelante(version.id)
    actualizarFecha(flask.session['faseid'])
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
    editarItem(item.id,vvieja.nombre,"Activo",vvieja.costo,vvieja.dificultad,flask.session['usuarioid'])
    version=getVersionItem(item.id)
    copiarValores(vvieja.id,version.id)
    for rel in vvieja.ante_list:
        crearRelacion(rel.ante_id,version.id,rel.tipo)
    for rel in vvieja.post_list:
        crearRelacion(version.id,rel.post_id,rel.tipo)
    desAprobarAdelante(version.id)
    actualizarFecha(flask.session['faseid'])
    return flask.redirect('/admitem/'+str(flask.session['faseid'])) 


@app.route('/admitem/aprobaritem/<vid>', methods=['POST', 'GET'])
@pms.vista.required.login_required
def aprobarItem(vid=None): 
    """
    Funcion que llama a la Vista de Aprobar item
    """
    
    vvieja=getVersionId(vid)
    item=vvieja.item
    if request.method == "GET":
        flask.session['itemid']=vid
        padres=[]
        antecesores=[]
        entrantes=vvieja.ante_list
        for rel in entrantes:
            itm=getVersionId(rel.ante_id)
            if itm.actual:
                if rel.tipo=="P-H":
                    padres.append(itm)
                else:
                    antecesores.append(itm)
        if comprobarAprobar(vid):
            return flask.render_template('aprobarItem.html',version=vvieja, padres=padres, ante=antecesores, a=True)
        else:
            return flask.render_template('aprobarItem.html',version=vvieja, padres=padres, ante=antecesores, a=False)
    if request.method == "POST":
        if "Aceptar" in flask.request.form:
            editarItem(item.id,vvieja.nombre,"Aprobado",vvieja.costo,vvieja.dificultad,flask.session['usuarioid'])
            version=getVersionItem(item.id)
            copiarValores(vvieja.id,version.id)
            copiarRelacionesEstable(vvieja.id,version.id)
            actualizarFecha(flask.session['faseid'])
            flask.flash(u"APROBACION EXITOSA","text-success")
            flask.session.pop('itemid',None)
            return flask.redirect('/admitem/'+str(flask.session['faseid'])) 
        if "Cancelar" in flask.request.form:
            flask.flash(u"APROBACION CANCELADA","text-error")
            flask.session.pop('itemid',None)
            return flask.redirect('/admitem/'+str(flask.session['faseid']))
        if "CancelarA" in flask.request.form:
            flask.session.pop('itemid',None)
            return flask.redirect('/admitem/'+str(flask.session['faseid']))
    
@app.route('/admitem/eliminarrel/<vid>')
@pms.vista.required.login_required
def eliminarRel(vid=None): 
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
    return flask.render_template('eliminarRelacion.html',padres=padres,antecesores=antecesores,hijos=hijos,sucesores=sucesores)   
       

@app.route('/admitem/eliminarrelb/<vid>')
@pms.vista.required.login_required
def eliminarRelb(vid=None): 
    """

    """
    flask.session.pop('itemnombre',None)
    eliminarRelacion(flask.session['idver'],vid)
    if getVersionId(vid).estado=="Aprobado":
        desAprobar(vid)
        desAprobarAdelante(vid)
    flask.flash(u"Relacion eliminada con exito")
    actualizarFecha(flask.session['faseid'])
    return flask.redirect('/admitem/eliminarrel/'+str(flask.session['idver']))

@app.route('/admitem/eliminarrelc/<vid>')
@pms.vista.required.login_required
def eliminarRelc(vid=None): 
    """

    """
    eliminarRelacion(vid,flask.session['idver'])
    if getVersionId(flask.session['idver']).estado=="Aprobado":
        desAprobar(flask.session['idver'])
        desAprobarAdelante(flask.session['idver'])
    flask.flash(u"Relacion eliminada con exito")
    actualizarFecha(flask.session['faseid'])
    return flask.redirect('/admitem/eliminarrel/'+str(flask.session['idver']))

    
@app.route('/admitem/nextitem/')
@pms.vista.required.login_required       
def nextPageI():
    """Responde al boton 'siguiente' de la paginacion de la lista de Items de AdmItem
    """
    flask.session['cambio']=True
    flask.session['infopag']=calculoDeSiguiente(flask.session['cantidaditems'])
    return flask.redirect('/admitem/'+str(flask.session['faseid']))   

@app.route('/admitem/previtem/')
@pms.vista.required.login_required       
def prevPageI():
    """Responde al boton 'anterior' de la paginacion de la lista de Items de AdmItem
    """
    flask.session['cambio']=True
    flask.session['infopag']=calculoDeAnterior(flask.session['cantidaditems'])
    return flask.redirect('/admitem/'+str(flask.session['faseid']))
    
    
    
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
            flask.flash(u"ELIMINACION EXITOSAA","text-success")
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
    return flask.render_template('ejecutarEliminarItem.html',i=ver, atributos=atr, valores=val)   

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