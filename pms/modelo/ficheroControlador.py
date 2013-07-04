'''
Created on 03/07/2013

@author: sync

'''
from entidad import ValorFile
from initdb import db_session, init_db, shutdown_session

session = db_session()

def getFileByItemId(itemId=None):
    """
        Recupera un fichero de la base de datos, dado el id del item del cual es
        adjunto
        @param itemId: Identificador del Item del cual es adjunto el fichero 
    """
    init_db()
    respuesta = session.query(ValorFile).filter(ValorFile.item_id == itemId).first()
    shutdown_session()
    return respuesta

def getFileById(idFile=None):
    """
        Recupera un fichero de la base de datos,dado el id del fichero
        @param idFile: Identificador del fichero   
    """
    init_db()
    respuesta = session.query(ValorFile).filter(ValorFile.id == idFile).first()
    return respuesta

def eliminarFichero(idFile=None):
    """
        Elimina un fichero de la base de datos dado el id del fichero
        @param idFile: Identificador del fichero 
    """
    if(idFile):
        init_db()
        session.query(ValorFile).filter(ValorFile.id == idFile).delete()
        session.commit()
        shutdown_session()

def subirFichero(fichero=None,itemId=None):
    """
        Carga el fichero en la base de datos
        @param fichero: Es el fichero cargado por el cliente
        @param itemId: Identificador del item relacionado
    """
    
    if(fichero and itemId):
        init_db()
        
        vFile = session.query(ValorFile).filter(ValorFile.item_id == itemId).first()
        
        if vFile:
            vFile.nombre = fichero.filename
            vFile.valor = fichero.read()
            session.merge(vFile)
        else:
            vFile = ValorFile(itemId, fichero.read(), fichero.filename)
            session.add(vFile)
            
        session.commit()
        shutdown_session()
        return True
    
    return None