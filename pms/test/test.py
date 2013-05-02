'''
Created on 25/04/2013

@author: synchro
'''
import pms
import unittest
from pms.modelo import proyectoControlador
from pms.modelo.entidad import Proyecto
from pms.modelo.proyectoControlador import getProyecto
from pms.modelo.faseControlador import getFase

class PMSTestSuite(unittest.TestCase):
    index = '/'
    projectTitle = 'de manera organizada y eficiente.'
    inicilizarQuery = 'Esta seguro que desea Inicializar'
    crearFaseOK = 'CREACION EXITOSA'
    editarFaseOK = 'EDICION EXITOSA'
    eliminarFaseOK = 'ELIMINACION EXITOSA'
    listProject = 'Listado de Proyectos'
    listUser ='Listado de Usuarios'
    listFase = 'Listado de Fases'
    editarUsuarioTitle = 'Editar Usuario'
    editarFaseTitle = 'Editar Fase'
    failLogin = 'Nombre de usuario no existe o clave incorrecta'
    failCreateProjectMsg = 'El proyecto ya existe'
    failCreateFaseMsg = 'La fase ya existe'
    failCreateFaseDateMsg =  'Incoherencia entre fechas de inicio y de fin'
    logoutMessage = 'El logueo es necesario'
    crearUsuarioURL = '/admusuario/crearusuario/'
    editarUsuarioURL = '/admusuario/editarusuario/'
    eliminarUsuarioURL = '/admusuario/eliminarusuario/'
    crearProyectoURL = '/admproyecto/crearproyecto/'
    eliminarProyectoURL = '/admproyecto/eliminarproyecto/'
    faseURL = '/admfase/'
    crearFaseURL = faseURL + 'crearfase/'
    editarFaseURL = faseURL + 'editarfase/'
    eliminarFaseURL = faseURL + 'eliminarfase/'
    inicializarProyectoURL = faseURL + 'inicializarproyecto/'

    def setUp(self):
        pms.app.config['TESTING'] = True
        self.app = pms.app.test_client()

    def tearDown(self):
        pass

    def login(self, username=None, password=None):
        if username == None:
            username = pms.app.default_user
        if password == None:
            password = pms.app.default_password
            
        return self.app.post('/', data=dict(
            username=username,
            passwd=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.post('/', data=dict(logout='logout'), follow_redirects=True)
    
    def testRoute(self,url=None,assertion=None):
        if url == None:
            url = self.index
            
        if assertion == None:
            assertion = self.projectTitle
            
        rv = self.app.get(url,follow_redirects=True)
        assert assertion in rv.data
    
    def testInicializarProyecto(self, proyecto=None):
        if proyecto != None:
            id = proyecto.id
            self.testRoute(self.faseURL + id.__str__(), self.listFase)
            self.testRoute(self.inicializarProyectoURL, self.incializarQuery)
            rv = self.app.post(self.inicializarProyectoURL, follow_redirects=True)
            assert self.listProject in rv.data
        else:
            assert False
        #
        #    Deberia leer Inicializacion Exitosa o algo asi
        #
        proyecto = getProyecto(proyecto.nombre)
        assert proyecto.estado == 'Iniciado'
    
    def helperEliminar(self,entidadTitle,entidadValue):
        return 'Eliminar ' + entidadTitle + ' <em>'+ entidadValue + '</em>'

    def testInicio(self):
        self.testRoute(self.index, self.projectTitle)
        print 'Proyect initial page [OK]'

    def testIniciarCerrarSesion(self):
        rv = self.login(username='trudy')
        assert self.failLogin in rv.data
        
        rv = self.login(password='123465trudy')
        assert self.failLogin in rv.data
        
        rv = self.login()
        assert self.listProject in rv.data
        
        rv = self.logout()
        assert self.logoutMessage in rv.data
        
        # Repetir el proceso
        rv = self.login()
        assert self.listProject in rv.data
        
        rv = self.logout()
        assert self.logoutMessage in rv.data
        print 'Correct/Incorrect Authentication [OK]'
    
    def testCRUDUsuario(self):
        # Dummy data
        fullname = 'The Dummy User'
        username = 'dummyUser'
        password = 'dummy'
        
        #Login
        rv = self.login()
        assert self.listProject in rv.data 
        
        #Crear Usuario
        rv = self.app.post(self.crearUsuarioURL, data=dict(nombre=fullname,
                                                                usuario=username,
                                                                clave=password),
                           follow_redirects=True)
        assert fullname in rv.data
        
        #Editar Usuario
        othername = 'Other Dummy User'
        rv = self.app.get( self.editarUsuarioURL + username, follow_redirects=True)
        assert self.editarUsuarioTitle in rv.data
        assertionTmp = 'value="' + username + '"' 
        assert assertionTmp in rv.data
        rv = self.app.post(self.editarUsuarioURL, data=dict(nombre=othername,
                                                                   usuario=username,
                                                                   clave=password),
                           follow_redirects=True) 
        assert self.listUser in rv.data
        assert othername in rv.data
        
        #Logout, Login con el nuevo usuario
        rv = self.logout()
        assert self.logoutMessage in rv.data
        
        rv = self.login(username, password)
        assert self.listProject in rv.data
        
        rv = self.logout()
        assert self.logoutMessage in rv.data
        
        rv = self.login()
        assert self.listProject in rv.data 
        
        #Eliminar Usuario
        self.testRoute(self.eliminarUsuarioURL + username, self.helperEliminar('Usuario',othername))
        
        rv = self.app.post(self.eliminarUsuarioURL,follow_redirects=True)
        assert self.listUser in rv.data
        assert username not in rv.data
        print 'CRUD Usuario [OK]'
    
    def testCRUDProyecto(self):
        # Dummy data
        nombre = 'Dummy Project'
        fechaInicio = '2013-10-10'
        fechaFin = '2014-10-10'
        lider = '1'
        
        #Login
        rv = self.login()
        assert self.listProject in rv.data 
        
        #Crear Proyecto
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombre,
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                lider=lider),
                           follow_redirects=True)
        assert nombre in rv.data
        
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombre,
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                lider=lider),
                           follow_redirects=True)
        assert self.failCreateProjectMsg in rv.data
        
        tempProyecto = getProyecto(nombre)
        
        #Eliminar Proyecto
        self.testRoute(self.eliminarProyectoURL + tempProyecto.id.__str__(), self.helperEliminar('Proyecto', nombre))
        
        rv = self.app.post(self.eliminarProyectoURL,follow_redirects=True)
        assert self.listProject in rv.data
        assert nombre not in rv.data
        
        print 'CRUD Proyecto [OK]'


#    def testCRUDFase(self):
#        # Dummy data
#        nombre = 'Dummy Fase'
#        fechaInicio = '2013-10-11'
#        fechaFin = '2013-12-11'
#        numero = '1'
#        
#        #Login
#        rv = self.login()
#        assert self.listProject in rv.data 
#        
#        #Crear Proyecto
#        nombreProyecto = 'Dummy Project'
#        fechaInicioProyecto = '2013-10-10'
#        fechaFinProyecto = '2014-10-10'
#        liderProyecto = '1'
#        
#        #Login
#        rv = self.login()
#        assert self.listProject in rv.data 
#        
#        #Crear Proyecto
#        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombreProyecto,
#                                                                fechainicio=fechaInicioProyecto,
#                                                                fechafin=fechaFinProyecto,
#                                                                lider=liderProyecto),
#                           follow_redirects=True)
#        assert nombreProyecto in rv.data
#        
#        
#        #Crear Fase
#        
#        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), nombreProyecto)
#        
#        
#        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre,
#                                                                fechainicio=fechaInicio,
#                                                                fechafin=fechaFin,
#                                                                numero=numero),
#                           follow_redirects=True)
#        assert nombre in rv.data
#        
#        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre,
#                                                                fechainicio=fechaInicio,
#                                                                fechafin=fechaFin,
#                                                                numero=numero),
#                           follow_redirects=True)
#        assert self.failCreateFaseMsg in rv.data
#        
#        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre,
#                                                                fechainicio=fechaInicio,
#                                                                fechafin=fechaInicio,
#                                                                numero=numero + '1'),
#                           follow_redirects=True)
#        assert self.failCreateFaseDateMsg in rv.data
#        
#        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre+'B',
#                                                                fechainicio=fechaInicio,
#                                                                fechafin=fechaFin,
#                                                                numero=numero + '1'),
#                           follow_redirects=True)
#        assert self.listFase in rv.data
#        assert self.crearFaseOK in rv.data
#        
#        faseTemp = getFase(numero + '1' , getProyecto(nombreProyecto).id.__str__())        
#        #Eliminar Fase
#        self.testRoute(self.eliminarFaseURL + faseTemp.id.__str__(), self.helperEliminar('Fase', nombre))
#        
#        rv = self.app.post(self.eliminarFaseURL,follow_redirects=True)
#        assert self.listFase in rv.data
#        assert self.eliminarFaseOK in rv.data
#        assert nombre not in rv.data
#        
#        #Editar Fase
#        faseTemp = getFase(numero , getProyecto(nombreProyecto))
#        self.testRoute(self.editarFaseURL + faseTemp.id.__str__(), self.editarFaseTitle)
#        
#        rv = self.app.post(self.editarFaseURL, data=dict(nombre=nombre + 'ready',
#                                                                fechainicio=fechaInicio,
#                                                                fechafin=fechaFin,
#                                                                numero=numero),
#                           follow_redirects=True)
#        assert self.editarFaseOK in rv.data
#        
#        self.testInicializarProyecto(getProyecto(nombreProyecto))
#        
#        #Eliminar el proyecto y todas sus fases
#        
#        print 'CRUD Proyecto [OK]'
