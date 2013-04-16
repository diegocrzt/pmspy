'''
Created on 05/04/2013

@author: synchro
'''
from sqlalchemy import Column, Integer, Boolean
from initdb import init_db
from initdb import Base
from sqlalchemy.types import Unicode
from sqlalchemy.types import DateTime



class Usuario(Base):
    """
        Define la clase Usuario y la mapea con la tabla usuario
    """
    __tablename__ = 'usuario'
    idd = Column(Integer,primary_key = True)
    nombre = Column(Unicode(20))
    nombredeusuario = Column(Unicode(20), unique=True)
    clave = Column(Unicode(10))
    isAdmin = Column(Boolean)
    
    def __init__(self, nombre,nombredeusuario, clave, isAdmin):
        self.nombre = nombre
        self.nombredeusuario= nombredeusuario
        self.clave = clave
        self.isAdmin = isAdmin

    def get_idd(self):
        return self.__idd


    def get_nombre(self):
        return self.__nombre


    def get_nombredeusuario(self):
        return self.__nombredeusuario


    def get_clave(self):
        return self.__clave


    def set_idd(self, value):
        self.__idd = value


    def set_nombre(self, value):
        self.__nombre = value


    def set_nombredeusuario(self, value):
        self.__nombredeusuario = value


    def set_clave(self, value):
        self.__clave = value
        
        
        
class Proyecto(Base):
    """
        Define la clase proyecto y la mapea con la tabla proyecto
    """
    __tablename__ = 'proyecto'
    id = Column(Integer,primary_key=True)
    nombre = Column(Unicode(10),unique=True)
    cantFase = Column(Integer)
    fechaInicio = Column(DateTime)
    fechaFin = Column(DateTime)
    fechaUltMod = Column(DateTime)
    
    def __init__(self,nombre,cantFase,fechaInicio,fechaFin,fechaUltMod):
        self.nombre = nombre
        self.cantFase = cantFase
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaUltMod = fechaUltMod

    def get_nombre(self):
        return self.__nombre


    def get_cant_fase(self):
        return self.__cantFase


    def get_fecha_inicio(self):
        return self.__fechaInicio


    def get_fecha_fin(self):
        return self.__fechaFin


    def get_fecha_ult_mod(self):
        return self.__fechaUltMod


    def set_nombre(self, value):
        self.__nombre = value


    def set_cant_fase(self, value):
        self.__cantFase = value


    def set_fecha_inicio(self, value):
        self.__fechaInicio = value


    def set_fecha_fin(self, value):
        self.__fechaFin = value


    def set_fecha_ult_mod(self, value):
        self.__fechaUltMod = value

init_db()