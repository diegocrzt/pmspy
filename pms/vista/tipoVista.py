import flask.views
from flask import request
import pms.vista.required
from pms import app
from pms.modelo.tipoItemControlador import getAllTipoFiltrados, getAllTiposItem, getAllTiposItemPaginados, getTiposItemFiltrados,getTiposItemPaginados, getTiposFase, getTipoItemId, getTipoItemNombre, comprobarTipoItem, crearTipoItem, editarTipoItem, eliminarTipoItem
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase,actualizarFecha
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
        """Devuelve la lista paginada de todos los Tipos de Items de la fase 
        """
        if flask.session['faseid']!=None:
            flask.session.pop('aux1',None)
            flask.session.pop('aux2',None)
            flask.session.pop('aux3',None)
            flask.session.pop('aux4',None)
            flask.session.pop('enimportar',None)
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
        """Devuelve la lista paginada de todos los Tipos de Item de la fase filtrados por la busqueda
        """
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
        """
        Funcion que despliega la vista de Crear Tipo de Item, llama a crearTipo.html 
        responde al boton 'Crear' de Administrar Tipo de Item
        """
        return flask.render_template('crearTipo.html')
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de crear un nuevo tipo de item, controlando previamente que los campos obligatorios no esten vacios
        y que no exista ya un tipo con dicho nombre
        """
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
        actualizarFecha(flask.session['faseid'])
        return flask.redirect('/admtipo/'+str(flask.session['faseid'])) 

class Editartipo(flask.views.MethodView):
    """
    Gestiona la Vista de Editar Tipo de Item
    """
    @pms.vista.required.login_required
    def get(self):
        """
        Esta funcion solo evita errores de url no encontrado para el caso en que se introduzca el url /admtipo/editartipo/
        el cual no devuelve ningun resultado, para ello se redirecciona a la vista de Administrar Tipo de Item
        """
        return flask.redirect('/admtipo/'+str(flask.session['faseid']))

    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de editar el tipo de item controlando previamente que el campo nombre no este vacio 
        y que no exista ya un tipo con dicho nombre
        """
        flask.session['aux1']=flask.request.form['nombre']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            tipo=getTipoItemId(flask.session['tipoitemid'])
            return flask.render_template('editarTipo.html',t=tipo)
        if comprobarTipoItem(flask.request.form['nombre'],flask.session['faseid']):
            flask.flash(u"El tipo ya existe", "nombre")
            tipo=getTipoItemId(flask.session['tipoitemid'])
            return flask.render_template('editarTipo.html',t=tipo)
        editarTipoItem(flask.session['tipoitemid'],flask.request.form['nombre'][:20],flask.request.form['comentario'][:100],flask.session['faseid'])
        idcreado=getTipoItemNombre(flask.request.form['nombre'][:20],flask.session['faseid'])
        flask.session.pop('aux1',None)
        flask.flash(u"EDICION EXITOSA","text-success")
        actualizarFecha(flask.session['faseid'])
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
        Ejecuta la funcion de Eliminar la Fase
        """
        if(flask.session['tipoitemid']!=None):
            eliminarTipoItem(flask.session['tipoitemid'])
            flask.flash(u"ELIMINACION EXITOSA","text-success")
            actualizarFecha(flask.session['faseid'])
            return flask.redirect('/admtipo/'+str(flask.session['faseid'])) 
        else:
            return flask.redirect('/admtipo/'+str(flask.session['faseid'])) 
        
class ImportarTipo(flask.views.MethodView):
    """
    Realiza la operacion de crear un nuevo tipo de item a partir del seleccionado previamente en admImportar y 
    cambiado de nombre en importarTipoItem.html
    """
    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['comentario']
        tipo=getTipoItemId(flask.session['tipoitemid'])
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.render_template('importarTipoItem.html',tipo=tipo)
        if comprobarTipoItem(flask.request.form['nombre'],flask.session['faseid']):
            flask.flash(u"El tipo ya existe", "nombre")
            return flask.render_template('importarTipoItem.html',tipo=tipo)
        crearTipoItem(flask.request.form['nombre'][:20],flask.request.form['comentario'][:100],flask.session['faseid'])
        idcreado=getTipoItemNombre(flask.request.form['nombre'][:20],flask.session['faseid']).id
        for a in tipo.atributos:
            crearAtributo(a.nombre,a.tipoDato,idcreado)
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.flash(u"IMPORTACION EXITOSA","text-success")
        actualizarFecha(flask.session['faseid'])
        return flask.redirect('/admtipo/importar/'+str(flask.session['faseid']))         

class AdmImportar(flask.views.MethodView):
    """Vista de Importar Tipo, pagina y filtra los Tipos de de Item
    """
    @pms.vista.required.login_required
    def get(self):
        """Devuelve la lista paginada de todos los Tipos de Items existentes
        """
        if flask.session['faseid']!=None:
            f=int(flask.session['faseid'])
            flask.session['enimportar']=True
            if flask.session['cambio']:
                flask.session['cambio']=False
                tipos=getAllTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA,None)
                infopag=flask.session['infopag']
            else:
                flask.session['pagina']=1
                tipos=getAllTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA, None)
                infopag=calculoPrimeraPag(getAllTiposItem().count())
            return flask.render_template('importar.html',tipos=tipos, faseid=f, infopag=infopag, buscar=False)
    @pms.vista.required.login_required
    def post(self):
        """Devuelve la lista paginada de todos los Tipos de Item existentes filtrados por la busqueda
        """
        if flask.request.form['fil']!="":
            global TAM_PAGINA
            f=int(flask.session['faseid'])
            flask.session['filtro']=flask.request.form['fil']
            cant=getAllTipoFiltrados(flask.session['filtro']).count()
            if 'buscar' in flask.request.form:
                flask.session['pagina']=1
                tipos=getAllTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA, flask.request.form['fil'])
                infopag=calculoPrimeraPag(cant)
            elif 'sgte' in flask.request.form:
                infopag=calculoDeSiguiente(cant)
                tipos=getAllTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA, flask.request.form['fil'])
            elif 'anterior' in flask.request.form:
                infopag=calculoDeAnterior(cant)
                tipos=getAllTiposItemPaginados(flask.session['pagina']-1,TAM_PAGINA, flask.request.form['fil'])
                    
            return flask.render_template('importar.html',tipos=tipos, faseid=f, infopag=infopag, buscar=True)
        else:
            flask.session['filtro']=""
            return flask.redirect('/admtipo/admimportartipo/')
@app.route('/admtipo/<f>')
@pms.vista.required.login_required
def admTipo(f=None):
    """
    Funcion que llama a al gestor de la vista de Administrar Tipo de Item
    revibe el id de la fase y lo guarda en una variable de sesion
    """
    fase=getFaseId(f)
    flask.session.pop('faseid',None)
    flask.session.pop('fasenombre',None)
    flask.session['faseid']=fase.id
    flask.session['fasenombre']=fase.nombre
    return flask.redirect('/admtipo/')
    
@app.route('/admtipo/editartipo/<t>')
@pms.vista.required.login_required       
def edTipoItem(t=None): 
    """
    Funcion que llama a la Vista de Editar Tipo de Item, responde al boton de 'Eliminar' de Administrar Tipo de Item
    recibe el id del tipo de item a eliminarce
    """
    tipo=getTipoItemId(t)
    flask.session['tipoitemid']=tipo.id
    flask.session['aux1']=tipo.nombre
    return flask.render_template('editarTipo.html',t=tipo) 
    
@app.route('/admtipo/eliminar/<t>')
@pms.vista.required.login_required       
def eTipoItem(t=None): 
    """
    Funcion que despliega la Vista de Eliminar Tipo de Item, llama a eliminarTipo.html 
    responde al boton de 'Eliminar' de Administrar Tipo de Item
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
    Funcion que despliega pagina de consulta de Tipo de Item, llama a consultarTipo.html
    responde al boton de 'Consultar' de Administrar Tipo de Item
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
    """Responde al boton 'siguiente' de la paginacion de la lista de Tipos de Items de AdmTipoItem
    """
    flask.session['cambio']=True
    cantT=getTiposFase(flask.session['faseid']).count()
    flask.session['infopag']=calculoDeSiguiente(cantT)
    return flask.redirect('/admtipo/'+str(flask.session['faseid']))   

@app.route('/admtipo/prevtipo/')
@pms.vista.required.login_required       
def prevPageT():
    """Responde al boton 'anterior' de la paginacion de la lista de Tipos de Items de AdmTipoItem
    """
    flask.session['cambio']=True
    flask.session['infopag']=calculoDeAnterior(getTiposFase(flask.session['faseid']).count())
    return flask.redirect('/admtipo/'+str(flask.session['faseid']))

@app.route('/admtipo/importartipo/<t>')
@pms.vista.required.login_required   
def cambiarNombreTipo(t=None):
    """
    Funcion que despliega la Vista de Cambiar Nombre de Tipo, llama al importarTipoItem.html para cambiar 
    el nombre del tipo de item que se desea importar o copiar
    responde al boton 'Importar' o 'Copiar' de admImportar
    """ 
    flask.session['tipoitemid']=t
    tipo=getTipoItemId(t)
    flask.session['aux1']=tipo.nombre
    flask.session['aux2']=tipo.comentario
    return flask.render_template('importarTipoItem.html',tipo=tipo)
    
@app.route('/admtipo/importar/nexttipo/')
@pms.vista.required.login_required       
def nextPageImp():
    """Responde al boton 'siguiente' de la paginacion de la lista de Tipos de Items para importar
    """
    flask.session['cambio']=True
    cantT=getAllTiposItem().count()
    flask.session['infopag']=calculoDeSiguiente(cantT)
    return flask.redirect('/admtipo/admimportartipo/')  

@app.route('/admtipo/importar/prevtipo/')
@pms.vista.required.login_required       
def prevPageImp():
    """Responde al boton 'anterior' de la paginacion de la lista de Tipos de Items para importar
    """
    flask.session['cambio']=True
    flask.session['infopag']=calculoDeAnterior(getAllTiposItem().count())
    return flask.redirect('/admtipo/admimportartipo/')


