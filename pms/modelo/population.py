'''
Created on 05/04/2013

@author: mpoletti
'''
from sqlalchemy import Table
from pms.modelo.entidad import Usuario, Proyecto, Fase, TipoItem, Atributo, Item, ValorNum, ValorStr, ValorBoolean, ValorDate, VersionItem, Rol, User_Rol, Relacion
from pms.modelo.initdb import metadata, db_session, init_db, engine
import hashlib
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
session = db_session()

user = Usuario(nombre="Administrador", nombredeusuario="admin", clave=hashlib.sha1( "123456" ).hexdigest(), isAdmin="true")
session.add(user)
user2 = Usuario(nombre="Natalia Valdez", nombredeusuario="natalia", clave=hashlib.sha1( "admin2" ).hexdigest(), isAdmin="true")
session.add(user2)
user3 = Usuario(nombre="Martin Poletti", nombredeusuario="martin", clave=hashlib.sha1( "martin" ).hexdigest(), isAdmin="false")
session.add(user3) 
session.commit()

pro = Proyecto(nombre="Proyecto 1", cantFase="1", fechaInicio="12/01/2013", fechaFin = "10/05/2015",fechaUltMod=None, delider = "3", estado="Pendiente")
session.add(pro)
session.commit()

fa = Fase(nombre="Fase 1", numero="1", fechaInicio="12/01/2013", fechaFin = "10/05/2015",
          fechaUltMod="01/02/2013", estado = "Abierta", delproyecto= "1")
session.add(fa)
session.commit()

tItem = TipoItem(nombre="cosa", comentario="representa una cosa", defase="1")
session.add(tItem)
tItem2 = TipoItem(nombre="persona", comentario="representa una persona", defase="1")
session.add(tItem2)
session.commit()

atr = Atributo(nombre="nombre", tipoDato="Cadena", pertenece="2")
session.add(atr)
atr2 = Atributo(nombre="apellido", tipoDato="Cadena", pertenece="2")
session.add(atr2)
atr3 = Atributo(nombre="edad", tipoDato="Numerico", pertenece="2")
session.add(atr3)
atr4 = Atributo(nombre="fecha nacimiento", tipoDato="Fecha", pertenece="2")
session.add(atr4)
session.commit()

itm = Item(tipo="2", etiqueta="p1f1i1")
session.add(itm)
itm = Item(tipo="1",etiqueta="p1f1i2")
session.add(itm)
session.commit()

vitm = VersionItem(version="1", nombre="a1", estado="Activo", actual="false", costo="5", dificultad="5", deitem="1")
session.add(vitm)
vitm2 = VersionItem(version="2", nombre="a1", estado="Activo", actual="true", costo="5", dificultad="5",deitem="1")
session.add(vitm2)
vitm3 = VersionItem(version="1", nombre="a2", estado="Activo", actual="true", costo="5", dificultad="5",deitem="2")
session.add(vitm3)
session.commit()

vl1 = ValorStr(atributo="1", item="1",valor="Pedro")
session.add(vl1)
vl2 = ValorStr(atributo="2",item="1", valor="Perez")
session.add(vl2)
vl3 = ValorNum(atributo="3",item="1", valor="24")
session.add(vl3)
vl4 = ValorDate(atributo="4",item="1", valor="12/01/1989")
session.add(vl4)
vl5 = ValorStr(atributo="1",item="2", valor="Juan")
session.add(vl5)
vl6 = ValorStr(atributo="2",item="2", valor="Benitez")
session.add(vl6)
vl7 = ValorNum(atributo="3",item="2", valor="33")
session.add(vl7)
vl8 = ValorDate(atributo="4",item="2", valor="12/01/1980")
session.add(vl8)
session.commit()

rol=Rol(fase_id="1",nombre="todo",codigoItem="1",codigoTipo="111",codigoLB="0")
session.add(rol)
rol2=Rol(fase_id="1",nombre="TnoI",codigoItem="1",codigoTipo="000",codigoLB="0")
session.add(rol2)
rol3=Rol(fase_id="1",nombre="nada",codigoItem="0",codigoTipo="000",codigoLB="0")
session.add(rol3)
rol4=Rol(fase_id="1",nombre="cIT",codigoItem="1",codigoTipo="001",codigoLB="0")
session.add(rol4)
session.commit()

ur=User_Rol(usuario_id="1",rol_id="1")
session.add(ur)
ur2=User_Rol(usuario_id="2",rol_id="2")
session.add(ur2)
ur3=User_Rol(usuario_id="3",rol_id="3")
session.add(ur3)
session.commit()

rel=Relacion(ante_id="2",post_id="3",tipo="P-H")
session.add(rel)
session.commit()