'''
Created on 05/04/2013

@author: mpoletti
@author: synchro, Natalia Valdez
@author: mpoletti
'''
from sqlalchemy import Column, Integer, Boolean, ForeignKey, Table, Numeric, REAL, BLOB
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Unicode
from sqlalchemy.types import DateTime
from initdb import init_db
from initdb import Base


class Usuario(Base):

    """
        Define la clase Usuario y la mapea con la tabla usuario
    """
    __tablename__ = 'usuario'

    id = Column(Integer,primary_key = True)
    nombre = Column(Unicode(20))
    nombredeusuario = Column(Unicode(20), unique=True)
    clave = Column(Unicode(41))
    isAdmin = Column(Boolean)
    
    esLider = relationship("Proyecto", backref="lider")
    
    def __init__(self, nombre, nombredeusuario, clave, isAdmin):
        self.nombre = nombre
        self.nombredeusuario = nombredeusuario
        self.clave = clave
        self.isAdmin = isAdmin
    

    def __repr__(self):
        return 'Usuario { ' + self.nombre + '(' + self.nombredeusuario + ')}'
        
class Proyecto(Base):
    """
        Define la clase Proyecto y la mapea con la tabla proyecto
    """
    __tablename__ = 'proyecto'
    id = Column(Integer, primary_key=True)
    nombre = Column(Unicode(20), unique=True)
    cantFase = Column(Integer)
    fechaInicio = Column(DateTime)
    fechaFin = Column(DateTime)
    fechaUltMod = Column(DateTime)
    delider = Column(Integer, ForeignKey('usuario.id') )
    estado = Column(Unicode(10))
    fases = relationship("Fase",order_by="Fase.id",backref="proyecto")

    
    
    def __init__(self, nombre, cantFase, fechaInicio, fechaFin, fechaUltMod, delider, estado):
        self.nombre = nombre
        self.cantFase = cantFase
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaUltMod = fechaUltMod
        self.delider = delider
        self.estado = estado

    
    def __repr__(self):
        return 'Proyecto { ' + self.nombre + ')}'

        


class Fase(Base):
    """
        Define la clase Fase y la mapea con la tabla fase
    """
    __tablename__ = 'fase'
    id = Column(Integer, primary_key=True)
    nombre = Column(Unicode(20))
    numero = Column(Integer)
    fechaInicio = Column(DateTime)
    fechaFin = Column(DateTime)
    fechaUltMod = Column(DateTime)
    estado = Column(Unicode(10))
    delproyecto = Column(Integer, ForeignKey('proyecto.id'))
    
    tipos = relationship("TipoItem", backref="fase")
    
    
    def __init__(self, nombre, numero, fechaInicio, fechaFin, fechaUltMod, estado, delproyecto):
        self.nombre = nombre
        self.numero = numero
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaUltMod = fechaUltMod
        self.estado = estado
        self.delproyecto = delproyecto
    
    def __repr__(self):
        return 'Fase { ' + self.numero + '-' + self.nombre + ')}'
        
        
class TipoItem(Base):
    """
        Define la clase Tipo de Item y la mapea con la tabla tipoitem
    """
    __tablename__ = 'tipoitem'
    id = Column(Integer, primary_key=True)
    nombre = Column(Unicode(20))
    comentario = Column(Unicode(100))
    defase = Column(Integer, ForeignKey('fase.id')) 
    atributos = relationship("Atributo", backref="tipoitem")
    instancias = relationship("Item", backref="tipoitem")
    
    def __init__(self, nombre, comentario, defase):
        self.nombre = nombre
        self.comentario = comentario
        self.defase = defase
        
    def __repr__(self):
        return 'TipoItem { '+self.nombre + '('+ self.comentario+ ')}'
    
        
class Atributo(Base):
    """
        Define la clase Atributo y la mapea con la tabla atributo
    """
    __tablename__ = 'atributo'
    id = Column(Integer, primary_key=True)
    nombre = Column(Unicode(20))
    tipoDato = Column(Unicode(20))
    pertenece = Column(Integer, ForeignKey('tipoitem.id')) 
    
    def __init__(self, nombre, tipoDato, pertenece):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.pertenece = pertenece
        
    def __repr__(self):
        return 'Atributo { '+ self.nombre + '('+ self.tipoDato+ ')}' 
        
class Item(Base):
    """
        Define la clase Item y la mapea con la tabla item
    """
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    tipo = Column(Integer, ForeignKey('tipoitem.id'))
    etiqueta = Column(Unicode(60), unique=True)
    version = relationship("VersionItem", uselist=False, backref="item")
    
    def __init__(self, tipo, etiqueta):
        self.tipo = tipo
        self.etiqueta = etiqueta 
    
    def __repr__(self):
        return 'Item { '+ self.etiqueta + '('+ self.version+ ')}'
        
class VersionItem(Base):
    """
        Define la clase VersionItem y la mapea con la tabla vitem
    """
    __tablename__ = 'vitem'
    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    nombre = Column(Unicode(20))
    estado = Column(Unicode(20))
    actual = Column(Boolean)
    costo = Column(Integer)
    dificultad =Column(Integer)
    archivo= Column(BLOB)
    deitem = Column(Integer, ForeignKey('item.id'))
    atributosint = relationship("ValorNum")
    atributosbool = relationship("ValorBoolean")
    atributosstr = relationship("ValorStr")
    atributosdate = relationship("ValorDate")

    
    def __init__(self, version, nombre, estado, actual, deitem):
        self.version = version
        self.nombre = nombre
        self.estado = estado
        self.actual = actual
        self.deitem = deitem
        
    def __repr__(self):
        return 'VersionItem { '+ self.nombre + '('+ self.version+ ')}'

class ValorNum(Base):
    """
        Define la clase ValorInt y la mapea con la tabla valorint
    """
    __tablename__ = 'valorint'
    atributo_id = Column(Integer, ForeignKey('atributo.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('vitem.id'), primary_key=True)
    valor = Column(REAL)     
    atributo = relationship("Atributo")
    
    def __init__(self, atributo, item, valor):
        self.atributo_id = atributo
        self.item_id = item
        self.valor = valor
        
    def __repr__(self):
        return 'ValorInt { '+ self.valor+ '}'

class ValorBoolean(Base):
    """
        Define la clase ValorBoolean y la mapea con la tabla valorbool
    """
    __tablename__ = 'valorbool'
    atributo_id = Column(Integer, ForeignKey('atributo.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('vitem.id'), primary_key=True)
    valor = Column(Boolean)     
    atributo = relationship("Atributo")
        
    def __init__(self, atributo, item, valor):
        self.atributo_id = atributo
        self.item_id = item
        self.valor = valor
        
class ValorStr(Base):
    """
        Define la clase ValorStr y la mapea con la tabla valorstr
    """
    __tablename__ = 'valorstr'
    atributo_id = Column(Integer, ForeignKey('atributo.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('vitem.id'), primary_key=True)
    valor = Column(Unicode(200))     
    atributo = relationship("Atributo")
        
    def __init__(self, atributo, item, valor):
        self.atributo_id = atributo
        self.item_id = item
        self.valor = valor
        
class ValorDate(Base):
    """
        Define la clase ValorDate y la mapea con la tabla valordate
    """
    __tablename__ = 'valordate'
    atributo_id = Column(Integer, ForeignKey('atributo.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('vitem.id'), primary_key=True)
    valor = Column(DateTime)     
    atributo = relationship("Atributo")
        
    def __init__(self, atributo, item, valor):
        self.atributo_id = atributo
        self.item_id = item
        self.valor = valor
'''
todavia no...
class Relacion(Base):
    """
        Define la clase Relacion y la mapea con la tabla relacion
    """
    __tablename__ = 'relacion'
    id = Column(Integer,primary_key=True)
    pre = Column(Integer,ForeignKey('vitem.id'))
    post = Column(Integer,ForeignKey('vitem.id'))
    tipo = Column(Unicode(15))     
    
    def __init__(self, pre, post, tipo):
        self.pre = pre
        self.post = post
        self.tipo = tipo
'''
init_db()
