import flask.views
from flask import request
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase, getFasesPaginadas
from pms.modelo.usuarioControlador import getUsuario,getUsuarioById,getUsuarios
from pms.modelo.rolControlador import comprobarRol,comprobarUser_Rol,crearRol,crearUser_Rol,editarRol,eliminarRol,eliminarUser_Rol,getRelRol,getRolesFase,getRolId,getRolNombre,getRolUser
import pms.vista.required
from pms import app


@app.route('/admrol/<f>')
@pms.vista.required.login_required
def admRol(f=None):
    """
    Funcion que llama a la Vista de Administrar Rol, responde al boton de 'Selec>>' de Administrar Fase
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
        rl=fase.roles
        
        return flask.render_template('admRol.html',roles=rl)
    else:
        return flask.redirect(flask.url_for('admfase'))
    
    
    
class CrearRol(flask.views.MethodView):
    """
    Gestiona la Vista de Crear rol
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.render_template('crearRol.html')
    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.render_template('crearRol.html')
        if comprobarRol(flask.request.form['nombre'],flask.session['faseid']):
            flask.flash(u"El rol ya existe","nombre")
            return flask.render_template('crearRol.html')
        codt=0
        a = 'crearT'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['crearT']
        if (a):
            codt=codt+1
        a = 'editarT'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['editarT']
        if (a):
            codt=codt+10
        a = 'eliminarT'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['eliminarT']
        if (a):
            codt=codt+100
        codi=0
        a = 'crearI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['crearI']
        if (a):
            codi=codi+1
        a = 'editarI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['editarI']
        if (a):
            codi=codi+10
        a = 'eliminarI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['eliminarI']
        if (a):
            codi=codi+100    
        a = 'aprobarI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['aprobarI']
        if (a):
            codi=codi+1000
        a = 'revivirI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['revivirI']
        if (a):
            codi=codi+10000
        a = 'reversionarI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['reversionarI']
        if (a):
            codi=codi+100000
        a = 'asignarpadreI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['asignarpadreI']
        if (a):
            codi=codi+1000000
        a = 'asignarantecesorI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['asignarantecesorI']
        if (a):
            codi=codi+10000000
        codlb=0
        a = 'crearLB'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['crearLB']
        if(a):
            codlb=codlb+1
        a = 'eliminarLB'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['eliminarLB']
        if(a):
            codlb=codlb+10
        crearRol(flask.session['faseid'],flask.request.form['nombre'][:20],codi,codt,codlb)
        flask.session.pop('aux1',None)
        flask.flash(u"CREACION EXITOSA","text-success")
        return flask.redirect('/admrol/'+str(flask.session['faseid'])) 
    
class EditarRol(flask.views.MethodView):
    """
    Gestiona la Vista de Crear rol
    """
    @pms.vista.required.login_required
    def get(self):
        return flask.redirect('/admrol/'+str(flask.session['faseid']))
    @pms.vista.required.login_required
    def post(self):
        flask.session['aux1']=flask.request.form['nombre']
        if(flask.request.form['nombre']==""):
            flask.flash(u"El campo nombre no puede estar vacio","nombre")
            return flask.redirect('/admrol/editarrol/'+str(flask.session['rolid'])) 
        codt=0
        a = 'crearT'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['crearT']
        if (a):
            codt=codt+1
        a = 'editarT'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['editarT']
        if (a):
            codt=codt+10
        a = 'eliminarT'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['eliminarT']
        if (a):
            codt=codt+100
        codi=0
        a = 'crearI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['crearI']
        if (a):
            codi=codi+1
        a = 'editarI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['editarI']
        if (a):
            codi=codi+10
        a = 'eliminarI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['eliminarI']
        if (a):
            codi=codi+100    
        a = 'aprobarI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['aprobarI']
        if (a):
            codi=codi+1000
        a = 'revivirI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['revivirI']
        if (a):
            codi=codi+10000
        a = 'reversionarI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['reversionarI']
        if (a):
            codi=codi+100000
        a = 'asignarpadreI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['asignarpadreI']
        if (a):
            codi=codi+1000000
        a = 'asignarantecesorI'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['asignarantecesorI']
        if (a):
            codi=codi+10000000
        codlb=0
        a = 'crearLB'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['crearLB']
        if(a):
            codlb=codlb+1
        a = 'eliminarLB'
        if a not in flask.request.form:
            a=False
        else:
            a=flask.request.form['eliminarLB']
        if(a):
            codlb=codlb+10
        editarRol(flask.session['rolid'],flask.request.form['nombre'][:20],codi,codt,codlb)
        flask.session.pop('aux1',None)
        flask.flash(u"EDICION EXITOSA","text-success")
        return flask.redirect('/admrol/'+str(flask.session['faseid'])) 
        
class Eliminarrol(flask.views.MethodView):
    """
    Vista de Eliminar Rol
    """
    
    @pms.vista.required.login_required  
    def get(self):
     
        return flask.redirect('/admrol/'+str(flask.session['faseid']))
    @pms.vista.required.login_required
    def post(self):
        """
        Ejecuta la funcion de Eliminar Rol
        """
        if(flask.session['rolid']!=None):
            eliminarRol(flask.session['rolid'])
            flask.flash(u"ELIMINACION EXITOSA","text-success")
            return flask.redirect('/admrol/'+str(flask.session['faseid']))
        else:
            return flask.redirect('/admrol/'+str(flask.session['faseid']))    
    
@app.route('/admrol/eliminarrol/<r>')
@pms.vista.required.login_required
def eRol(r=None): 
    """
    Funcion que llama a la Vista de Eliminar Rol, responde al boton de 'Eliminar' de Administrar Rol
    """
   
    rol=getRolId(r)
    flask.session['rolid']=rol.id
    #No controlo que sea Lider
    rl=[]
    rl.append(rol)
    return flask.render_template('eliminarRol.html',rol=rol,r=rl)   

@app.route('/admrol/editarrol/<r>')
@pms.vista.required.login_required
def edRol(r=None): 
    """
    Funcion que llama a la Vista de Eliminar Rol, responde al boton de 'Eliminar' de Administrar Rol
    """
   
    rol=getRolId(r)
    flask.session['rolid']=rol.id
    nombre=rol.nombre
    r=[]
    r.append(rol)
    #No controlo que sea Lider
    return flask.render_template('editarRol.html',r=r,nombre=nombre)              


@app.route('/admrol/asignarrol/<u>')
@pms.vista.required.login_required
def auRol(u=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    crearUser_Rol(flask.session['rolid'],u)
    rol=getRolId(flask.session['rolid'])
    usuarios=[]
    usr=getUsuarios()
    for u in usr:
        if comprobarUser_Rol(rol.id,u.id):
            usuarios.append(u)
    return flask.render_template('asignarRol.html',usuarios=usuarios)      
    
@app.route('/admrol/asignar/<r>')
@pms.vista.required.login_required
def aRol(r=None): 
    """
    Funcion que llama a la Vista de Asignar Rol, responde al boton de 'Asignar' de Administrar Rol
    """
    rol=getRolId(r)
    flask.session['rolid']=rol.id
    usuarios=[]
    usr=getUsuarios()
    for u in usr:
        if comprobarUser_Rol(rol.id,u.id):
            usuarios.append(u)
    return flask.render_template('asignarRol.html',usuarios=usuarios)   


@app.route('/admrol/consultarrol/<r>')
@pms.vista.required.login_required
def consultarRol(r=None): 
    """
    Funcion que llama a la Vista de Consultar Rol, responde al boton de 'Consultar' de Administrar Rol
    """
   
    rol=getRolId(r)
    flask.session['rolid']=rol.id
    #No controlo que sea Lider
    rl=[]
    rl.append(rol)
    return flask.render_template('consultarRol.html',rol=rol,r=rl) 

@app.route('/admrol/desasignar/<r>')
@pms.vista.required.login_required
def iradesaRol(r=None):
    """
    Funcion que llama a la Vista de Desasignar Rol, responde al boton de 'Desasignar' de Administrar Rol
    """
    rol=getRolId(r)
    flask.session['rolid']=rol.id
    usuarios=[]
    usr=getUsuarios()
    for u in usr:
        if not comprobarUser_Rol(rol.id,u.id):
            usuarios.append(u)
    return flask.render_template('desasignarRol.html',usuarios=usuarios)   

@app.route('/admrol/desasignarrol/<u>')
@pms.vista.required.login_required
def desauRol(u=None): 
    """
    Funcion que llama a la Vista de Desasignar Rol, responde al boton de 'Desasignar' de Desasignar Rol
    """
    eliminarUser_Rol(flask.session['rolid'],u)
    rol=getRolId(flask.session['rolid'])
    usuarios=[]
    usr=getUsuarios()
    for u in usr:
        if not comprobarUser_Rol(rol.id,u.id):
            usuarios.append(u)
    return flask.render_template('desasignarRol.html',usuarios=usuarios) 
