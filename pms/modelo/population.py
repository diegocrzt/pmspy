'''
Created on 05/04/2013

@author: mpoletti
'''
from sqlalchemy import Table
from pms.modelo.entidad import Usuario, Proyecto, Fase, TipoItem, Atributo, Item, ValorNum, ValorStr, ValorBoolean, ValorDate, VersionItem, Rol, User_Rol, Relacion, Miembro
from pms.modelo.initdb import metadata, db_session, init_db, engine
import hashlib
from sqlalchemy.dialects.sqlite.base import DATETIME
from xmlrpclib import datetime
"""Puebla la base de datos con datos de pureba"""
'''Se deben borrar todas las tablas antes'''
init_db()

usuario = Table('usuario', metadata)
proyecto = Table('proyecto', metadata)
fase = Table('fase', metadata)
tipoItem = Table('tipoitem', metadata)
atributo = Table('atributo', metadata)
item = Table('item', metadata)
valorInt = Table('valorint',metadata)
valorBool = Table('valorbool',metadata)
valorStr = Table('valorstr',metadata)
valorDate = Table('valordate',metadata)
miembro=Table('miembro',metadata)
session = db_session()
user = Usuario(nombre="Administrador", nombredeusuario="admin", clave=hashlib.sha1( "123456" ).hexdigest(), isAdmin="true")
try:
    session.add(user)
    session.commit()
except:
    pass
# user2 = Usuario(nombre="Natalia Valdez", nombredeusuario="natalia", clave=hashlib.sha1( "admin2" ).hexdigest(), isAdmin="true")
# session.add(user2)
# user3 = Usuario(nombre="Martin Poletti", nombredeusuario="martin", clave=hashlib.sha1( "martin" ).hexdigest(), isAdmin="false")
# session.add(user3) 
# session.commit()
# 
# pro = Proyecto(nombre="Proyecto 1", cantFase="3", fechaInicio="12/01/2013", fechaFin = "10/05/2015",fechaUltMod=None, delider = "3", estado="Iniciado")
# session.add(pro)
# pro2 = Proyecto(nombre="Proyecto 2", cantFase="2", fechaInicio="10/03/2013", fechaFin = "10/05/2015",fechaUltMod=None, delider = "1", estado="Pendiente")
# session.add(pro2)
# pro3 = Proyecto(nombre="Contruccion", cantFase="1", fechaInicio="10/03/2013", fechaFin = "10/05/2015",fechaUltMod=None, delider = "1", estado="Pendiente")
# session.add(pro3)
# session.commit()

# mie=Miembro(proyecto_id="1",user_id="3")
# session.add(mie)
# mie2=Miembro(proyecto_id="2",user_id="1")
# session.add(mie2)
# mie3=Miembro(proyecto_id="3",user_id="1")
# session.add(mie3)
# session.commit()
# 
# fa = Fase(nombre="Fase 1", numero="1", fechaInicio="12/01/2013", fechaFin = "10/02/2013",
#           fechaUltMod="01/02/2013", estado = "Abierta", delproyecto= "1")
# session.add(fa)
# fa2 = Fase(nombre="Fase 2", numero="2", fechaInicio="10/02/2013", fechaFin = "10/07/2013",
#           fechaUltMod=None, estado = "Abierta", delproyecto= "1")
# session.add(fa2)
# fa3 = Fase(nombre="Fase 3", numero="3", fechaInicio="10/07/2013", fechaFin = "10/02/2014",
#           fechaUltMod=None, estado = "Abierta", delproyecto= "1")
# session.add(fa3)
# fa4 = Fase(nombre="Comienzo", numero="1", fechaInicio="12/01/2013", fechaFin = "10/02/2013",
#           fechaUltMod="01/02/2013", estado = "Abierta", delproyecto= "2")
# session.add(fa4)
# fa5 = Fase(nombre="Fin", numero="2", fechaInicio="12/01/2013", fechaFin = "10/02/2013",
#           fechaUltMod="01/02/2013", estado = "Abierta", delproyecto= "2")
# session.add(fa5)
# fa6 = Fase(nombre="Inicio", numero="1", fechaInicio="12/01/2013", fechaFin = "10/02/2013",
#           fechaUltMod="01/02/2013", estado = "Abierta", delproyecto= "3")
# session.add(fa6)
# session.commit()
#
#tItem = TipoItem(nombre="Cosa", comentario="Representa una cosa", defase="1")
#session.add(tItem)
#tItem2 = TipoItem(nombre="Persona", comentario="representa una persona", defase="1")
#session.add(tItem2)
#tItem3 = TipoItem(nombre="Techo", comentario="Representa un techo", defase="6")
#session.add(tItem3)
#tItem4 = TipoItem(nombre="Puerta", comentario="Representa una puerta", defase="6")
#session.add(tItem4)
#tItem5 = TipoItem(nombre="Ventana", comentario="Representa una ventana", defase="6")
#session.add(tItem5)
#tItem6 = TipoItem(nombre="Auto", comentario="Representa un auto", defase="2")
#session.add(tItem6)
#tItem7 = TipoItem(nombre="Libro", comentario="Representa un libro", defase="4")
#session.add(tItem7)
#tItem8 = TipoItem(nombre="Leccion", comentario="Representa una leccion", defase="4")
#session.add(tItem8)
#tItem9 = TipoItem(nombre="Capitulo", comentario="Representa un capitulo", defase="4")
#session.add(tItem9)
#tItem10 = TipoItem(nombre="Conclusion", comentario="Representa una conclusion", defase="5")
#session.add(tItem10)
#session.commit()
#
#atr = Atributo(nombre="Nombre", tipoDato="Cadena", pertenece="2")
#session.add(atr)
#atr2 = Atributo(nombre="Apellido", tipoDato="Cadena", pertenece="2")
#session.add(atr2)
#atr3 = Atributo(nombre="Edad", tipoDato="Numerico", pertenece="2")
#session.add(atr3)
#atr4 = Atributo(nombre="Fecha nacimiento", tipoDato="Fecha", pertenece="2")
#session.add(atr4)
#atr5 = Atributo(nombre="Ancho", tipoDato="Numerico", pertenece="5")
#session.add(atr5)
#atr6 = Atributo(nombre="Alto", tipoDato="Numerico", pertenece="5")
#session.add(atr6)
#atr7 = Atributo(nombre="Numero", tipoDato="Numerico", pertenece="9")
#session.add(atr7)
#atr8 = Atributo(nombre="Titulo", tipoDato="Cadena", pertenece="7")
#session.add(atr8)
#atr9 = Atributo(nombre="Autor", tipoDato="Cadena", pertenece="7")
#session.add(atr9)
#atr10 = Atributo(nombre="Leido", tipoDato="Booleano", pertenece="7")
#session.add(atr10)
#atr11 = Atributo(nombre="Leido", tipoDato="Booleano", pertenece="10")
#session.add(atr11)
#atr12 = Atributo(nombre="Leido", tipoDato="Booleano", pertenece="9")
#session.add(atr12)
#atr13 = Atributo(nombre="Aprendida", tipoDato="Booleano", pertenece="8")
#session.add(atr13)
#atr14 = Atributo(nombre="Numero", tipoDato="Numerico", pertenece="8")
#session.add(atr14)
#session.commit()
#
#itm = Item(tipo="2", etiqueta="1-1-1",fechaCreacion="12/01/2013")#1
#session.add(itm)
#itm = Item(tipo="1",etiqueta="1-1-2",fechaCreacion="12/01/2013")#2
#session.add(itm)
#itm = Item(tipo="6",etiqueta="1-2-1",fechaCreacion="12/01/2013")#3
#session.add(itm)
#itm = Item(tipo="6",etiqueta="1-2-2",fechaCreacion="12/01/2013")#4
#session.add(itm)
#"""itm = Item(tipo="3",etiqueta="1-6-1",fechaCreacion="12/01/2013")#5
#session.add(itm)
#itm = Item(tipo="4",etiqueta="1-6-2",fechaCreacion="12/01/2013")#6
#session.add(itm)
#itm = Item(tipo="5",etiqueta="1-6-3",fechaCreacion="12/01/2013")#7
#session.add(itm)
#itm = Item(tipo="7",etiqueta="1-4-1")#8
#session.add(itm)"""
#session.commit()
#
#vitm = VersionItem(version="1", nombre="a1", estado="Activo", actual="false", costo="50", dificultad="5", deitem="1")
#session.add(vitm)
#vitm2 = VersionItem(version="2", nombre="a1", estado="Activo", actual="true", costo="15", dificultad="55",deitem="1")
#session.add(vitm2)
#vitm3 = VersionItem(version="1", nombre="a2", estado="Activo", actual="true", costo="65", dificultad="100",deitem="2")
#session.add(vitm3)
#vitm4 = VersionItem(version="1", nombre="Nissan", estado="Activo", actual="true", costo="80", dificultad="50",deitem="3")
#session.add(vitm4)
#vitm5 = VersionItem(version="1", nombre="Toyota", estado="Activo", actual="true", costo="95", dificultad="50",deitem="4")
#session.add(vitm5)
#"""vitm5 = VersionItem(version="1", nombre="De cocina", estado="Activo", actual="true", costo="95", dificultad="50",deitem="5")
#session.add(vitm5)
#vitm5 = VersionItem(version="1", nombre="Principal", estado="Activo", actual="true", costo="95", dificultad="50",deitem="6")
#session.add(vitm5)
#vitm5 = VersionItem(version="1", nombre="Persiana", estado="Activo", actual="true", costo="95", dificultad="50",deitem="7")
#session.add(vitm5)
#vitm5 = VersionItem(version="1", nombre="Calculo", estado="Activo", actual="true", costo="95", dificultad="50",deitem="8")
#session.add(vitm5)"""
#session.commit()
#
#vl1 = ValorStr(atributo="1", item="1",valor="Pedro")
#session.add(vl1)
#vl2 = ValorStr(atributo="2",item="1", valor="Perez")
#session.add(vl2)
#vl3 = ValorNum(atributo="3",item="1", valor="24")
#session.add(vl3)
#vl4 = ValorDate(atributo="4",item="1", valor="12/01/1989")
#session.add(vl4)
#vl5 = ValorStr(atributo="1",item="2", valor="Juan")
#session.add(vl5)
#vl6 = ValorStr(atributo="2",item="2", valor="Benitez")
#session.add(vl6)
#vl7 = ValorNum(atributo="3",item="2", valor="33")
#session.add(vl7)
#vl8 = ValorDate(atributo="4",item="2", valor="12/01/1980")
#session.add(vl8)
#session.commit()
#
# rol=Rol(fase_id="1",nombre="Todo",codigoItem="11111111",codigoTipo="111",codigoLB="1")
# session.add(rol)
# rol2=Rol(fase_id="1",nombre="Item",codigoItem="11111111",codigoTipo="000",codigoLB="0")
# session.add(rol2)
# rol3=Rol(fase_id="1",nombre="Nada",codigoItem="0",codigoTipo="000",codigoLB="0")
# session.add(rol3)
# rol4=Rol(fase_id="1",nombre="TipoDeItem",codigoItem="0",codigoTipo="111",codigoLB="0")
# session.add(rol4)
# rol4=Rol(fase_id="2",nombre="TipoDeItem",codigoItem="0",codigoTipo="111",codigoLB="0")
# session.add(rol4)
# rol=Rol(fase_id="2",nombre="Todo",codigoItem="11111111",codigoTipo="111",codigoLB="1")
# session.add(rol)
# rol=Rol(fase_id="3",nombre="Todo",codigoItem="11111111",codigoTipo="111",codigoLB="1")
# session.add(rol)
# rol=Rol(fase_id="4",nombre="Todo",codigoItem="11111111",codigoTipo="111",codigoLB="1")
# session.add(rol)
# rol=Rol(fase_id="5",nombre="Todo",codigoItem="11111111",codigoTipo="111",codigoLB="1")
# session.add(rol)
# rol=Rol(fase_id="6",nombre="Todo",codigoItem="11111111",codigoTipo="111",codigoLB="1")
# session.add(rol)
# session.commit()
# 
# ur=User_Rol(usuario_id="1",rol_id="1")
# session.add(ur)
# ur2=User_Rol(usuario_id="2",rol_id="2")
# session.add(ur2)
# ur3=User_Rol(usuario_id="3",rol_id="3")
# session.add(ur3)
# session.commit()
#
#rel=Relacion(ante_id="2",post_id="3",tipo="P-H")
#session.add(rel)
#session.commit()