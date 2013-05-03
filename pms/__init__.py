from flask import Flask
app = Flask(__name__)
app.secret_key = "bacon"
import vista.proyectoVista
import vista.required
import vista.usuarioVista
import vista.faseVista
import vista.logVista
import vista.tipoVista
import vista.atributoVista
import vista.itemVista



app.add_url_rule('/admproyecto/',
                 view_func=vista.proyectoVista.AdmProyecto.as_view('admproyecto'),
                 methods=["GET", "POST"])

app.add_url_rule('/admfase/eliminarproyecto/',
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

app.add_url_rule('/admitem/crearitem/',
                 view_func=vista.itemVista.CrearItem.as_view('crearitem'),
                 methods=["GET", "POST"])

app.add_url_rule('/admitem/atributo/',
                 view_func=vista.itemVista.CompletarAtributo.as_view('completaratributo'),
                 methods=["GET", "POST"])