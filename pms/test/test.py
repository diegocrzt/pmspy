'''
Created on 05/04/2013

@author: synchro
'''
import unittest
from pms.modelo.entidad import Usuario
from pms.modelo.initdb import metadata, db_session


'''
    Inicializa la base de datos para las pruebas unitarias usando sqlite en ram 
'''
def _initTestingDB():
    from sqlalchemy import create_engine
            
    engine = create_engine('sqlite:///:memory:')
    db_session.configure(bind=engine)
    metadata.bind = engine
    metadata.create_all(engine)

    model = Usuario("Fulano de tal","fulano","fulano",True) 
    db_session.add(model)
        
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
        #from pms.modelos.usuario import Usuario
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
        self.assertEqual(instance.clave, '123456')
        self.assertEqual(instance.isAdmin, "true")
        print 'Agregar usuario: [EXITO]'