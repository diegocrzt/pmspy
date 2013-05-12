import flask.views
from flask import request
import pms.vista.required
from pms import app
from pms.modelo.tipoItemControlador import getAllTiposItem, getTiposItemFiltrados,getTiposItemPaginados, getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase
from pms.modelo.rolControlador import getRolesFase,  comprobarUser_Rol
from pms.modelo.atributoControlador import crearAtributo, comprobarAtributo
from pms.modelo.entidad import Atributo,TipoItem, Rol
from pms.modelo.itemControlador import getVersionItem
from pms.modelo.rolControlador import getRolesDeUsuarioEnFase
from pms.vista.paginar import calculoDeAnterior
from pms.vista.paginar import calculoDeSiguiente
from pms.vista.paginar import calculoPrimeraPag
TAM_PAGINA=5


class AdmTipo(flask.views.MethodView):
    """
    Funcion que llama a la Vista de Administrar Tipo de Item, responde al boton de 'Selec>>' de Administrar Fase
    """
    @pms.vista.required.login_required
    def get(self):
        if flask.session['faseid']!=None:
            flask.session.pop('aux1',None)
            flask.session.pop('aux2',None)
            flask.session.pop('aux3',None)
            flask.session.pop('aux4',None)
            fase=getFaseId(flask.session['faseid'])
            flask.session.pop('faseid',None)
            flask.session.pop('fasenombre',None)
            flask.session['faseid']=fase.id
            flask.session['fasenombre']=fase.nombre 
            roles=getRolesDeUsuarioEnFase(flask.session['usuarioid'], flask.session['faseid'])
           
            flask.session['filtro']=""
            
            if flask.session['cambio']:
                flask.session['cambio']=False
                tipos=getTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA,fase.id)
                infopag=flask.session['infopag']
            else:
                flask.session['pagina']=1
                tipos=getTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA,fase.id)
                infopag=calculoPrimeraPag(getTiposFase(fase.id).count())
            return flask.render_template('admTipo.html',tipos=tipos,infopag=infopag, buscar=False, roles=roles)
    
    @pms.vista.required.login_required
    def post(self):
        if flask.request.form['fil']!="":
            global TAM_PAGINA
            flask.session['filtro']=flask.request.form['fil']
            cant=getTiposItemFiltrados(flask.session['filtro'],flask.session['faseid']).count()
            if 'buscar' in flask.request.form:
                
                flask.session['pagina']=1
                p=getTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA,flask.session['faseid'], flask.request.form['fil'])
                infopag=calculoPrimeraPag(cant)
            elif 'sgte' in flask.request.form:
                infopag=calculoDeSiguiente(cant)
                p=getTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA,flask.session['faseid'], flask.request.form['fil'])
            elif 'anterior' in flask.request.form:
                infopag=calculoDeAnterior(cant)
                p=getTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA,flask.session['faseid'], flask.request.form['fil'])
                    
            return flask.render_template('admTipo.html',tipos=p,infopag=infopag,buscar=True)
        else:
            return flask.redirect('/admtipo/')
    
    
    
class Creartipo(flask.views.MethodView):
    """
    Gestiona la Vista de Crear tipo
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.render_template('crearTipo.html')
    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['comentario']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.render_template('crearTipo.html')
        if comprobarTipoItem(flask.request.form['nombre'],flask.session['faseid']):
            flask.flash(u"El tipo ya existe", "nombre")
            return flask.render_template('crearTipo.html')
        crearTipoItem(flask.request.form['nombre'][:20],flask.request.form['comentario'][:100],flask.session['faseid'])
        idcreado=getTipoItemNombre(flask.request.form['nombre'][:20],flask.session['faseid'])
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.flash(u"CREACION EXITOSA","text-success")
        return flask.redirect('/admtipo/'+str(flask.session['faseid'])) 

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
            return flask.redirect('/admtipo/editartipo/'+str(flask.session['tipoitemid']))
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
        
@app.route('/admtipo/<f>')
@pms.vista.required.login_required
def admTipo(f=None):
    fase=getFaseId(f)
    flask.session.pop('faseid',None)
    flask.session.pop('fasenombre',None)
    flask.session['faseid']=fase.id
    flask.session['fasenombre']=fase.nombre
    return flask.redirect('/admtipo/')
    

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
    versiones=[]
    for i in tipo.instancias:
        versiones.append(getVersionItem(i.id))
    return flask.render_template('consultarTipo.html',t=tipo, versiones=versiones)   


@app.route('/admtipo/nexttipo/')
@pms.vista.required.login_required       
def nextPageT():
    
    flask.session['cambio']=True
    cantT=getTiposFase(flask.session['faseid']).count()
    flask.session['infopag']=calculoDeSiguiente(cantT)
    return flask.redirect('/admtipo/'+str(flask.session['faseid']))   

@app.route('/admtipo/prevtipo/')
@pms.vista.required.login_required       
def prevPageT():
    flask.session['cambio']=True
    flask.session['infopag']=calculoDeAnterior(getTiposFase(flask.session['faseid']).count())
    return flask.redirect('/admtipo/'+str(flask.session['faseid']))

@app.route('/admtipo/importar/<f>')
@pms.vista.required.login_required   
def importar(f=None):
    flask.session['faseid']=f
    tipos=getAllTiposItem(flask.session['faseid'])
    tiposcopiar=getTiposFase(flask.session['faseid'])
    return flask.render_template('importar.html',tipos=tipos, tiposcopiar=tiposcopiar)

@app.route('/admtipo/importartipo/<t>')
@pms.vista.required.login_required   
def cambiarNombreTipo(t=None):
    """Llama al importarTipoItem.html para cambiar el nombre del tipo de item que se desea importar o copiar
    """ 
    tipo=getTipoItemId(t)
    return flask.render_template('importarTipoItem.html',tipo=tipo)
    
    

class ImportarTipo(flask.views.MethodView):
    
    @pms.vista.required.login_required
    def post(self):
        
        tipos=getAllTiposItem(flask.session['faseid'])
        return flask.render_template('importar.html',tipos=tipos)
