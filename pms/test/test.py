'''
Created on 05/04/2013

@author: synchro
'''
import unittest
from pms.modelo.entidad import Usuario, Proyecto, Fase
from pms.modelo.initdb import metadata, db_session
import pms


'''
    Inicializa la base de datos para las pruebas unitarias usando sqlite en ram 
'''
def _initTestingDB():
    from sqlalchemy import create_engine
    #pms.main.app.config['TESTING'] = True

    engine = create_engine('sqlite:///:memory:')
    db_session.configure(bind=engine)
    metadata.bind = engine
    metadata.create_all(engine)

#     model = Usuario("Fulano de tal","fulano","fulano",True) 
#     db_session.add(model)
        
    return db_session
'''
    Clase para pruebas unitarias
    @param TestCase: Caso de prueba del paquete unittest  
'''
class UsuarioTest(unittest.TestCase):
    '''
        Inicializa la base de datos
        @param self: caso de pruebas
    '''
    
    def setUp(self):
        self.session = _initTestingDB()    
    '''
        Remueve la base de datos
        @param self: caso de pruebas
    '''
    def tearDown(self):
        self.session.remove()

    '''
        Devuelve la clase usada en las pruebas
        @param self: caso de pruebas
        @return: Usuario 
    '''
    def _getTargetClass(self):
        return Usuario
    
    '''
        Crea una instancia de la clase de pruebas
        @param self: caso de pruebas
        @param campos de la clase: campos que tiene la clase mapeada a la base de datos 
        @return: Usuario
    '''
    def _makeOne(self, nombre="Fulano de Tal", nombredeusuario="fulano", clave="123456", isAdmin="true"):
        return self._getTargetClass()(nombre,nombredeusuario,clave,isAdmin)
    
    '''
        Prueba el constructor de la clase, e imprime un mensaje en caso de superar la prueba
        @param self: caso de pruebas
    '''
    def test_constructor(self):
        instance = self._makeOne()
        self.assertEqual(instance.nombre, 'Fulano de Tal')
        self.assertEqual(instance.nombredeusuario, 'fulano')
        self.assertEqual(instance.isAdmin, "true")
        print 'Agregar usuario: [EXITO]'
        
        
class ProyectoTest(unittest.TestCase):
    '''
        Inicializa la base de datos
        @param self: caso de pruebas
    '''
    def setUp(self):
        self.session = _initTestingDB()    
    '''
        Remueve la base de datos
        @param self: caso de pruebas
    '''
    def tearDown(self):
        self.session.remove()

    '''
        Devuelve la clase usada en las pruebas
        @param self: caso de pruebas
        @return: Proyecto
    '''
    def _getTargetClass(self):
        return Proyecto
    
    '''
        Crea una instancia de la clase de pruebas
        @param self: caso de pruebas
        @param campos de la clase: campos que tiene la clase mapeada a la base de datos 
        @return: Proyecto
    '''
    def _makeOne(self, nombre="Proyecto Test", cantFase="1", fechaInicio="12/01/2013", fechaFin = "10/05/2015",fechaUltMod=None, lider = "1", estado="Pendiente"):
        return self._getTargetClass()(nombre, cantFase, fechaInicio, fechaFin, fechaUltMod, lider, estado)
    
    '''
        Prueba el constructor de la clase, e imprime un mensaje en caso de superar la prueba
        @param self: caso de pruebas
    '''
    def test_constructor(self):
        instance = self._makeOne()
        self.assertEqual(instance.nombre, 'Proyecto Test')
        self.assertEqual(instance.cantFase, '1')
        self.assertEqual(instance.fechaInicio, '12/01/2013')
        self.assertEqual(instance.fechaFin, "10/05/2015")
        self.assertEqual(instance.fechaUltMod, None)
        self.assertEqual(instance.lider, "1")
        self.assertEqual(instance.estado, "Pendiente")
        print 'Agregar proyecto: [EXITO]'


class FaseTest(unittest.TestCase):
    '''
        Inicializa la base de datos
        @param self: caso de pruebas
    '''
    def setUp(self):
        self.session = _initTestingDB()    
    '''
        Remueve la base de datos
        @param self: caso de pruebas
    '''
    def tearDown(self):
        self.session.remove()

    '''
        Devuelve la clase usada en las pruebas
        @param self: caso de pruebas
        @return: Fase 
    '''
    def _getTargetClass(self):
        return Fase
    
    '''
        Crea una instancia de la clase de pruebas
        @param self: caso de pruebas
        @param campos de la clase: campos que tiene la clase mapeada a la base de datos 
        @return: Fase
    '''
    def _makeOne(self, nombre="Fase 1", numero="1", fechaInicio="12/01/2013", fechaFin = "10/05/2015",
          fechaUltMod="01/02/2013", estado = "Abierta", proyecto= "1"):
        return self._getTargetClass()(nombre, numero, fechaInicio, fechaFin, fechaUltMod, estado, proyecto)
    
    '''
        Prueba el constructor de la clase, e imprime un mensaje en caso de superar la prueba
        @param self: caso de pruebas
    '''
    def test_constructor(self):
        instance = self._makeOne()
        self.assertEqual(instance.nombre, 'Fase 1')
        self.assertEqual(instance.numero, '1')
        self.assertEqual(instance.fechaInicio, '12/01/2013')
        self.assertEqual(instance.fechaFin, "10/05/2015")
        self.assertEqual(instance.fechaUltMod, '01/02/2013')
        self.assertEqual(instance.estado, "Abierta")
        self.assertEqual(instance.proyecto, "1")
        print 'Agregar fase: [EXITO]'