from flask import Flask, render_template, url_for
import flask.views
from pms.modelo.proyectoControlador import getProyectoId
from flask_weasyprint import HTML, render_pdf
from pms.modelo.relacionControlador import hijos
from pms.modelo.itemControlador import getItemId,getVersionId
from pms.modelo.tipoItemControlador import getTipoItemId
from pms.modelo.peticionControlador import getLBPeticion
from datetime import datetime
from pms import app
@app.route('/hello/')
def informeProyecto():
    """
    Retorna el informe de un proyecto
    """
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
def informeProyectoPdf():
    """
    Retorna la version pdf del informe de proyecto
    """
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
@app.route('/informesolicitud/<a>')
def informeSolicitud(a=None):
    """
    Retorna la version pdf del informe de solicitudes si recibe a, sino la version web
    """
    pro=getProyectoId(flask.session['proyectoid'])
    solicitudes=[]
    for s in pro.solicitudes:
        lineas=[]
        lineas=getLBPeticion(s.id)
        aux=[]
        aux.insert(0, s)
        aux.insert(1, lineas)
        solicitudes.append(aux)
        dia=datetime.today()
    if a:
        html = render_template('informeSolicitudes.html', solicitudes=solicitudes, dia=dia)
        return render_pdf(HTML(string=html))
    else:
        return flask.render_template('informeSolicitudesWeb.html', solicitudes=solicitudes, dia=dia)
    

@app.route('/informeitem/<i>')
def informeItem(i):
    """
    Retorna la version pdf del informe del historial de un item
    """
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
    
    
    
    