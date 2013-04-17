'''
Created on 05/04/2013

@author: synchro
'''
from sqlalchemy import Table
from pms.modelo.entidad import Usuario, Proyecto
from pms.modelo.initdb import metadata, db_session, init_db


init_db()
usuario = Table('usuario', metadata)
proyecto = Table('proyecto', metadata)

session = db_session()
'''
user = Usuario(nombre="Administrador", nombredeusuario="admin", clave="123456", isAdmin="true")
session.add(user)
user2 = Usuario(nombre="Natalia Valdez", nombredeusuario="natalia", clave="admin2", isAdmin="true")
session.add(user2)
user3 = Usuario(nombre="Martin Poletti", nombredeusuario="martin", clave="martin", isAdmin="false")
session.add(user3) '''

pro = Proyecto(nombre="Proyecto 1", cantFase="0", fechaInicio="12/01/2013", fechaFin = "20/05/1015",fechaUltMod="01/02/2013", lider = "3")
session.add(pro)

session.commit()

