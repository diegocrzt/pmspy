'''
Created on 25/04/2013

@author: synchro
'''
import pms
import unittest

class PMSTestSuite(unittest.TestCase):
    
    default_user = 'admin'
    default_password = '123456'

    def setUp(self):
        pms.app.config['TESTING'] = True
        pms.app.config['LOGGER_NAME'] = "/tmp/pmspy.test.log"
        self.app = pms.app.test_client()

    def tearDown(self):
        pass

    def login(self, username, password):
        return self.app.post('/', data=dict(
            username=username,
            passwd=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.post('/', data=dict(logout='logout'), follow_redirects=True)

    def testInicio(self):
        rv = self.app.get('/')
        assert 'Project Manager System' in rv.data
        print 'Proyect initial page [OK]'

    def testIniciarCerrarSesion(self):
        rv = self.login('trudy', self.default_password)
        assert 'Nombre de usuario no existe o clave incorrecta' in rv.data
        
        rv = self.login(self.default_user, '123465trudy')
        assert 'Nombre de usuario no existe o clave incorrecta' in rv.data
        
        rv = self.login(self.default_user, self.default_password)
        assert 'Listado de Proyectos' in rv.data
        
        rv = self.logout()
        assert 'El logueo es necesario:' in rv.data
        
        # Repetir el proceso
        rv = self.login(self.default_user, self.default_password)
        assert 'Listado de Proyectos' in rv.data
        
        rv = self.logout()
        assert 'El logueo es necesario:' in rv.data
        print 'Correct/Incorrect Authentication [OK]'
    
    def testCRUDUsuario(self):
        # Dummy data
        fullname = 'The Dummy User'
        username = 'dummyUser'
        password = 'dummy'
        
        #Login
        rv = self.login(self.default_user, self.default_password)
        assert 'Listado de Proyectos' in rv.data 
        
        #Crear Usuario
        rv = self.app.post('/admusuario/crearusuario/', data=dict(nombre=fullname,
                                                                usuario=username,
                                                                clave=password),
                           follow_redirects=True)
        assert 'The Dummy User' in rv.data
        
        #Editar Usuario
        othername = 'Other Dummy User'
        rv = self.app.get('/admusuario/editarusuario/' + username, follow_redirects=True)
        assert 'Editar Usuario' in rv.data
        assert 'value="' + username + '"' in rv.data
        rv = self.app.post('/admusuario/editarusuario/', data=dict(nombre=othername,
                                                                   usuario=username,
                                                                   clave=password),
                           follow_redirects=True) 
        assert 'Listado de Usuarios' in rv.data
        assert othername in rv.data
        
        #Logout, Login con el nuevo usuario
        rv = self.logout()
        assert 'El logueo es necesario:' in rv.data
        
        rv = self.login(username, password)
        assert 'Listado de Proyectos' in rv.data
        
        rv = self.logout()
        assert 'El logueo es necesario:' in rv.data
        
        rv = self.login(self.default_user, self.default_password)
        assert 'Listado de Proyectos' in rv.data 
        
        #Eliminar Usuario
        rv = self.app.get('/admusuario/eliminarusuario/' + username, follow_redirects=True)
        print rv.data
        assert 'Eliminar Usuario <em>'+ othername + '</em>' in rv.data
        
        rv = self.app.post('/admusuario/eliminarusuario/',follow_redirects=True)
        assert 'Listado de Usuarios' in rv.data
        assert username not in rv.data
        print 'CRUD Usuario [OK]'
    
    
#    def testCRUDProyecto(self):
#         # Dummy data
#        nombre = 'Dummy Proyect'
#        fechaInicio = '2013-10-10'
#        fechaFin = '2014-10-10'
#        lider = '1'
#        
#        #Login
#        rv = self.login(self.default_user, self.default_password)
#        assert 'Listado de Proyectos' in rv.data 
#        
#        #Crear Usuario
#        rv = self.app.post('/admproyecto/crearproyecto/', data=dict(nombre=nombre,
#                                                                fechainicio=fechaInicio,
#                                                                fechafin=fechaFin,
#                                                                lider=lider),
#                           follow_redirects=True)
#        assert nombre in rv.data
#        
#        rv = self.app.post('/admproyecto/crearproyecto/', data=dict(nombre=nombre,
#                                                                fechainicio=fechaInicio,
#                                                                fechafin=fechaFin,
#                                                                lider=lider),
#                           follow_redirects=True)
#        assert 'El proyecto ya existe' in rv.data
#        
#        #Eliminar Usuario
#        rv = self.app.get('/admproyecto/eliminarproyecto/' + nombre, follow_redirects=True)
#        print rv.data
#        assert 'Eliminar Proyecto <em>'+ nombre + '</em>' in rv.data
#        
#        rv = self.app.post('/admproyecto/eliminarproyecto/',follow_redirects=True)
#        assert 'Listado de Proyectos' in rv.data
#        assert nombre not in rv.data
#        print 'CRUD Proyecto [OK]'