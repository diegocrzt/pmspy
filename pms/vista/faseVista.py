import flask.views
from flask import request
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase
from pms.modelo.proyectoControlador import getProyectoId
from datetime import timedelta
from datetime import datetime
import pms.vista.required
from pms import app

class Crearfase(flask.views.MethodView):
    """
    Gestiona la Vista de Crear Fase
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.render_template('crearFase.html')
    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        flask.session['aux2']=flask.request.form['numero']
        flask.session['aux3']=flask.request.form['fechainicio']
        flask.session['aux4']=flask.request.form['fechafin']
        fechainicio=flask.request.form['fechainicio']
        fechafin=flask.request.form['fechafin']
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect(flask.url_for('crearfase'))
        if(flask.request.form['numero']==""):
            flask.flash("El campo numero no puede estar vacio")
            return flask.redirect(flask.url_for('crearfase'))
        if(flask.request.form['fechainicio']==""):
            fechainicio=datetime.today()
        else:
            fechainicio = datetime.strptime(fechainicio, '%Y-%m-%d')
        if(flask.request.form['fechafin']==""):
            fechafin=datetime.today()+timedelta(days=15)
        else:
            fechafin = datetime.strptime(fechafin, '%Y-%m-%d')
        if fechafin <= fechainicio:
            flask.flash("incoherencia entre fechas de inicio y de fin")
            return flask.redirect(flask.url_for('crearfase'))
        if comprobarFase(flask.request.form['numero'],flask.session['proyectoid']):
            flask.flash("La fase ya existe")
            return flask.redirect(flask.url_for('crearfase'))
        crearFase(flask.request.form['nombre'][:20],flask.request.form['numero'], fechainicio, fechafin, None, None, flask.session['proyectoid'])
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        return flask.redirect('/admfase/'+str(flask.session['proyectoid'])) 
    
class Editarfase(flask.views.MethodView):
    """
    Vista de Editar Fase
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect(flask.url_for('admfase'))
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Editar Fase
        """
        fechainicio=flask.request.form['fechainicio']
        fechafin=flask.request.form['fechafin']
        if(flask.request.form['nombre']==""):
            flask.flash("El campo nombre no puede estar vacio")
            return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid']))
        if(flask.request.form['numero']==""):
            flask.flash("El campo numero no puede estar vacio")
            return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid']))     
        if(flask.request.form['fechainicio']==""):
            fechainicio=datetime.today()
        else:
            fechainicio = datetime.strptime(fechainicio, '%Y-%m-%d')
        if(flask.request.form['fechafin']==""):
            fechafin=datetime.today()+timedelta(days=15)
        else:
            fechafin = datetime.strptime(fechafin, '%Y-%m-%d')
        if fechafin <= fechainicio:
            flask.flash("incoherencia entre fechas de inicio y de fin")
            return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid'])) 
        if str(flask.session['numerofase']) != str(flask.request.form['numero']):
            if comprobarFase(flask.request.form['numero'], flask.session['proyectoid']):
                flask.flash("El numero de fase ya esta usado")
                return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid']))
        editarFase(flask.session['faseid'], flask.request.form['nombre'][:20],flask.request.form['numero'], fechainicio,fechafin)
        return flask.redirect('/admfase/'+str(flask.session['proyectoid']))        
    
class Eliminarfase(flask.views.MethodView):
    """
    Vista de Eliminar Fase
    """
    
    @pms.vista.required.login_required  
    def get(self):
        if(flask.session['faseid']!=None):
            return flask.render_template('eliminarFase.html')
        else:
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Eliminar Fase
        """
        if(flask.session['faseid']!=None):
            eliminarFase(flask.session['faseid'],flask.session['proyectoid'])
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
        else:
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
        
@app.route('/admfase/eliminarfase/<fase>')
@pms.vista.required.login_required
def eFase(fase=None): 
    """
    Funcion que llama a la Vista de Eliminar Fase, responde al boton de 'Eliminar' de Administrar Fase
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)
    fas=getFaseId(fase)
    flask.session['faseid']=fas.id
    p=getProyectoId(fas.proyecto)
    if(p.lider == flask.session['usuarioid']):
        return flask.render_template('eliminarFase.html',f=fas)           
    else:
        return flask.redirect(flask.url_for('admproyecto'))
    
@app.route('/admfase/editarfase/<f>', methods=["POST", "GET"])
@pms.vista.required.login_required
def edFase(f=None):
    """
    Funcion que llama a la Vista de Editar Fase, responde al boton de 'Editar' de Administrar Fase
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)
    if request.method == "GET":
        fas=getFaseId(f)
        flask.session['numerofase']=fas.numero
        flask.session['faseid']=fas.id
        flask.session['proyectoid']=fas.proyecto
        p=getProyectoId(fas.proyecto)
        if(p.lider == flask.session['usuarioid']):
            return flask.render_template('editarFase.html',f=fas)
        else:
            return flask.redirect(flask.url_for('admproyecto'))
    else:
        return flask.render_template('admFase.html')        
        
@app.route('/admfase/<p>')
@pms.vista.required.login_required
def admFase(p=None):
    """
    Funcion que llama a la Vista de Administrar Fase, responde al boton de 'Selec>>' de Administrar Proyecto
    """
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)  
    if request.method == "GET":
        if(getProyectoId(p).lider==flask.session['usuarioid']):
            flask.session.pop('faseid',None)
            flask.session['proyectoid']=p
            flask.session['proyectonombre']=getProyectoId(p).nombre
            f=getFases(p)
            if(getProyectoId(p).estado!="Iniciado"):
                flask.session['proyectoiniciado']=False
            else:
                flask.session['proyectoiniciado']=True
            tienefases=True
            if(getProyectoId(p).cantFase==0):
                tienefases=False
            return flask.render_template('admFase.html',fases=f, hay=tienefases)
        else:
            return flask.redirect(flask.url_for('admproyecto'))
    else:
        return flask.redirect(flask.url_for('admproyecto'))
