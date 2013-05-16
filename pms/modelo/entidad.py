'''
Created on 05/04/2013

@author: mpoletti
@author: synchro, Natalia Valdez
@author: mpoletti
'''
from sqlalchemy import Column, Integer, Boolean, ForeignKey, Table, Numeric, REAL
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
    lineas = relationship("LineaBase",backref="creador")
    
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
    roles = relationship("Rol",backref="fase")
    lineas = relationship("LineaBase",order_by="LineaBase.numero", backref="fase")
    
    def __init__(self, nombre, numero, fechaInicio, fechaFin, fechaUltMod, estado, delproyecto):
        self.nombre = nombre
        self.numero = numero
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.fechaUltMod = fechaUltMod
        self.estado = estado
        self.delproyecto = delproyecto
    
    def __repr__(self):
        return 'Fase { ' + self.numero.__str__() + '-' + self.nombre + ')}'
        
        
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
    instancias = relationship("Item",order_by="Item.id", backref="tipoitem")
    
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
    version = relationship("VersionItem", backref="item")
    linea_id=Column(Integer, ForeignKey('lineabase.id'))
    
    def __init__(self, tipo, etiqueta,linea_id=None):
        self.linea_id=linea_id
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
    deitem = Column(Integer, ForeignKey('item.id'))
    atributosnum = relationship("ValorNum")
    atributosbool = relationship("ValorBoolean")
    atributosstr = relationship("ValorStr")
    atributosdate = relationship("ValorDate")

    
    def __init__(self, version, nombre, estado, actual, costo, dificultad, deitem):
        self.version = version
        self.nombre = nombre
        self.estado = estado
        self.actual = actual
        self.costo =costo
        self.dificultad=dificultad
        self.deitem = deitem
        
    def __repr__(self):
        return 'VersionItem { '+ self.nombre + '('+ self.version+ ')}'
    
class Relacion(Base):
    """
        Define la clase Relacion y la mapea con la tabla item
    """
    __tablename__ = 'relacion'
    id = Column(Integer,primary_key=True)
    ante_id = Column(Integer, ForeignKey('vitem.id'))
    post_id = Column(Integer, ForeignKey('vitem.id'))
    tipo = Column(Unicode(10))
    ante = relationship("VersionItem", backref="post_list",  primaryjoin=(VersionItem.id == ante_id))
    post = relationship("VersionItem", backref="ante_list",  primaryjoin=(VersionItem.id == post_id))
    
    def __init__(self, ante_id,post_id,tipo):
        self.ante_id = ante_id
        self.post_id = post_id
        self.tipo =tipo

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
        
    def __repr__(self):
        return 'ValorBoolean { '+ self.valor+ '}'
        
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
        
    def __repr__(self):
        return 'ValorStr { '+ self.valor+ '}'
        
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
        
    def __repr__(self):
        return 'ValorDate { '+ self.valor+ '}'
    
    
class Rol(Base):
    """
        Define la clase Rol y la mapea con la tabla valorstr
    """
    __tablename__ = 'rol'
    id = Column(Integer, primary_key=True)
    fase_id = Column(Integer, ForeignKey('fase.id'))
    nombre=Column(Unicode(30))
    codigoTipo = Column(Integer)
    codigoItem = Column(Integer)
    codigoLB = Column(Integer)
    usuarios = relationship("User_Rol",backref="rol")
        
    def __init__(self, fase_id, nombre,codigoTipo,codigoItem,codigoLB):
        self.fase_id = fase_id
        self.nombre = nombre
        self.codigoTipo = codigoTipo
        self.codigoItem = codigoItem
        self.codigoLB = codigoLB
        
    def __repr__(self):
        return 'Rol { '+ self.fase_id + self.nombre + self.codigoTipo + self.codigoItem + self.codigoLB + '}'   

class User_Rol(Base):
    """
        Define la tabla entre el rol y el usuario y la mapea con la tabla valorstr
    """
    __tablename__ = 'user_rol'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    rol_id = Column(Integer, ForeignKey('rol.id'),primary_key=True)
    usuario = relationship("Usuario",backref="elrol")
        
    def __init__(self, usuario_id, rol_id):
        self.usuario_id = usuario_id
        self.rol_id = rol_id
        
    def __repr__(self):
        return 'User_Rol { '+ self.usuario_id+ self.rol_id + '}'
    
class LineaBase(Base):
    """
        Define la clase Linea Base y la mapea a la tabla lineabase
    """
    __tablename__='lineabase'
    id = Column(Integer, primary_key=True)
    creador_id= Column(Integer, ForeignKey('usuario.id'))
    fechaCreacion=Column(DateTime)
    numero=Column(Integer)
    comentario=Column(Unicode(100))
    fase_id = Column(Integer, ForeignKey('fase.id'))
    items = relationship("Item",backref="lineabase")
    
    def __init__(self, creador_id, fechaCreacion, numero, fase_id):
        self.creador_id=creador_id
        self.fechaCreacion=fechaCreacion
        self.numero=numero
        self.fase_id=fase_id
        
    def __repr__(self):
        return 'LineaBase { '+ self.numero+ self.fase_id + self.creador_id + self.fechaCreacion +'}' 

init_db()
