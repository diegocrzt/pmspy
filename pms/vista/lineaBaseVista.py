'''
Created on 18/04/2013

@author: Natalia Valdez
'''
import flask.views
from flask import request
from pms.modelo.entidad import Atributo,TipoItem, Rol, Relacion
import pms.vista.required
from pms import app
from pms.modelo.itemControlador import copiarValores, getItemsTipo,getItemId,getItemEtiqueta,getVersionId,getVersionItem
from pms.modelo.rolControlador import getRolesDeUsuarioEnFase
from pms.modelo.faseControlador import getFaseId,actualizarFecha
from pms.modelo.lineaBaseControlador import desBloquearAdelante, comprobarBloquear, crearLB, aItemLB, quitarItemLB, eliminarLB, getLineaBaseId, agregarComentarioLB

class AdmLineaBase(flask.views.MethodView):
    
    @pms.vista.required.login_required
    def get(self):
        """Devuelve la lista paginada de todos los Tipos de Items de la fase 
        """
        if flask.session['faseid']!=None:
            flask.session['numerolb']=None
            fase=getFaseId(flask.session['faseid'])
            lineas=fase.lineas
            for l in lineas:
                if(len(l.items)==0):
                    eliminarLB(l.id)
            lineas=fase.lineas
            roles=getRolesDeUsuarioEnFase(flask.session['usuarioid'], flask.session['faseid'])
            return flask.render_template('admLineaBase.html',lineas=lineas, roles=roles)

class EliminarLineaBase(flask.views.MethodView):
    
    @pms.vista.required.login_required
    def get(self):
        """Esta funcion solo evita errores de url no encontrado para el caso en que se introduzca el url /admlinea/eliminarlinea/
        el cual no devuelve ningun resultado, para ello se redirecciona a la vista de Administrar Linea Base"""
        return flask.redirect('/admlinea/'+str(flask.session['faseid']))
    
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de eliminar linea base
        """
        if(flask.session['lineaid']):
            eliminarLB(flask.session['lineaid'])
            return flask.redirect('/admlinea/')
    
    
@app.route('/admlinea/crear/')    
@pms.vista.required.login_required
def CrearLineaBase():
    """Se encarga de crear el numero de linea base correcta, verifica si existen lineas bases creadas sin items y las elimina,
        llama a listaItemsLinea
    """
    if flask.session['numerolb']:
        fase=getFaseId(flask.session['faseid'])
        lineas=fase.lineas
        e=len(lineas)
        n=0
        for l in lineas:
            n=n+1
            if(n==e):
                eliminarLB(l.id)
    flask.session['lineaid']=crearLB(flask.session['usuarioid'], None, flask.session['faseid'])
    l=getLineaBaseId(flask.session['lineaid'])
    flask.session['numerolb']=l.numero
    return listaItemsLinea()
        
@app.route('/admlinea/crearlinea/')    
@pms.vista.required.login_required
def listaItemsLinea():
    """Despliega la vista de crear items pasando al hmtl la lista de items que pueden ser agregados a una linea base, osea aprobados.
    """
    fase=getFaseId(flask.session['faseid'])
    vitems=[]
    for t in fase.tipos:
        for i in t.instancias:
            vitem=getVersionItem(i.id)
            if(vitem.estado.lower()=="aprobado" or vitem.item.linea_id==int(flask.session['lineaid'])):
                vitems.append(vitem)
    return flask.render_template('crearLineaBase.html', vitems=vitems)


@app.route('/admlinea/agregar/<i>', methods=['POST', 'GET'])
@pms.vista.required.login_required         
def agregarItem(i=None):
    """Despliega la vista de agregar item a linea base(agregarItemLB.html) y ejecuta la funcion de agregar item a linea base
    """
    if request.method == "GET":
        version=getVersionId(i)
        flask.session['itemid']=i
        if(comprobarBloquear(version)):
            padres=[]
            return flask.render_template('agregarItemLB.html', version=version, padres=None)
        else:
            padres=[]
            for n in version.ante_list:
                if n.tipo=="P-H":
                    aux=getVersionId(n.ante_id)
                    if aux.actual==True:
                        padres.append(aux)
            return flask.render_template('agregarItemLB.html', version=version, padres=padres)
            
    if request.method == "POST":
        if "Aceptar" in flask.request.form:
            r=aItemLB(int(flask.session['itemid']),flask.session['lineaid'])
            if r:
                flask.flash(u"AGREGACION EXITOSA","text-success")
            flask.session.pop('itemid',None)
            return flask.redirect('/admlinea/crearlinea/')
        elif "Cancelar" in flask.request.form:
            flask.flash(u"NO SE PUDO AGREGAR","text-error")
            flask.session.pop('itemid',None)
            return flask.redirect('/admlinea/crearlinea/')
        elif "CancelarA" in flask.request.form:
            flask.flash(u"AGREGACION CANCELADA","text-error")
            return flask.redirect('/admlinea/crearlinea/')

@app.route('/admlinea/quitar/<i>', methods=['POST', 'GET'])
@pms.vista.required.login_required         
def quitarItem(i=None):
    """Despliega la vista de desagregar item(quitarItemLB.html) y ejecuta la funcion de quitar el item de la linea base
    """
    if request.method == "GET":
        flask.session['itemid']=i
        ver=getVersionId(i)
        hijos=[]
        for n in ver.post_list:
            if n.tipo=="P-H":
                aux=getVersionId(n.post_id)
                if aux.actual==True:
                    hijos.append(aux)
        if len(hijos)>0:
            return flask.render_template('quitarItemLB.html', version=ver, hijos=hijos)
        else:
            return flask.render_template('quitarItemLB.html', version=ver, hijos=None)
        
    if request.method == "POST":
        if "Aceptar" in flask.request.form:
            desBloquearAdelante(int(i))
            flask.flash(u"DESAGREGACION EXITOSA","text-success")
            flask.session.pop('itemid',None)
            return flask.redirect('/admlinea/crearlinea/')
        elif "Cancelar" in flask.request.form:
            flask.flash(u"DESAGREGACION CANCELADA","text-error")
            flask.session.pop('itemid',None)
            return flask.redirect('/admlinea/crearlinea/')
            
@app.route('/admlinea/<f>')
@pms.vista.required.login_required   
def admfase(f=None):
    """Recibe el id de la fase y lo setea a una variable de session para luego llamar a la funcion get de la clase AdmLineaBase
    """
    flask.session['faseid']=f
    flask.session['fasenombre']=getFaseId(f).nombre
    return flask.redirect('/admlinea/')

@app.route('/admlinea/eliminar/<l>')
@pms.vista.required.login_required   
def eliminarLineaBase(l=None):
    """Despliega el la vista de eliminar linea base(eliminarLineaBase.html), responde al boton eliminar de Administrar Linea Base
    """
    linea=getLineaBaseId(l)
    if(linea):
        flask.session['lineaid']=l
        versiones=[]
        for i in linea.items:
            v=getVersionItem(i.id)
            versiones.append(v)
        return flask.render_template('eliminarLineaBase.html', linea=linea, versiones=versiones)
    else:
        return flask.redirect('/admlinea/')

@app.route('/admlinea/confirmarcreacion/', methods=['POST'])
@pms.vista.required.login_required   
def confirmarCreacion():
    """Responde al boton aceptar de Crear Linea Base, confirma la creacion de la linea base, verifica que la linea base contenga al menos un item
    setea el comentario a la linea base
    """
    if request.method == "POST":
        if flask.request.form['comentario']!="":
            flask.session['aux1']=flask.request.form['comentario']
            agregarComentarioLB(flask.session['lineaid'], flask.request.form['comentario'][:100])
        if "Aceptar" in flask.request.form:
            linea=getLineaBaseId(flask.session['lineaid'])
            if linea.items:
                flask.flash(u"CREACION EXITOSA","text-success")
                actualizarFecha(flask.session['faseid'])
                return flask.redirect('/admlinea/')
            else:
                flask.flash(u"La linea base debe contener al menos un item","text-error")
                return flask.redirect('/admlinea/crearlinea/')
        else:
            return flask.redirect('/admlinea/crearlinea/')

@app.route('/admlinea/cancelarcreacion/')
@pms.vista.required.login_required   
def cancelarCreacion():
    """Cancela la creacion de la linea base eliminandola, responde al boton cancelar de Crear Linea Base
    """
    eliminarLB(flask.session['lineaid'])
    flask.flash(u"CREACION CANCELADA","text-error")
    return flask.redirect('/admlinea/')

@app.route('/admlinea/concultar/<l>')
@pms.vista.required.login_required 
def consultarLineaBase(l=None):
    """Despliega la vista de consultar linea base (consultarLineaBase.html), recibe el id de la linea base
    """
    linea=getLineaBaseId(l)
    if(linea):
        versiones=[]
        for i in linea.items:
            v=getVersionItem(i.id)
            versiones.append(v)
        return flask.render_template('consultarLineaBase.html', linea=linea, versiones=versiones)
    else:
        return flask.redirect('/admlinea/')
    

    
