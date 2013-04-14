'''
Created on 05/04/2013

@author: synchro
'''
from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper
from initdb import metadata, db_session, init_db

class Usuario(object):
    """
    define la clase usuario
    """
    query = db_session.query_property()
    def __init__(self, nombre=None,nombredeusuario=None, clave=None, isAdmin=None):
        self.nombre = nombre
        self.nombredeusuario= nombredeusuario
        self.clave = clave
        self.isAdmin = isAdmin
    def __repr__(self):
        return '<Usuario %r>' % (self.nombre)
usuario = Table('usuario', metadata,
    Column('idd', Integer, primary_key=True),
    Column('nombre', String(20)),
    Column('nombredeusuario', String(20), unique=True),
    Column('clave', String(10)),
    Column('isAdmin',Boolean)
    )
    
mapper(Usuario, usuario)        
init_db()