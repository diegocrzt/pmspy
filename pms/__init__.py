from flask import Flask
app = Flask(__name__)
app.config.from_object("config")
app.secret_key = "bacon"
app.default_user = 'admin'
app.default_password = '123456'
import vista.proyectoVista
import vista.required
import vista.usuarioVista
import vista.faseVista
import vista.logVista
import vista.tipoVista
import vista.atributoVista
import vista.paginar
import vista.itemVista
import vista.rolVista
import vista.lineaBaseVista
import modelo.rolControlador
import vista.funcionpop
import vista.solicitudVista

app.jinja_env.globals.update(esMiembro=modelo.peticionControlador.getMiembro)
app.jinja_env.globals.update(accionHabilitada=vista.funcionpop.funcionAReemplazar)
app.jinja_env.globals.update(tienePermiso=modelo.rolControlador.tienePermiso)
app.jinja_env.globals.update(permisoTipo=modelo.rolControlador.getPermisosStringTipoItem)
app.jinja_env.globals.update(permisoLB=modelo.rolControlador.getPermisosStringLB)
app.jinja_env.globals.update(permisoItem=modelo.rolControlador.getPermisosStringItem)
app.add_url_rule('/admproyecto/',
                 view_func=vista.proyectoVista.AdmProyecto.as_view('admproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/admproyecto/eliminarproyecto/',
                 view_func=vista.proyectoVista.Eliminarproyecto.as_view('eliminarproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/',
                 view_func=vista.logVista.Main.as_view('index'),
                 methods=["GET", "POST"])

app.add_url_rule('/admproyecto/',
                 view_func=vista.proyectoVista.AdmProyecto.as_view('admproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/admusuario/crearusuario/',
                 view_func=vista.usuarioVista.Crearusuario.as_view('crearusuario'),
                 methods=["GET", "POST"])

app.add_url_rule('/admusuario/',
                 view_func=vista.usuarioVista.AdmUsuario.as_view('admusuario'),
                 methods=["GET", "POST"])

app.add_url_rule('/admusuario/editarusuario/',
                 view_func=vista.usuarioVista.Editarusuario.as_view('editusuario'),
                 methods=["GET", "POST"])

app.add_url_rule('/admproyecto/crearproyecto/',
                 view_func=vista.proyectoVista.Crearproyecto.as_view('crearproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/crearfase/',
                 view_func=vista.faseVista.Crearfase.as_view('crearfase'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/editarfase/',
                 view_func=vista.faseVista.Editarfase.as_view('editarfase'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/inicializarproyecto/',
                 view_func=vista.proyectoVista.Inicializarproyecto.as_view('inicializarproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/eliminarfase/',
                 view_func=vista.faseVista.Eliminarfase.as_view('eliminarfase'),
                 methods=["GET", "POST"])

app.add_url_rule('/admusuario/eliminarusuario/',
                 view_func=vista.usuarioVista.Eliminarusuario.as_view('eliminarusuario'),
                 methods=["GET", "POST"])

app.add_url_rule('/admtipo/creartipo/',
                 view_func=vista.tipoVista.Creartipo.as_view('creartipo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admtipo/editartipo/',
                 view_func=vista.tipoVista.Editartipo.as_view('editartipo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admtipo/eliminartipo/',
                 view_func=vista.tipoVista.Eliminartipo.as_view('eliminartipo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admatributo/crearatributo/',
                 view_func=vista.atributoVista.Crearatributo.as_view('crearatributo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admatributo/eliminaratributo/',
                 view_func=vista.atributoVista.Eliminaratributo.as_view('eliminaratributo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admtipo/',
                 view_func=vista.tipoVista.AdmTipo.as_view('admtipo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admitem/crearitem/',
                 view_func=vista.itemVista.CrearItem.as_view('crearitem'),
                 methods=["GET", "POST"])

app.add_url_rule('/admitem/atributo/',
                 view_func=vista.itemVista.CompletarAtributo.as_view('completaratributo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admitem/editaritem/',
                 view_func=vista.itemVista.EditarItem.as_view('editaritem'),
                 methods=["GET", "POST"])

app.add_url_rule('/admitem/eliminaritem/',
                 view_func=vista.itemVista.Eliminaritem.as_view('eliminaritem'),
                 methods=["GET", "POST"])
app.add_url_rule('/admitem/crearitem/',
                 view_func=vista.itemVista.CrearItem.as_view('crearitem'),
                 methods=["GET", "POST"])

app.add_url_rule('/admitem/atributo/',
                 view_func=vista.itemVista.CompletarAtributo.as_view('completaratributo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admrol/crearrol/',
                 view_func=vista.rolVista.CrearRol.as_view('crearrol'),
                 methods=["GET", "POST"])

app.add_url_rule('/admrol/editarrol/',
                 view_func=vista.rolVista.EditarRol.as_view('editarrol'),
                 methods=["GET", "POST"])


app.add_url_rule('/admrol/eliminarrol/',
                 view_func=vista.rolVista.Eliminarrol.as_view('eliminarrol'),
                 methods=["GET", "POST"])

app.add_url_rule('/admtipo/importartipo/',
                 view_func=vista.tipoVista.ImportarTipo.as_view('importartipo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admtipo/admimportartipo/',
                 view_func=vista.tipoVista.AdmImportar.as_view('admimportartipo'),
                 methods=["GET", "POST"])

app.add_url_rule('/admlinea/',
                 view_func=vista.lineaBaseVista.AdmLineaBase.as_view('admlinea'),
                 methods=["GET"])

app.add_url_rule('/admlinea/eliminarlinea/',
                 view_func=vista.lineaBaseVista.EliminarLineaBase.as_view('eliminarlinea'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/comite/',
                 view_func=vista.faseVista.ListaMiembros.as_view('miembros'),
                 methods=["GET", "POST"])

app.add_url_rule('/admsolicitud/',
                 view_func=vista.solicitudVista.AdmSolicitud.as_view('admsolicitud'),
                 methods=["GET", "POST"])

app.add_url_rule('/admsolicitud/crear/',
                 view_func=vista.solicitudVista.Crearsolicitud.as_view('crearsolicitud'),
                 methods=["GET", "POST"])

app.add_url_rule('/admsolicitud/eliminar/',
                 view_func=vista.solicitudVista.EliminarSolicitud.as_view('eliminarsolicitud'),
                 methods=["GET", "POST"])

app.add_url_rule('/admsolicitud/editar/',
                 view_func=vista.solicitudVista.EditarSolicitud.as_view('editarsolicitud'),
                 methods=["GET", "POST"])

