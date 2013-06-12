'''
Created on 25/04/2013

@author: synchro
'''
import pms
import unittest
from pms.modelo import proyectoControlador
from pms.modelo.entidad import Proyecto
from pms.modelo.proyectoControlador import getProyecto, eliminarProyecto, getProyectoId
from pms.modelo.faseControlador import getFase, eliminarFase
from pms.modelo.rolControlador import getRolNombre
from pms.modelo.usuarioControlador import getUsuario
from pms.modelo.tipoItemControlador import getTipoItemNombre, eliminarTipoItem

class PMSTestSuite(unittest.TestCase):
    index = '/'
    projectTitle = 'de manera organizada y eficiente.'
    crearOK = 'CREACION EXITOSA'
    editarOK = 'EDICION EXITOSA'
    eliminarOK = 'ELIMINACION EXITOSA'
    importarOK = 'IMPORTACION EXITOSA'
    consultaRol = 'Consulta de rol'
    listProject = 'Listado de Proyectos'
    listUser = 'Listado de Usuarios'
    listFase = 'Listado de Fases'
    listTipo = 'Listado de Tipos de Items'
    listAtributo = 'Listado de los Atributos'
    editarUsuarioTitle = 'Editar Usuario'
    editarFaseTitle = 'Editar Fase'
    editarRolTitle = 'Editar Rol'
    failLogin = 'Nombre de usuario no existe o clave incorrecta'
    failCreateProjectMsg = 'El proyecto ya existe'
    failCreateFaseMsg = 'La fase ya existe'
    failCreateFaseDateMsg = 'Incoherencia entre fechas de inicio y de fin'
    logoutMessage = 'Login'
    inicializarQuery = 'La Inicializacion de un proyecto es <strong>irreversible</strong>.'
    proyectoURL = '/admproyecto/'
    nextProyectoURL = '/admproyecto/nextproyecto/'
    prevProyectoURL = '/admproyecto/prevproyecto/'
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
    rolURL='/admrol/'
    crearRolURL = rolURL + 'crearrol/'
    editarRolURL = rolURL + 'editarrol/'
    eliminarRolURL = rolURL + 'eliminarrol/'
    asignarRolURL = rolURL + 'asignar/'
    asignarRolActionURL = rolURL + 'asignarrol/'
    desasignarRolURL = rolURL + 'desasignar/'
    desasignarRolActionURL = rolURL + 'desasignarrol/'
    consultarRolURL = rolURL + 'consultarrol/'
    tipoURL = '/admtipo/'
    crearTipoURL = tipoURL + 'creartipo/'
    atributoURL = 'admatributo/'
    crearAtributoURL = atributoURL + 'crearatributo/'
    importarTipoURL = tipoURL + 'admimportartipo/'
    importarTipoActionURL = tipoURL + 'importartipo/'
    
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
   
    def testRoute(self, url=None, assertion=None):
        if url == None:
            url = self.index
           
        if assertion == None:
            assertion = self.projectTitle
           
        rv = self.app.get(url, follow_redirects=True)
        assert assertion in rv.data
   
    def inicializarProyecto(self, proyecto=None):
        id = proyecto.id
        self.testRoute(self.faseURL + id.__str__(), self.listFase)
        self.testRoute(self.inicializarProyectoURL, self.inicializarQuery)
        rv = self.app.post(self.inicializarProyectoURL, follow_redirects=True)
        assert self.listFase in rv.data
        #
        #    Deberia leer Inicializacion Exitosa o algo asi
        #
        proyecto = getProyecto(proyecto.nombre)
        assert proyecto.estado == 'Iniciado'
   
    def testBorrarProyecto(self, nombreProyecto=None):
        if (nombreProyecto):
            eliminarProyecto(getProyecto(nombreProyecto).id)
            return True
        else:
            return True
   
    def helperEliminar(self, entidadTitle, entidadValue):
        return 'Eliminar ' + entidadTitle + ' <em>' + entidadValue + '</em>'
   
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
       
        # Login
        rv = self.login()
        assert self.listProject in rv.data
       
        # Crear Usuario
        rv = self.app.post(self.crearUsuarioURL, data=dict(nombre=fullname,
                                                                usuario=username,
                                                                clave=password),
                           follow_redirects=True)
        assert fullname in rv.data
       
        # Editar Usuario
        othername = 'Other Dummy User'
        rv = self.app.get(self.editarUsuarioURL + username, follow_redirects=True)
        assert self.editarUsuarioTitle in rv.data
        assertionTmp = 'value="' + username + '"'
        assert assertionTmp in rv.data
        rv = self.app.post(self.editarUsuarioURL, data=dict(nombre=othername,
                                                                   usuario=username,
                                                                   clave=password),
                           follow_redirects=True)
        assert self.listUser in rv.data
        assert othername in rv.data
       
        # Logout, Login con el nuevo usuario
        rv = self.logout()
        assert self.logoutMessage in rv.data
       
        rv = self.login(username, password)
        assert self.listProject in rv.data
       
        rv = self.logout()
        assert self.logoutMessage in rv.data
       
        rv = self.login()
        assert self.listProject in rv.data
       
        # Eliminar Usuario
        self.testRoute(self.eliminarUsuarioURL + username, self.helperEliminar('Usuario', othername))
       
        rv = self.app.post(self.eliminarUsuarioURL, follow_redirects=True)
        assert self.listUser in rv.data
        assert username not in rv.data
        print 'CRUD Usuario [OK]'
   
    def testCRUDProyecto(self):
        # Dummy data
        nombre = 'DemoProyect'
        fechaInicio = '2013-10-10'
        fechaFin = '2014-10-10'
        lider = '1'
       
        # Login
        rv = self.login()
        assert self.listProject in rv.data
       
        # Crear Proyecto
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombre,
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                lider=lider),
                           follow_redirects=True)
        assert self.crearOK in rv.data
       
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombre,
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                lider=lider),
                           follow_redirects=True)
        assert self.failCreateProjectMsg in rv.data
       
        tempProyecto = getProyecto(nombre)
       
        # Eliminar Proyecto
        self.testRoute(self.eliminarProyectoURL + tempProyecto.id.__str__(), self.helperEliminar('Proyecto', nombre))
       
        rv = self.app.post(self.eliminarProyectoURL, follow_redirects=True)
        assert self.listProject in rv.data
        assert nombre not in rv.data
       
        print 'CRUD Proyecto [OK]'


    def testCRUDFase(self):
        # Dummy data
        nombre = 'Dummy Fase'
        fechaInicio = '2013-10-11'
        fechaFin = '2013-12-11'
        numero = '1'
       
        # Login
        rv = self.login()
        assert self.listProject in rv.data
       
        # Crear Proyecto
        nombreProyecto = 'Dummy Project'
        fechaInicioProyecto = '2013-10-10'
        fechaFinProyecto = '2014-10-10'
        liderProyecto = '1'
       
        # Crear Proyecto
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombreProyecto,
                                                                fechainicio=fechaInicioProyecto,
                                                                fechafin=fechaFinProyecto,
                                                                lider=liderProyecto),
                           follow_redirects=True)
        assert self.crearOK in rv.data
       
       
        # Crear Fase
       
        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), nombreProyecto)
       
        # Crea Una Fase
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre,
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                numero=numero),
                           follow_redirects=True)
        assert self.crearOK in rv.data
       
        # Intenta Crear la misma fase con los mismo datos
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre,
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                numero=numero),
                           follow_redirects=True)
        assert self.failCreateFaseMsg in rv.data
       
        # Intentar crear otra fase con fechas de inicio/fin iguales
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre,
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaInicio,
                                                                numero=numero + '1'),
                           follow_redirects=True)
        assert self.failCreateFaseDateMsg in rv.data
       
        # Crea una fase 11
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre + 'B',
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                numero=numero + '1'),
                           follow_redirects=True)
        assert self.listFase in rv.data
        assert self.crearOK in rv.data
       
        # Eliminar Fase
        faseTemp = getFase(numero + '1' , getProyecto(nombreProyecto).id.__str__())
        self.testRoute(self.eliminarFaseURL + faseTemp.id.__str__(), 'Eliminar Fase de Proyecto <em>' + nombreProyecto + '</em>')
       
        rv = self.app.post(self.eliminarFaseURL, follow_redirects=True)
        assert self.listFase in rv.data
        assert self.eliminarOK in rv.data
        assert nombre + 'B' not in rv.data
       
        # Editar Fase
        faseTemp = getFase(numero , getProyecto(nombreProyecto).id.__str__())
        self.testRoute(self.editarFaseURL + faseTemp.id.__str__(), self.editarFaseTitle)
       
        rv = self.app.post(self.editarFaseURL, data=dict(nombre=nombre + 'ready',
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                numero=numero),
                           follow_redirects=True)
        assert self.editarOK in rv.data
       
        # Inicializar proyecto
        self.inicializarProyecto(getProyecto(nombreProyecto))
       
        # Eliminar el proyecto y todas sus fases
        assert self.testBorrarProyecto(nombreProyecto)
        
        rv = self.logout()
        assert self.logoutMessage in rv.data
       
        print 'CRUD Fase [OK]'
       
    def nextPag(self):
        rv = self.app.get(self.proyectoURL, follow_redirects=True)
        assert self.nextProyectoURL in rv.data
       
        rv = self.app.get(self.nextProyectoURL, follow_redirects=True)
        assert 'Pagina 2 de' in rv.data
       
    def prevPag(self):
#        rv = self.app.get(self.proyectoURL,follow_redirects=True)
#        assert self.prevProyectoURL in rv.data
       
        rv = self.app.get(self.prevProyectoURL, follow_redirects=True)
        assert 'Pagina 1 de' in rv.data
       
    def testPaginar(self):
        # Login
        rv = self.login()
        assert self.listProject in rv.data
       
        # Crear Proyecto
        nombreProyecto = 'Proyecto '
        fechaInicioProyecto = '2013-10-10'
        fechaFinProyecto = '2014-10-10'
        liderProyecto = '1'
       
        for i in range(1, 15):
            # Crear Proyecto
            rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombreProyecto + i.__str__(),
                                                                    fechainicio=fechaInicioProyecto,
                                                                    fechafin=fechaFinProyecto,
                                                                    lider=liderProyecto),
                               follow_redirects=True)
            assert self.crearOK in rv.data
       
        # Paginar hacia adelante y hacia atras
        self.nextPag()
       
        self.prevPag()
       
        for i in range(1, 15):
            # Eliminar Proyecto
            tempProyecto = getProyecto(nombreProyecto + i.__str__())
            self.testRoute(self.eliminarProyectoURL + tempProyecto.id.__str__(), self.helperEliminar('Proyecto', nombreProyecto + i.__str__()))
       
            rv = self.app.post(self.eliminarProyectoURL, follow_redirects=True)
            assert self.listProject in rv.data
            assert nombreProyecto + i.__str__() not in rv.data
           
        print 'Paginar [OK]'
        
    def testInicializarProyecto(self):
        # Dummy data
        nombre = 'Dummy Fase'
        fechaInicio = '2014-10-11'
        fechaFin = '2015-12-11'
        numero = '1'
        # Crear Proyecto
        nombreProyecto = 'Dummy Project'
        fechaInicioProyecto = '2014-10-10'
        fechaFinProyecto = '2015-10-10'
        liderProyecto = '1'
       
        # Login
        rv = self.login()
        assert self.listProject in rv.data
       
        # Crear Proyecto
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombreProyecto,
                                                                fechainicio=fechaInicioProyecto,
                                                                fechafin=fechaFinProyecto,
                                                                lider=liderProyecto),
                           follow_redirects=True)
        assert self.crearOK in rv.data
       
        # Crear Fase
        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), nombreProyecto)
       
        # Crea Una Fase
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombre,
                                                                fechainicio=fechaInicio,
                                                                fechafin=fechaFin,
                                                                numero=numero),
                           follow_redirects=True)
        assert self.crearOK in rv.data
              
        # Inicializar proyecto
        self.inicializarProyecto(getProyecto(nombreProyecto))
       
        # Eliminar el proyecto y todas sus fases
        assert self.testBorrarProyecto(nombreProyecto)
        
        rv = self.logout()
        assert self.logoutMessage in rv.data
       
        print 'Inicialiar Proyecto [OK]'
        
    def testCRUDRol(self):
        # Dummy data
        nombreFase = 'Dummy Fase'
        fechaInicioFase = '2014-10-11'
        fechaFinFase = '2015-12-11'
        numeroFase = '1'
        # Crear Proyecto
        nombreProyecto = 'Dummy Project'
        fechaInicioProyecto = '2014-10-10'
        fechaFinProyecto = '2015-10-10'
        liderProyecto = '1'
       
        # Login
        rv = self.login()
        assert self.listProject in rv.data
       
        # Crear Proyecto
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombreProyecto,
                                                                fechainicio=fechaInicioProyecto,
                                                                fechafin=fechaFinProyecto,
                                                                lider=liderProyecto),
                           follow_redirects=True)
        assert self.crearOK in rv.data
       
        # Crear Fase
        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), nombreProyecto)
       
        # Crea Una Fase
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombreFase,
                                                                fechainicio=fechaInicioFase,
                                                                fechafin=fechaFinFase,
                                                                numero=numeroFase),
                           follow_redirects=True)
        assert self.crearOK in rv.data
              
        # Inicializar proyecto
        self.inicializarProyecto(getProyecto(nombreProyecto))
        
        #Crear rol
        nombreRol='Rol1'
        crearT='on'
        
        self.testRoute(self.rolURL + getFase(numeroFase, getProyecto(nombreProyecto).id).id.__str__(), nombreFase)
        
        rv = self.app.post(self.crearRolURL,data=dict(nombre=nombreRol,
                                                      crearT=crearT),
                           follow_redirects=True)
        assert self.crearOK in rv.data
        
        #Editar rol
        newNombreRol = 'rol1'
        rv = self.app.get(self.editarRolURL + getRolNombre(nombreRol).id.__str__() , follow_redirects=True)
        assert self.editarRolTitle in rv.data
        rv = self.app.post(self.editarRolURL, data=dict(nombre=newNombreRol,
                                                                   crearT=crearT),
                           follow_redirects=True)
        assert self.editarOK in rv.data        
        
        #Eliminar rol
        self.testRoute(self.eliminarRolURL + getRolNombre(newNombreRol).id.__str__() , 'Eliminar')
        rv = self.app.post(self.eliminarRolURL, follow_redirects=True)
        assert self.eliminarOK in rv.data
        
        # Eliminar el proyecto y todas sus fases
        assert self.testBorrarProyecto(nombreProyecto)
        
        rv = self.logout()
        assert self.logoutMessage in rv.data
       
        print 'CRUD Rol [OK]'
        
    def testADCRol(self):
        # Dummy data
        nombreFase = 'Dummy Fase'
        fechaInicioFase = '2014-10-11'
        fechaFinFase = '2015-12-11'
        numeroFase = '1'
        # Crear Proyecto
        nombreProyecto = 'Dummy Project'
        fechaInicioProyecto = '2014-10-10'
        fechaFinProyecto = '2015-10-10'
        liderProyecto = '1'
       
        # Login
        rv = self.login()
        assert self.listProject in rv.data
       
        # Crear Proyecto
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombreProyecto,
                                                                fechainicio=fechaInicioProyecto,
                                                                fechafin=fechaFinProyecto,
                                                                lider=liderProyecto),
                           follow_redirects=True)
        assert self.crearOK in rv.data
       
        # Crear Fase
        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), nombreProyecto)
       
        # Crea Una Fase
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombreFase,
                                                                fechainicio=fechaInicioFase,
                                                                fechafin=fechaFinFase,
                                                                numero=numeroFase),
                           follow_redirects=True)
        assert self.crearOK in rv.data
              
        # Inicializar proyecto
        self.inicializarProyecto(getProyecto(nombreProyecto))
        
        #Crear rol
        nombreRol='Rol1'
        crearT='on'
        
        self.testRoute(self.rolURL + getFase(numeroFase, getProyecto(nombreProyecto).id).id.__str__(), nombreFase)
        
        rv = self.app.post(self.crearRolURL,data=dict(nombre=nombreRol,
                                                      crearT=crearT),
                           follow_redirects=True)
        assert self.crearOK in rv.data
        
        #Asignar un rol
        id_rol = getRolNombre(nombreRol).id.__str__()
        id_user = getUsuario(pms.app.default_user).id.__str__()
        
        nombre_user = getUsuario(pms.app.default_user).nombre
        
        self.testRoute(self.asignarRolURL + id_rol,self.listUser)
        rv = self.app.get(self.asignarRolActionURL + id_user ,follow_redirects=True)

        #Consultar        
        rv = self.app.get(self.consultarRolURL + id_rol, follow_redirects=True)
        assert nombre_user in rv.data
        
        #Desasignar
        self.testRoute(self.desasignarRolURL + id_rol, self.listUser)
        rv = self.app.get(self.desasignarRolActionURL + id_user,follow_redirects=True)
        
        #Consultar (que ya no esta en la lista)
        rv = self.app.get(self.consultarRolURL + id_rol, follow_redirects=True)
        assert nombre_user not in rv.data
        
        #Eliminar rol
        self.testRoute(self.eliminarRolURL + getRolNombre(nombreRol).id.__str__() , 'Eliminar')
        rv = self.app.post(self.eliminarRolURL, follow_redirects=True)
        assert self.eliminarOK in rv.data
        
        # Eliminar el proyecto y todas sus fases
        assert self.testBorrarProyecto(nombreProyecto)
        
        rv = self.logout()
        assert self.logoutMessage in rv.data
       
        print 'Asignar/Consultar/Desasignar Rol [OK]'

    def testOpItem(self):
        # Dummy data
        nombreFase = 'Dummy Fase'
        fechaInicioFase = '2014-10-11'
        fechaFinFase = '2015-12-11'
        numeroFase = '1'
        nombreFase2 = 'Dummy Fase2'
        fechaInicioFase2 = '2014-11-11'
        fechaFinFase2 = '2015-12-11'
        numeroFase2 = '2'
        # Crear Proyecto
        nombreProyecto = 'Dummy Project'
        fechaInicioProyecto = '2014-10-10'
        fechaFinProyecto = '2015-10-10'
        liderProyecto = '1'
       
        # Login
        rv = self.login()
        assert self.listProject in rv.data
       
        # Crear Proyecto
        rv = self.app.post(self.crearProyectoURL, data=dict(nombre=nombreProyecto,
                                                                fechainicio=fechaInicioProyecto,
                                                                fechafin=fechaFinProyecto,
                                                                lider=liderProyecto),
                           follow_redirects=True)
        assert self.crearOK in rv.data
       
        # Crear Fase
        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), nombreProyecto)
       
        # Crea Una Fase
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombreFase,
                                                                fechainicio=fechaInicioFase,
                                                                fechafin=fechaFinFase,
                                                                numero=numeroFase),
                           follow_redirects=True)
        assert self.crearOK in rv.data
        
        # Crear Fase (segunda)
        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), nombreProyecto)
       
        # Crea otra Fase
        rv = self.app.post(self.crearFaseURL, data=dict(nombre=nombreFase2,
                                                                fechainicio=fechaInicioFase2,
                                                                fechafin=fechaFinFase2,
                                                                numero=numeroFase2),
                           follow_redirects=True)
        assert self.crearOK in rv.data
              
        # Inicializar proyecto
        self.inicializarProyecto(getProyecto(nombreProyecto))
        
        #Crear rol
        nombreRol='Rol1'
        nombreRol2='Rol2'
        crearT='on'
        editarT='on'
        eliminarT='on'
        crearLB='on'
        eliminarLB='on'
        crearI='on'
        editarI='on'
        eliminarI='on'
        aprobarI='on'
        revivirI='on'
        reversionarI='on'
        asignarpadreI='on'
        asignarantecesorI='on'
        
        # Rol para la fase 1
        self.testRoute(self.rolURL + getFase(numeroFase, getProyecto(nombreProyecto).id).id.__str__(), nombreFase)
        
        rv = self.app.post(self.crearRolURL,data=dict(nombre=nombreRol,
                                                      crearT=crearT,
                                                      editarT=editarT,
                                                      eliminarT=eliminarT,
                                                      crearLB=crearLB,
                                                      eliminarLB=eliminarLB,
                                                      crearI=crearI,
                                                      editarI=editarI,
                                                      eliminarI=eliminarI,
                                                      aprobarI=aprobarI,
                                                      revivirI=revivirI,
                                                      reversionarI=reversionarI,
                                                      asignarpadreI=asignarpadreI,
                                                      asignarantecesorI=asignarantecesorI),
                           follow_redirects=True)
        assert self.crearOK in rv.data
        
        # Rol para la fase 2
        self.testRoute(self.rolURL + getFase(numeroFase2, getProyecto(nombreProyecto).id).id.__str__(), nombreFase2)
        
        rv = self.app.post(self.crearRolURL,data=dict(nombre=nombreRol2,
                                                      crearT=crearT,
                                                      editarT=editarT,
                                                      eliminarT=eliminarT,
                                                      crearLB=crearLB,
                                                      eliminarLB=eliminarLB,
                                                      crearI=crearI,
                                                      editarI=editarI,
                                                      eliminarI=eliminarI,
                                                      aprobarI=aprobarI,
                                                      revivirI=revivirI,
                                                      reversionarI=reversionarI,
                                                      asignarpadreI=asignarpadreI,
                                                      asignarantecesorI=asignarantecesorI),
                           follow_redirects=True)
        assert self.crearOK in rv.data
        
        #Asignar un rol
        id_rol = getRolNombre(nombreRol).id.__str__()
        id_rol2 = getRolNombre(nombreRol2).id.__str__()
        id_user = getUsuario(pms.app.default_user).id.__str__()
        
        #nombre_user = getUsuario(pms.app.default_user).nombre
        
        #Rol1
        self.testRoute(self.asignarRolURL + id_rol,self.listUser)
        rv = self.app.get(self.asignarRolActionURL + id_user ,follow_redirects=True)
        #Rol2
        self.testRoute(self.asignarRolURL + id_rol2,self.listUser)
        rv = self.app.get(self.asignarRolActionURL + id_user ,follow_redirects=True)
        
        
        #crear tipo item
        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), self.listFase)
        self.testRoute(self.tipoURL + getFase(numeroFase,getProyecto(nombreProyecto).id.__str__()).id.__str__(),self.listTipo)
        self.testRoute(self.crearTipoURL, 'Crear Tipo')
        
        #Tipo Item
        nombreTipo = 'Madera'
        comentarioTipo = 'Tipo de Item madera'
        rv = self.app.post(self.crearTipoURL, data=dict(nombre=nombreTipo,
                                                        comentario=comentarioTipo),
                           follow_redirects=True)
        assert self.crearOK in rv.data
        
        #Atributo
        nombreAtributo = 'Peso'
        tipoDatoAtributo = 'Numerico'
        rv = self.app.get(self.atributoURL + getTipoItemNombre(nombreTipo, getFase(numeroFase,getProyecto(nombreProyecto).id.__str__()).id.__str__()).id.__str__(),follow_redirects=True)
        self.testRoute(self.atributoURL + getTipoItemNombre(nombreTipo, getFase(numeroFase,getProyecto(nombreProyecto).id.__str__()).id.__str__()).id.__str__(), self.listAtributo)
        self.testRoute(self.crearAtributoURL,'Crear Atributo')
        rv = self.app.post(self.crearAtributoURL,data=dict(nombre=nombreAtributo,
                                                           tipoDato=tipoDatoAtributo),
                           follow_redirects=True)
        assert self.crearOK in rv.data
        
        #Para la segunda fase
        self.testRoute(self.faseURL + getProyecto(nombreProyecto).id.__str__(), self.listFase)
        self.testRoute(self.tipoURL + getFase(numeroFase2,getProyecto(nombreProyecto).id.__str__()).id.__str__(),self.listTipo)
        #Importar tipo de la primera fase
        nombreTipo2 = 'Madera Petrificada'
        comentarioTipo2 = 'Tipo de Item madera petrificada'
        self.testRoute(self.importarTipoURL, 'para importar o copiar')
        self.testRoute(self.importarTipoActionURL + getTipoItemNombre(nombreTipo, getFase(numeroFase,getProyecto(nombreProyecto).id.__str__()).id.__str__()).id.__str__(), 'nombre del Tipo')
        rv = self.app.post(self.importarTipoActionURL, data=dict(nombre=nombreTipo2,
                                                                 comentario=comentarioTipo2),
                           follow_redirects=True)
        assert self.importarOK in rv.data
        
        #Eliminar rol (ambos)
        self.testRoute(self.eliminarRolURL + getRolNombre(nombreRol).id.__str__() , 'Eliminar')
        rv = self.app.post(self.eliminarRolURL, follow_redirects=True)
        assert self.eliminarOK in rv.data
        
        self.testRoute(self.eliminarRolURL + getRolNombre(nombreRol2).id.__str__() , 'Eliminar')
        rv = self.app.post(self.eliminarRolURL, follow_redirects=True)
        assert self.eliminarOK in rv.data
        
        eliminarTipoItem(getTipoItemNombre(nombreTipo, getFase(numeroFase,getProyecto(nombreProyecto).id.__str__()).id.__str__()).id)
        eliminarTipoItem(getTipoItemNombre(nombreTipo2, getFase(numeroFase2,getProyecto(nombreProyecto).id.__str__()).id.__str__()).id)
        
        # Eliminar el proyecto y todas sus fases
        assert self.testBorrarProyecto(nombreProyecto)
        
        rv = self.logout()
        assert self.logoutMessage in rv.data
       
        print 'Operaciones con Items [OK]'