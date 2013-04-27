'''
Created on 05/04/2013

@author: Martin Poletti
@author: Natalia Valdez
'''
import flask.views
from flask import request
from werkzeug.serving import run_simple
from pms.modelo.usuarioControlador import validar, getUsuarios, eliminarUsuario, getUsuario, crearUsuario, getUsuarioById, editarUsuario, comprobarUsuario, usuarioIsLider
from pms.modelo.proyectoControlador import comprobarProyecto, crearProyecto, getProyectos, eliminarProyecto, getProyectoId, inicializarProyecto
from pms.modelo.faseControlador import getFases, comprobarFase, crearFase, eliminarFase, getFaseId, editarFase
from datetime import timedelta
from datetime import datetime
import pms.vista.required
from pms import app
app.secret_key = "bacon"

    



app.debug = True 
run_simple("localhost", 5000, app, use_reloader=True, use_debugger=True, use_evalex=True)