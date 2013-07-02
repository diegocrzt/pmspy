from flask import Flask, render_template, url_for
import flask.views
from pms.modelo.proyectoControlador import getProyectoId
from flask_weasyprint import HTML, render_pdf
from pms.modelo.relacionControlador import hijos
from pms import app
@app.route('/hello/')
def hello():
    pro=getProyectoId(flask.session['proyectoid'])
    fas=[]
    for fase in pro.fases:
        li=[]
        li.insert(0, fase.numero)
        li.insert(1, fase.nombre)
        li.insert(2, fase.estado)
        li.insert(3, fase.fechaInicio)
        li.insert(4, fase.fechaFin)
        li.insert(5, fase.fechaUltMod)
        tipos=fase.tipos
        itm=[]
        for t in tipos:
            for ins in t.instancias:
                for ver in ins.version:
                    if ver.actual:
                        itm.append(ver)
        li.insert(6, itm)
        fas.append(li)
    
    return flask.render_template('hello.html',fases=fas)
@app.route('/proyectopdf/')
def hello_pdf():
    # Make a PDF straight from HTML in a string.
    pro=getProyectoId(flask.session['proyectoid'])
    fas=[]
    for fase in pro.fases:
        li=[]
        li.insert(0, fase.numero)
        li.insert(1, fase.nombre)
        li.insert(2, fase.estado)
        li.insert(3, fase.fechaInicio)
        li.insert(4, fase.fechaFin)
        li.insert(5, fase.fechaUltMod)
        tipos=fase.tipos
        itm=[]
        for t in tipos:
            for ins in t.instancias:
                for ver in ins.version:
                    if ver.actual:
                        itm.append(ver)
        li.insert(6, itm)
        fas.append(li)
    html = render_template('informeProyecto.html', fases=fas)
    return render_pdf(HTML(string=html))

@app.route('/informesolicitud/')
def informeSolicitud():
    pro=getProyectoId(flask.session['proyectoid'])
    solicitudes=[]
    for s in pro.solicitudes:
        lineas=[]
        for i in s.items:
            hi=hijos(i.item.id)
            for item in hi:
                if item.item.linea_id:
                    if not item.item.lineabase in lineas:
                        lineas.append(item.item.lineabase)
        aux=[]
        aux.insert(0, s)
        aux.insert(1, lineas)
        solicitudes.append(aux)
    html = render_template('informeSolicitudes.html', solicitudes=solicitudes)
    return render_pdf(HTML(string=html))
    
    