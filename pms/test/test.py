'''
Created on 25/04/2013

@author: synchro
'''
import pms
import unittest
from pms.modelo.entidad import Usuario

class PMSTestSuite(unittest.TestCase):

    def setUp(self):
        pms.app.config['TESTING'] = True
        self.app = pms.app.test_client()

    def tearDown(self):
        pass

    def login(self, username, password):
        return self.app.post('/', data=dict(
            username=username,
            passwd=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.post('/',data='logout',follow_redirects=True)

    def testStart(self):
        rv = self.app.get('/')
        assert 'Project Manager System' in rv.data

    def testLogin(self):
        rv = self.login('trudy', '123456')
        assert 'Nombre de usuario no existe o clave incorrecta' in rv.data
        
        rv = self.login(pms.app.config['DEFAULT_USER'], '123465trudy')
        assert 'Nombre de usuario no existe o clave incorrecta' in rv.data
        
        rv = self.login(pms.app.config['DEFAULT_USER'], pms.app.config['DEFAULT_PASSWORD'])
        assert 'Listado de Proyectos' in rv.data
        
        rv = self.logout()
        #print rv.data
        assert 'Logout' in rv.data
    
    def testCreateUser(self):
        self.login(pms.app.config['DEFAULT_USER'], pms.app.config['DEFAULT_PASSWORD'])
        fullname = 'The Dummy User'
        username = 'dummyUser'
        password = 'dummy'
        # The Buttons should be followed by the TestingSuite
        rv = self.app.post('/admusuario/crearusuario/Crear', data=dict(nombre=fullname, usuario=username, clave=password, admin=False),follow_redirects=True)
        print rv.data
        assert 'The Dummy User' in rv.data 