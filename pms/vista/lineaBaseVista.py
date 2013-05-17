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
from pms.modelo.faseControlador import getFaseId
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
        return flask.redirect('/admlinea/'+str(flask.session['faseid']))
    
    @pms.vista.required.login_required
    def post(self):
        if(flask.session['lineaid']):
            eliminarLB(flask.session['lineaid'])
            return flask.redirect('/admlinea/')
    
    
@app.route('/admlinea/crear/')    
@pms.vista.required.login_required
def CrearLineaBase():
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
            return flask.redirect('/admlinea/crearlinea/')
        elif "Cancelar" in flask.request.form:
            flask.flash(u"No se pudo agregar","text-error")
            return flask.redirect('/admlinea/crearlinea/')

@app.route('/admlinea/quitar/<i>')
@pms.vista.required.login_required         
def quitarItem(i=None):
    desBloquearAdelante(int(i))
    flask.flash(u"Quitado","text-success")
    return flask.redirect('/admlinea/crearlinea/')

@app.route('/admlinea/<f>')
@pms.vista.required.login_required   
def admfase(f=None):
    flask.session['faseid']=f
    flask.session['fasenombre']=getFaseId(f).nombre
    return flask.redirect('/admlinea/')

@app.route('/admlinea/eliminar/<l>')
@pms.vista.required.login_required   
def eliminarLineaBase(l=None):
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
    if request.method == "POST":
        if flask.request.form['comentario']!="":
            flask.session['aux1']=flask.request.form['comentario']
            agregarComentarioLB(flask.session['lineaid'], flask.request.form['comentario'][:100])
        if "Aceptar" in flask.request.form:
            flask.flash(u"CREACION EXITOSA","text-success")
            return flask.redirect('/admlinea/')
        else:
            return flask.redirect('/admlinea/crearlinea/')

@app.route('/admlinea/cancelarcreacion/')
@pms.vista.required.login_required   
def cancelarCreacion():
    eliminarLB(flask.session['lineaid'])
    flask.flash(u"CREACION CANCELADA","text-error")
    return flask.redirect('/admlinea/')

@app.route('/admlinea/concultar/<l>')
@pms.vista.required.login_required 
def consultarLineaBase(l=None):
    linea=getLineaBaseId(l)
    if(linea):
        versiones=[]
        for i in linea.items:
            v=getVersionItem(i.id)
            versiones.append(v)
        return flask.render_template('consultarLineaBase.html', linea=linea, versiones=versiones)
    else:
        return flask.redirect('/admlinea/')
    
"""    @app.route('/admlinea/crearlinea/<i>', methods=['POST'])
    @pms.vista.required.login_required     
    def crearLB(i=None):
    if request.method == "POST":
        if 'agregar' in flask.request.form:
            return agregarItem()"""
    
