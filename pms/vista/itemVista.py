import flask.views
from flask import request
import pms.vista.required
from pms import app
from pms.modelo.tipoItemControlador import getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.entidad import Atributo,TipoItem
from pms.modelo.itemControlador import getItemsTipo,getItemId, comprobarItem, crearItem, crearValor, editarItem,eliminarItem,getItemEtiqueta,getVersionId,getVersionItem



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
        flask.session['fasenombre']=fase.nombre
        t=fase.tipos
        i=[]
        for ti in t:
            itms=ti.instancias
            for it in itms:
                aux=getVersionItem(it.id)
                i.append(aux)
        
        return flask.render_template('admItem.html',items=i)
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
            return flask.render_template('crearTipo.html')
        tipos=getTiposFase(flask.session['faseid'])
        c=1
        for t in tipos:
            for i in t.instancias:
                for v in i.version:
                    c=c+1
        etiqueta=str(flask.session['proyectoid'])+str(flask.session['faseid'])+str(c)
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
        itm=getVersionItem(flask.session['itemid'])
        editarItem(flask.session['itemid'],itm.nombre,itm.estado,itm.costo,itm.dificultad)
        itm=getVersionItem(flask.session['itemid'])
        tipo=getTipoItemId(flask.session['tipoitemid'])
        for at in tipo.atributos:
            crearValor(at.id,itm.id,flask.request.form[at.nombre])
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
'''
class Editartipo(flask.views.MethodView):
    """
    Gestiona la Vista de Editar Tipo de Item
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect('/admtipo/'+str(flask.session['faseid']))

    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['comentario']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.render_template('editarTipo.html')
        editarTipoItem(flask.session['tipoitemid'],flask.request.form['nombre'][:20],flask.request.form['comentario'][:100],flask.session['faseid'])
        idcreado=getTipoItemNombre(flask.request.form['nombre'][:20],flask.session['faseid'])
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.flash(u"EDICION EXITOSA","text-success")
        return flask.redirect('/admtipo/'+str(flask.session['faseid']))
    
class Eliminartipo(flask.views.MethodView):
    """
    Vista de Eliminar Atributo
    """
    
    @pms.vista.required.login_required  
    def get(self):
        return flask.redirect('/admtipo/'+str(flask.session['faseid'])) 
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Eliminar Fase
        """
        if(flask.session['tipoitemid']!=None):
            eliminarTipoItem(flask.session['tipoitemid'])
            flask.flash(u"ELIMINACION EXITOSA","text-success")
            return flask.redirect('/admtipo/'+str(flask.session['faseid'])) 
        else:
            return flask.redirect('/admtipo/'+str(flask.session['faseid'])) 
        

@app.route('/admtipo/editartipo/<t>')
@pms.vista.required.login_required       
def edTipoItem(t=None): 
    tipo=getTipoItemId(t)
    flask.session['tipoitemid']=tipo.id
    return flask.render_template('editarTipo.html',t=tipo) 
    
    
@app.route('/admtipo/eliminar/<t>')
@pms.vista.required.login_required       
def eTipoItem(t=None): 
    """
    Funcion que llama a la Vista de Eliminar Tipo de Item, responde al boton de 'Eliminar' de Administrar Item
    recibe el id del tipo de item a eliminarce
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    tipo=getTipoItemId(t)
    flask.session['tipoitemid']=tipo.id
    return flask.render_template('eliminarTipo.html',t=tipo)   

@app.route('/admtipo/consultartipo/<t>')
@pms.vista.required.login_required
def consultarTipoItem(t=None):
    """
    Funcion que despliega pagina de consulta de tipo de item, llama a consultarTipo.html
    recibe el id del tipo de item a consultar
    """
    tipo=getTipoItemId(t)
    return flask.render_template('consultarTipo.html',t=tipo)   
'''