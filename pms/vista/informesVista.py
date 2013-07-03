from flask import Flask, render_template, url_for
import flask.views
from pms.modelo.proyectoControlador import getProyectoId
from flask_weasyprint import HTML, render_pdf
from pms.modelo.relacionControlador import hijos
from pms.modelo.itemControlador import getItemId,getVersionId,getVersionItem
from pms.modelo.tipoItemControlador import getTipoItemId
from datetime import datetime
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
    dia=datetime.today()
    html = render_template('informeProyecto.html', fases=fas, dia=dia)
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
        dia=datetime.today()
    html = render_template('informeSolicitudes.html', solicitudes=solicitudes, dia=dia)
    return render_pdf(HTML(string=html))

@app.route('/informeitem/<i>')
def informeItem(i):
    ver=getVersionId(i)
    item=getItemId(ver.deitem)
    tipo=getTipoItemId(item.tipo)
    atr=tipo.atributos
    versiones=[]
    for v in item.version:
        
        val=[]
        for at in v.atributosnum:
            val.append(at)
        for at in v.atributosstr:
            val.append(at)
        for at in v.atributosbool:
            val.append(at)
        for at in ver.atributosdate:
            val.append(at)
        padres=[]
        antecesores=[]
        for n in v.ante_list:
            if n.tipo=="P-H":
                aux=getVersionId(n.ante_id)
                if aux.actual==True:
                    padres.append(aux)
            else:
                aux=getVersionId(n.ante_id)
                if aux.actual==True:
                    antecesores.append(aux)
        hijos=[]
        posteriores=[]
        for n in v.post_list:
            if n.tipo=="P-H":
                aux=getVersionId(n.post_id)
                if aux.actual==True:
                    hijos.append(aux)
            else:
                aux=getVersionId(n.post_id)
                if aux.actual==True:
                    posteriores.append(aux)
        conten=[]
        conten.insert(0, v)
        conten.insert(1, val)
        conten.insert(2, padres)
        conten.insert(3, antecesores)
        conten.insert(4, hijos)
        conten.insert(5, posteriores)
        versiones.append(conten)
        
    dia=datetime.today()
    html = render_template('informeItem.html', versiones=versiones, dia=dia, atributos=atr, item=item)
    return render_pdf(HTML(string=html))
    
    
    
    