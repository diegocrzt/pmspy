import flask.views
from flask import request
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase, getFasesPaginadas, controlCerrarFase, cerrarFase,actualizarFecha
from pms.modelo.proyectoControlador import getProyectoId
from pms.modelo.rolControlador import getProyectosDeUsuario
from pms.modelo.peticionControlador import getMiembros, agregarListaMiembros
from pms.modelo.usuarioControlador import getUsuarios, getUsuarioById
from datetime import timedelta
from datetime import datetime
import pms.vista.required
from pms import app
TAM_PAGINA=5

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
        error=False
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            error=True
        if(flask.request.form['numero']==""):
            flask.flash(u"El campo numero no puede estar vacio","numero")
            error=True
        elif comprobarFase(flask.request.form['numero'],flask.session['proyectoid']):
            flask.flash(u"La fase ya existe","numero")
            error=True
        if error:
            return flask.redirect(flask.url_for('crearfase'))
        if(flask.request.form['fechainicio']==""):
            fechainicio=datetime.today()
        else:
            fechainicio = datetime.strptime(fechainicio, '%Y-%m-%d')
        if(flask.request.form['fechafin']==""):
            fechafin=fechainicio+timedelta(days=15)
        else:
            fechafin = datetime.strptime(fechafin, '%Y-%m-%d')
        if fechafin <= fechainicio:
            flask.flash(u"Incoherencia entre fechas de inicio y de fin","fecha")
            return flask.redirect(flask.url_for('crearfase'))
        
        crearFase(flask.request.form['nombre'][:20],flask.request.form['numero'], fechainicio, fechafin, None, None, flask.session['proyectoid'])
        flask.session.pop('aux1',None)
        flask.session.pop('aux2',None)
        flask.session.pop('aux3',None)
        flask.session.pop('aux4',None)
        flask.flash(u"CREACION EXITOSA","text-success")
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
        error=False
        fechainicio=flask.request.form['fechainicio']
        fechafin=flask.request.form['fechafin']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            error=True
        if(flask.request.form['numero']==""):
            flask.flash(u"El campo numero no puede estar vacio","numero")  
            error=True  
        elif str(flask.session['numerofase']) != str(flask.request.form['numero']):
            if comprobarFase(flask.request.form['numero'], flask.session['proyectoid']):
                flask.flash("El numero de fase ya esta usado")
                error=True
        if error:
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
            flask.flash(u"Incoherencia entre fechas de inicio y de fin","fecha")
            return flask.redirect('/admfase/editarfase/'+str(flask.session['faseid']))         
        editarFase(flask.session['faseid'], flask.request.form['nombre'][:20],flask.request.form['numero'], fechainicio,fechafin)
        flask.flash(u"EDICION EXITOSA","text-success")
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
            eliminarFase(flask.session['faseid'])
            flask.flash(u"ELIMINACION EXITOSA","text-success")
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
    p=getProyectoId(fas.proyecto.id)
    if(p.delider == flask.session['usuarioid']):
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
        flask.session['proyectoid']=fas.proyecto.id
        p=getProyectoId(fas.proyecto.id)
        if(p.delider == flask.session['usuarioid']):
            return flask.render_template('editarFase.html',f=fas)
        else:
            return flask.redirect(flask.url_for('admproyecto'))
    else:
        return flask.render_template('admFase.html')        
        
@app.route('/admfase/<p>')
@pms.vista.required.login_required
def admFase(p=None):
    """
    Funcion que llama a la Vista de Administrar Fase, responde al boton de 'Selec>>' de Administrar Proyecto, 
    recibe p que contiene el id del proyecto al que se ingreso
    """
    global TAM_PAGINA
    flask.session.pop('aux1',None)
    flask.session.pop('aux2',None)
    flask.session.pop('aux3',None)
    flask.session.pop('aux4',None)  
    if request.method == "GET":
        lp=getProyectosDeUsuario(flask.session['usuarioid'])
        p2=int(p)
        if getProyectoId(p).delider==int(flask.session['usuarioid']):
            flask.session['islider']=True
        else:
            flask.session['islider']=False
        
        if(getProyectoId(p).lider.id==flask.session['usuarioid'] or (p2 in lp)):
            flask.session.pop('faseid',None)
            flask.session['proyectoid']=p
            flask.session['proyectonombre']=getProyectoId(p).nombre
            if flask.session['cambio']:
                flask.session['cambio']=False
            else:
                flask.session['haynext']=True
                flask.session['hayprev']=False
                flask.session['pagina']=1
            f=getFasesPaginadas(flask.session['pagina']-1,TAM_PAGINA,p)
            if(f.count()!=0):
                t=getFases(p).count()/TAM_PAGINA
                mod=getFases(p).count()%TAM_PAGINA
                if mod>0:
                    t=int(t)+1#Total de paginas
                else:
                    t=int(t+mod)
                m=flask.session['pagina']#Pagina en la que estoy
                infopag="Pagina "+ str(m) +" de " + str(t)
                if m<t:
                    flask.session['haynext']=True
                else:
                    flask.session['haynext']=False
                if m==1:
                    flask.session['hayprev']=False
                else:
                    flask.session['hayprev']=True
            else:
                flask.session['haynext']=False
                flask.session['hayprev']=False
                infopag="Pagina 1 de 1"
            if(getProyectoId(p).estado!="Iniciado"):
                flask.session['proyectoiniciado']=False
            else:
                flask.session['proyectoiniciado']=True
            tienefases=True
            if(getProyectoId(p).cantFase==0):
                tienefases=False
            return flask.render_template('admFase.html',fases=f, hay=tienefases,infopag=infopag,p=getProyectoId(p))
        else:
            return flask.redirect(flask.url_for('admproyecto'))
    else:
        return flask.redirect(flask.url_for('admproyecto'))
    
    
@app.route('/admfase/nextfase/')
@pms.vista.required.login_required       
def nextPageF():
    flask.session['cambio']=True
    cantF=getFases(flask.session['proyectoid']).count()
    flask.session['pagina']=flask.session['pagina']+1
    global TAM_PAGINA
    sobran=cantF-flask.session['pagina']* TAM_PAGINA
    print "Pagina:"
    print flask.session['pagina']
    print sobran
    if sobran>0:
        flask.session['haynext']=True
    else:
        flask.session['haynext']=False
    if flask.session['pagina']==1:
        flask.session['hayprev']=False
    else:
        flask.session['hayprev']=True
    return flask.redirect('/admfase/'+str(flask.session['proyectoid']))   

@app.route('/admfase/prevfase/')
@pms.vista.required.login_required       
def prevPageF():
    flask.session['cambio']=True
    flask.session['pagina']=flask.session['pagina']-1
    global TAM_PAGINA
    pag=flask.session['pagina']
    if pag==1:
        flask.session['hayprev']=False
    else:
        flask.session['hayprev']=True
    if getFases(flask.session['proyectoid']).count()>(pag*TAM_PAGINA):
            flask.session['haynext']=True
    return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
    
@app.route('/admfase/cerrarfase/<f>', methods=["POST", "GET"])
@pms.vista.required.login_required
def cerrFase(f=None):
    """
    Funcion que llama a la Vista de Cerrar Fase
    """
    if request.method == "GET":
        f=int(f)
        flask.session['faseid']=f
        fas=getFaseId(f)
        tipos=fas.tipos
        itm=[]
        for t in tipos:
            for ins in t.instancias:
                for ver in ins.version:
                    if ver.actual:
                        itm.append(ver)
        if not controlCerrarFase(fas.id):
            flask.flash(u"LA FASE NO SE PUEDE CERRAR", "text-error")
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
        return flask.render_template('cerrarFase.html',items=itm)   
    else:
        return flask.redirect(flask.url_for('admproyecto'))
    
@app.route('/admfase/cerrarfaseb/<f>', methods=["POST", "GET"])
@pms.vista.required.login_required
def cerrarFaseB(f=None):
    """ 
    Funcion que cierra la fase
    """
    f=int(f)
    if controlCerrarFase(f):
        cerrarFase(f)
        flask.flash(u"FASE CERRADA EXITOSAMENTE","text-success")
        actualizarFecha(f)
        return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
    else:
        return flask.redirect('/admfase/'+str(flask.session['proyectoid']))
    
    
class ListaMiembros(flask.views.MethodView):
    """
    
    """
    @pms.vista.required.login_required  
    def get(self):
        miembros=getMiembros(flask.session['proyectoid'])
        usuarios=getUsuarios()
        lider=getUsuarioById(flask.session['usuarioid'])
        lista=[]
        for u in usuarios:
            if u.nombredeusuario!=lider.nombredeusuario:
                bandera=False
                for m in miembros:
                    if m.user_id==u.id:
                        bandera=True
                aux=[]
                aux.append(u.nombredeusuario)
                if bandera==True:
                    aux.append(True)
                else:
                    aux.append(False)
                lista.append(aux)
            
        for l in lista:
            print l[0]
            print l[1]    
        return flask.render_template('listaComite.html',batata=lista,lider=lider)   
    @pms.vista.required.login_required
    def post(self):
        """
        
        """
        usuarios=getUsuarios()
        ag=[]
        lider=getUsuarioById(flask.session['usuarioid'])
        ag.append(lider)
        for u in usuarios:
            if u.nombredeusuario in flask.request.form:
                if flask.request.form[u.nonombredeusuariombre]:
                    ag.append(u)
        if len(ag)%2!=0:
            agregarListaMiembros(ag,flask.session['proyectoid'])
            flask.flash(u"COMITE EDITADO", "text-success")
            return flask.redirect('/admfase/'+str(flask.session['proyectoid']))            
        else:
            flask.flash(u"El numero de miembros seleccionados es impar.", "cantidad")
            return flask.redirect("/admfase/comite/")
        

