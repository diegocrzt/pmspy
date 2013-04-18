'''
Created on 05/04/2013

@author: mpoletti
'''
from sqlalchemy import Table
from pms.modelo.entidad import Usuario
from pms.modelo.initdb import metadata, db_session, init_db


init_db()
usuario = Table('usuario', metadata)

session = db_session()

user = Usuario(nombre="Administrador", nombredeusuario="admin", clave="123456", isAdmin="true")
session.add(user)
user2 = Usuario(nombre="Natalia Valdez", nombredeusuario="natalia", clave="admin2", isAdmin="true")
session.add(user2)
user3 = Usuario(nombre="Martin Poletti", nombredeusuario="martin", clave="martin", isAdmin="false")
session.add(user3) 

session.commit()

