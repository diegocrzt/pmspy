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
from pms.modelo.lineaBaseControlador import crearLB, agregarItemLB, quitarItemLB, eliminarLB, getLineaBaseId

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
            return flask.render_template('admLineaBase.html',lineas=lineas)

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


@app.route('/admlinea/agregar/<i>')
@pms.vista.required.login_required         
def agregarItem(i=None):
    idl=flask.session['lineaid']
    version=getVersionId(i)
    
    agregarItemLB(int(i),idl)
    return flask.redirect('/admlinea/crearlinea/')

@app.route('/admlinea/quitar/<i>')
@pms.vista.required.login_required         
def quitarItem(i=None):
    quitarItemLB(int(i),flask.session['lineaid'])
    return flask.redirect('/admlinea/crearlinea/')

@app.route('/admlinea/<f>')
@pms.vista.required.login_required   
def admfase(f=None):
    flask.session['faseid']=f
    return flask.redirect('/admlinea/')

@app.route('/admlinea/eliminar/<l>')
@pms.vista.required.login_required   
def eliminarLineaBase(l=None):
    linea=getLineaBaseId(l)
    flask.session['lineaid']=l
    versiones=[]
    for i in linea.items:
        v=getVersionItem(i.id)
        versiones.append(v)
    
    return flask.render_template('eliminarLineaBase.html', linea=linea, versiones=versiones)

@app.route('/admlinea/confirmarcreacion/')
@pms.vista.required.login_required   
def confirmarCreacion():
    flask.flash(u"CREACION EXITOSA","text-success")
    return flask.redirect('/admlinea/')

@app.route('/admlinea/cancelarcreacion/')
@pms.vista.required.login_required   
def cancelarCreacion():
    eliminarLB(flask.session['lineaid'])
    flask.flash(u"CREACION CANCELADA","text-error")
    return flask.redirect('/admlinea/')
    