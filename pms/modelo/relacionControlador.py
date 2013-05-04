from entidad import Fase, Usuario, Rol, User_Rol, Relacion
from initdb import db_session, init_db
from tipoItemControlador import getTiposFase
from atributoControlador import getAtributosTipo, getAtributoId
from usuarioControlador import getUsuario,getUsuarioById,getUsuarios
from faseControlador import getFase, getFaseId, getFases

session = db_session()

def crearRelacion(ante_id=None,post_id=None,tipo=None):
    init_db()
    session = db_session()
    rel = Relacion(ante_id=ante_id, post_id=post_id,tipo=tipo)
    session.add(rel)
    session.commit()

def comprobarRelacion(ante_id=None,post_id=None):
    init_db()
    if int(ante_id) != int(post_id):   
        res = session.query(Relacion).filter(Relacion.ante_id==ante_id).filter(Relacion.post_id==post_id).first()
        if res:
            return True
        else:
            return False
    else:
        return True