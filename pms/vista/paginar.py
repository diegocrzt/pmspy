import flask.views
from flask import request


TAM_PAGINA=5

def calculoPrimeraPag(cant):
    if(cant!=0):#Si devolvio algo
        t=cant/TAM_PAGINA
        mod=cant%TAM_PAGINA
        if mod>0:
            t=int(t)+1#Total de paginas
        elif int(t)==0:
            t=1
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
    else:#si no pantalla vacia sin botones siguiente ni anterior
        flask.session['haynext']=False
        flask.session['hayprev']=False
        infopag="Pagina 1 de 1"
    return infopag

def calculoDeSiguiente(cant):
    t=cant/TAM_PAGINA
    mod=cant%TAM_PAGINA
    if mod>0:
        t=int(t)+1#Total de paginas
    elif int(t)==0:
        t=1
    flask.session['pagina']=flask.session['pagina']+1
    sobran=cant-flask.session['pagina']* TAM_PAGINA
    if sobran>0:
        flask.session['haynext']=True
    else:
        flask.session['haynext']=False
    if flask.session['pagina']==1:
        flask.session['hayprev']=False
    else:
        flask.session['hayprev']=True
    m=flask.session['pagina']
    infopag="Pagina "+ str(m) +" de " + str(t)
    return infopag

def calculoDeAnterior(cant):
    t=cant/TAM_PAGINA #Saber cuantas paginas se necesitan
    mod=cant%TAM_PAGINA #modulo
    if mod>0: #si el mod no es cero, la division no es perfecta
        t=int(t)+1#la cantidad de paginas necesarias es la parte entera de la division mas 1
    elif int(t)==0:
        t=1
    flask.session['pagina']=flask.session['pagina']-1
    pag=flask.session['pagina']
    if pag==1:
        flask.session['hayprev']=False
    else:
        flask.session['hayprev']=True
    if cant>(pag*TAM_PAGINA):
        flask.session['haynext']=True
    
    m=flask.session['pagina']#Pagina en la que estoy
    infopag="Pagina "+ str(m) +" de " + str(t)
    return infopag


def totalPaginas(cant):
    t=cant/TAM_PAGINA
    mod=cant%TAM_PAGINA
    if mod>0:
        t=int(t)+1#Total de paginas
    else:
        t=1
    return t
    